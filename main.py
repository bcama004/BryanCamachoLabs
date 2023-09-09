import time
from MemoryGame import *
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

game = MemoryGame()
game.run()