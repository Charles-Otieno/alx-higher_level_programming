#!/usr/bin/python3
"""
# Takes a URL, sends a request, and displays X-Request-Id from response header.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        request_id = response.headers.get('X-Request-Id')
        print(request_id)
