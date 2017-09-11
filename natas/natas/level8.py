
#!/usr/bin/python
# coding: utf-8
from requests.auth import HTTPBasicAuth
import requests
import sys
import re

def exploit(level8pass):
    print "{+} Natas Level 8. Doing magic..."
    print "{*} First we grab the secret value..."
    try:
        r = requests.get(url="http://natas8.natas.labs.overthewire.org/index-source.html", auth=HTTPBasicAuth('natas8', level8pass))
    except Exception:
        print "{-} Something fucked up, request failed. Bailing. Maybe your password was wrong?"
        return None
    secrets = re.findall("=&nbsp;\"(.*?)\";", r.text)
    if len(secrets):
        secret = secrets[0]
    else:
        print "{-} Failed to grab secret. WTF?"
        return None
    decoded_secret = secret.decode("hex")[::-1].decode("base64")
    print "{*} Secret is %s" %(decoded_secret)
    print "{*} Now we do the next bit..."
    data = {"secret": decoded_secret, "submit": "submit"}
    try:
        r = requests.post(url="http://natas8.natas.labs.overthewire.org/", auth=HTTPBasicAuth('natas8', level8pass), data=data)
    except Exception:
        print "{-} Something fucked up, request failed. Bailing. Maybe your password was wrong?"
        return None
#    print r.text
    password = re.findall("natas9 is (.*?)\n", r.text)
    if len(password):
        return password[0]
    return None



def main(args):
    if len(args) != 2:
        sys.exit("use: %s level8password" %(args[0]))
    level9pass = exploit(args[1])
    if level9pass != None:
        print "{$$} Level 9 Password is: %s" %(level9pass)

if __name__ == "__main__":
    main(args=sys.argv)
