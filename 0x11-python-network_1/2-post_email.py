#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Eg: ./2-post_email.py <URL> <email>
"""


import sys
from urllib import request
from urllib import parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    data_encoded = parse.urlencode(data).encode('ascii')

    # Make a POST request to the provided URL with the email parameter
    with request.urlopen(url, data=data_encoded) as response:
        print(response.read().decode('utf-8'))
