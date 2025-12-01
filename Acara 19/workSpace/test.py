from machine import Pin
from time import sleep
Led=Pin(2,Pin.OUT)

while True:
  Led.value(not Led.value())
  sleep(0.5)
  
