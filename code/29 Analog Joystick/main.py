from machine import Pin, ADC
import utime

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
button = Pin(16,Pin.IN, Pin.PULL_UP)

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    xStatus = "middle"
    yStatus = "middle"
    buttonStatus = "not pressed"
    if xValue <= 600:
        xStatus = "right"
    elif xValue >= 60000:
        xStatus = "left"
    if yValue <= 600:
        yStatus = "down"
    elif yValue >= 60000:
        yStatus = "up"
    if buttonValue == 0:
        buttonStatus = "pressed"
    print("X: " + xStatus + ", Y: " + yStatus + " -- button " + buttonStatus)
    utime.sleep(0.1)