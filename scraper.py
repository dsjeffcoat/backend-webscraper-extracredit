"""
Scrape car data and recreate our own HTML page with it.

URL: http://kenzie.academy

TODO:
- get HTML of the site to scrape
- read the contents of the HTML
- extract specific data that we want from the HTML
    - URLs
    - emails
    - phone numbers
- display extracted data
    - build a parser in order to display on terminal
"""

__author__ = 'Diarte Jeffcoat'

import requests
import re
import argparse
import sys


def scrape_links(url):
    """Search and return all URL links within a webpage"""
    request = requests.get(url).text
    links = re.findall(
        r'''
        http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+
        ''', request)
    for link in links:
        print(link)


def scrape_emails(url):
    """Search and return all email addresses within a webpage"""
    request = requests.get(url).text
    emails = re.findall(
        r'([a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+)', request)
    for email in emails:
        print(email)


def scrape_nums(url):
    """Search and return all phone numbers within a webpage"""
    request = requests.get(url).text
    nums = re.findall(
        r'''
        (\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4})
        ''', request)
    for num in nums:
        print(num)


def create_parser():
    '''Create an argument parser object for command
    line arguments in the terminal'''
    parser = argparse.ArgumentParser(
        description='''Search within a web URL for other
        URLs, email addresses, and phone numbers.''')
    # Positional Arguments
    parser.add_argument('url', type=str, help='URL address to scrape')
    # Optional Arguments
    parser.add_argument(
        '-l', '--link', help='search for specific URLs within main URL')
    parser.add_argument(
        '-e', '--email', help='search for specific emails within main URL')
    parser.add_argument(
        '-n', '--num', help='search for phone numbers within main URL')
    return parser


def main(args):
    parser = create_parser()
    ns = parser.parse_args(args)
    link = ns.url

    # html = requests.get(link).text
    # print(html)

    print(f'{"-"*40}\n')
    print("URLs:\n")
    scrape_links(link)
    print(f'{"-"*40}\n')
    print("Email Addresses:\n")
    scrape_emails(link)
    print(f'{"-"*40}\n')
    print("Phone Numbers:\n")
    scrape_nums(link)


if __name__ == '__main__':
    main(sys.argv[1:])
