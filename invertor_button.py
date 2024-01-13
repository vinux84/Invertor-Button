import machine
import utime

invertor_button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
relay_switch = machine.Pin(28, machine.Pin.OUT) 

def button_logic():
    relay_switch.value(1)
    utime.sleep(1.5)
    relay_switch.value(0)

while True:
    if invertor_button.value() == 1:
        button_logic()
        while True:
            if invertor_button.value() == 0:
                button_logic()
                break 
        

        
        
        
        
