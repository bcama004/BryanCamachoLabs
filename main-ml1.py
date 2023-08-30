import time
import machine
import utime
from Lights import *
from Buzzer import *
from Displays import *

time.sleep(0.1) # Wait for USB to become ready

print("Hello, MSIS Students!")

#Define the pin for the internal LED
# led pin = machine.pin(25, machine.Pin.Out)

myled = Light(25, "Internal LED")

# Turn on LED
#led_pin.value(1)

myled.on()

# Wait for a few seconds
utime.sleep(1)

#Turn off the LED
# led_pin.value(0

myled.off()

extled = DimLight(22, "Blue LED")
extled.on()
utime.sleep(1)
extled.setBrightness(100)
utime.sleep(1)
extled.off()
extled.upDown()

mybuzzer = PassiveBuzzer(16)
mybuzzer.beep()

mydisplay = LCDDisplay(sda=0, scl=1, i2cid=0)
mydisplay.showText(' This is Sparta! ')
