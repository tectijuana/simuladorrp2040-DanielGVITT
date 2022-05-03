# Alumno: Gutierrez Vizcarra Daniel 19210503
# Circuito que prende una bocina.  

from machine import Pin
import utime
buzzer = Pin(21,Pin.OUT)

while True:
  buzzer.on()
  utime.sleep_ms(500)
  buzzer.off()
  utime.sleep_ms(500)