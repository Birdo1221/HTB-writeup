#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    // Array of specific integer values
    int values[] = {
        0x244b28be, 0x0af77805, 0x110dfc17, 0x07afc3a1, 0x6afec533,
        0x4ed659a2, 0x33c5d4b0, 0x286582b8, 0x43383720, 0x055a14fc,
        0x19195f9f, 0x43383720, 0x19195f9f, 0x747c9c5e, 0x0f3da237,
        0x615ab299, 0x6afec533, 0x43383720, 0x0f3da237, 0x6afec533,
        0x615ab299, 0x286582b8, 0x055a14fc, 0x3ae44994, 0x06d7dfe9,
        0x4ed659a2, 0x0ccd4acd, 0x57d8ed64, 0x615ab299, 0x22e9bc2a
    };

    // Loop through each value in the array
    for (int i = 0; i < 30; i++) {
        // Check ASCII values from 33 to 126
        for (int ascii_value = 33; ascii_value < 126; ascii_value++) {
            srand(ascii_value);  // Seed the random number generator
            if (rand() == values[i]) {
                printf("%c", ascii_value);  // Print the corresponding character
            }
        }
    }
    printf("\n");  // Print a newline
    return 0;  // Exit the program
}
