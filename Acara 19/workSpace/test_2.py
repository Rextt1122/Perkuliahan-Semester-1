from machine import Pin

led = Pin(2, Pin.OUT)

def hidup():
    led.value(0)   # karena active-low → 0 = ON
    print("LED hidup")

def mati():
    led.value(1)   # 1 = OFF
    print("LED mati")

