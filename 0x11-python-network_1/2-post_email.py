#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": "sys.argv[2]"}
    """ encoding the data fromdictionary to byte object"""
    encoding_value = urllib.parse.urlencode(value)
    """convert to byte"""
    value_coded = encoding_value.encode("ascii")

        
    with urllib.request.urlopen(url, data = value_coded) as response:
        print(response.read().decode("utf-8"))
