import machine
import utime

invertor_button = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN) # for step-down convertor: ground on pin 18
relay_switch = machine.Pin(20, machine.Pin.OUT) # for relay: ground on pin 38, 3.3v(out) on pin 36

def button_logic():
    relay_switch.value(1)
    utime.sleep(1.5)
    relay_switch.value(0)

def push_status():
    while True:
        if invertor_button.value() == 1:
            utime.sleep_ms(250)
            if invertor_button.value() == 1:
                button_logic()
                while True:
                    if invertor_button.value() == 0:
                        button_logic()
                        break

if __name__ == '__main__':
    push_status()
        

        
        
        
        
