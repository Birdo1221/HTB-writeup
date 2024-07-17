import random

# Array of integers
a = [
    0x244b28be, 0x0af77805, 0x110dfc17, 0x07afc3a1,
    0x6afec533, 0x4ed659a2, 0x33c5d4b0, 0x286582b8,
    0x43383720, 0x055a14fc, 0x19195f9f, 0x43383720,
    0x19195f9f, 0x747c9c5e, 0x0f3da237, 0x615ab299,
    0x6afec533, 0x43383720, 0x0f3da237, 0x6afec533,
    0x615ab299, 0x286582b8, 0x055a14fc, 0x3ae44994,
    0x06d7dfe9, 0x4ed659a2, 0x0ccd4acd, 0x57d8ed64,
    0x615ab299, 0x22e9bc2a
]

# Loop through each element in the array
for num in a:
    found = False
    for j in range(33, 126):
        random.seed(j)  # Set the seed
        if random.randint(0, 0xFFFFFFFF) == num:  # Simulate rand()
            print(chr(j), end='')  # Print the corresponding character
            found = True
            break
    if not found:
        print("Character not found for number:", hex(num))

print()  # Newline at the end
