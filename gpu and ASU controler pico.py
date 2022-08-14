import machine 
import utime as time
from machine import Pin

beam_pin = Pin(15, Pin.IN, Pin.PULL_UP)
beam_pin2 = Pin(18, Pin.IN, Pin.PULL_UP)
gpu1 = Pin(16, Pin.OUT)
leds1 = Pin(17, Pin.OUT)
old_beam_value = beam_pin.value()
old_beam_value2 = beam_pin2.value()

while True:
    if old_beam_value != beam_pin.value():
        gpu1.value(1) #Turn on gpu movement relay
        leds1.value(1) #Turn on signal wire for 2nd pico for proper strobe effects
        leds2.value(1) #Turn on GPU unit lights
        time.sleep(.5)
        gpu1.value(0)
        leds1.value(0)
        time.sleep(20)
        leds2.value(1)
        gpu1.value(1)
        time.sleep(.5)
        gpu1.value(0)
        
    elif old_beam_value2 != beam_pin2.value():
        
    time.sleep(0.1)








#led.value(1)   #Set led turn on
  
#time.sleep(0.5)
  
#led.value(0)   #Set led turn off
  