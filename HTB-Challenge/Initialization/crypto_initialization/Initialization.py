from pwn import unhex, xor

# Known plaintext messages
text = [
    'This is some public information that can be read out loud.',
    'No one can crack our encryption algorithm.',
    'HTB{?????????????????????????????????????????????}',
    'Secret information is encrypted with Advanced Encryption Standards.'
]

# Hex-encoded ciphertexts from output.txt
cipher = '''2ac199d1395745812e3e5d3c4dc995cd2f2a076426b70fd5209cdd5ddc0a0c372feb3909956a791702180f591a63af184c27a6ba2fd61c1741ea0818142d0b92
30c6d0cd775b16c23c3f103a1fd883c4632c11366fbc07d92088cc5ddc0a0c373aef3f12c7606c114f546c7f6e00c87a
36fdb2d97d0a5bcf0225586a1e8abfc62d3057273aab5ae5309d8c4ade060a236aed070d817b2c14110e590b1b27ef5d4d35ddc001b47d6c2bca00101c25039a
2dcc93d07c4a16c833375f2b00d894c62c2d442d3cf90cd43183c559c10006372cea2c1595487c0f4314091c0c268b120f3aaabe7bd31c0c05977a7f7c4f6ce6f59392e0e522e66500e153f7a6f914c7'''.splitlines()

# Decrypt the flag by XORing the ciphertext of the unknown message with a known plaintext and its ciphertext
flag = xor(unhex(cipher[2]), unhex(cipher[3]), text[3].encode())
print(flag)
