# Alumno: Gutierrez Vizcarra Daniel 19210503
# Circuito que prende un led utilizando un Slide Switch y un Resistor. 

from machine import Pin
from time import sleep

led = Pin(14, Pin.OUT)
button = Pin(13, Pin.IN)

while True:
  
  logic_state = button.value()
  if logic_state == True:     
      led.value(1)             
  else:                       
      led.value(0)             
