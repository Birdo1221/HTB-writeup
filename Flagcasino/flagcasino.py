from textwrap import wrap

# Input string containing hexadecimal characters
hex_string = "be284b240578f70a17fc0d11a1c3af0733c5fe6aa259d64eb0d4c533b882652820373843fc145a059f5f1919203738439f5f19195e9c7c7437a23d0f99b25a6133c5fe6a2037384337a23d0f33c5fe6a99b25a61b8826528fc145a059449e43ae9dfd706a259d64ecd4acd0c64edd85799b25a612abce922"

# Split the string into chunks of 8 characters
chunks = wrap(hex_string, 8)
reordered_chunks = []

# Rearrange the bytes within each chunk
for chunk in chunks:
    reordered = (
        chunk[6] + chunk[7] +  # Last two characters
        chunk[4] + chunk[5] +  # Middle two characters
        chunk[2] + chunk[3] +  # Next two characters
        chunk[0] + chunk[1]     # First two characters
    )
    reordered_chunks.append(reordered)

# Print the resulting reordered chunks
print(reordered_chunks)
