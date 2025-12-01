from machine import ADC, Pin
import time

ldr = ADC(0)        # baca sensor di pin A0
led = Pin(2, Pin.OUT)   # LED di GPIO2 (D4)

while True:
    nilai = ldr.read()     # 0..1023
    print(nilai)

    # Jika gelap (nilai kecil) → LED mati
    if nilai < 300:
        led.value(0)       # mati
    else:
        led.value(1)       # nyala

    time.sleep(0.2)

