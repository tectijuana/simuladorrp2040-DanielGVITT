# Alumno: Gutierrez Vizcarra Daniel 19210503
# Circuito que da uso a un Keypad.

from machine import Pin
import utime

matrix_keys = [['1', '2', '3', 'A'],
               ['4', '5', '6', 'B'],
               ['7', '8', '9', 'C'],
               ['*', '0', '#', 'D']]

keypad_rows = [9,8,7,6]
keypad_columns = [5,4,3,2]
col_pins = []
row_pins = []

guess = []
secret_pin = ['1','2','3','4','5','6']
led = Pin(15, Pin.OUT, Pin.PULL_UP)

for x in range(0,4):
    row_pins.append(Pin(keypad_rows[x], Pin.OUT))
    row_pins[x].value(1)
    col_pins.append(Pin(keypad_columns[x], Pin.IN, Pin.PULL_DOWN))
    col_pins[x].value(0)
    
def scankeys(): 
    for row in range(4):
        for col in range(4): 
            row_pins[row].high()
            key = None          
            if col_pins[col].value() == 1:
                print("You have pressed:", matrix_keys[row][col])
                key_press = matrix_keys[row][col]
                utime.sleep(0.3)
                guess.append(key_press)                            
            if len(guess) == 6:
                checkPin(guess)               
                for x in range(0,6):
                    guess.pop() 
                    
        row_pins[row].low()

def checkPin(guess):            
    if guess == secret_pin:       
        print("You got the secret pin correct")
        led.value(1)
        utime.sleep(3)
        led.value(0)        
    else:
        print("Better luck next time")          
    
print("Enter the secret Pin")

while True:
    scankeys()