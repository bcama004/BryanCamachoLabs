"""
This will randomly generate the pattern of 5 entries to be repeated by the players
"""

import utime
import random

random.seed(utime.ticks_ms())

# Define a class that encapsulates the random number generation
class RandomNumberGenerator:
    def __init__(self, seed=None):
        # Initialize the random number generator with the provided seed or current time
        if seed is not None:
            random.seed(seed)

    def generate_random_array(self):
        # Initialize an empty array to store the random numbers
        random_numbers = []

        # Loop 5 times to generate 5 random numbers
        for _ in range(5):
            # Generate a random number between 1 and 4
            random_num = random.randint(1, 4)
            # Append the random number to the array
            random_numbers.append(random_num)

        print(random_numbers)
        return random_numbers