import time
import sys

lyrics = [
    "Don't wanna say goodbye"
    "Birds of a feather, we should stick together, I know ('til the day that I die)"
    "I said I'd never think I wasn't better alone ('til the light leaves my eyes)"
    "Can't change the weather, might not be forever ('til the day I die)"
    "But if it's forever, it's even better"
]

for line in lyrics:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)  # delay per huruf
    print()
    time.sleep(1)  # jeda antar baris
