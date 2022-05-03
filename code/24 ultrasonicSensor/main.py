# Alumno: Gutierrez Vizcarra Daniel 19210503
# Circuito que prende un sensor ultrasonico. 

from machine import Pin
import utime

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()

   while echo.value() == 0:
       signaloff = utime.ticks_us()

   while echo.value() == 1:
       signalon = utime.ticks_us()
       
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   print("La Distancia del Objeto es ",distance,"cm")

while True:
   ultra()
   utime.sleep(1)
