import machine
import utime

invertor_button = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN) # for step-down convertor: ground on pin 18
relay_switch = machine.Pin(20, machine.Pin.OUT) # for relay: ground on pin 38, 3.3v(out) on pin 36

pressed = False

def button_logic():
    relay_switch.value(1)
    utime.sleep(1.5)
    relay_switch.value(0)

def button_handler(pin):
    global pressed
    invertor_button.irq(handler=None)
    utime.sleep_ms(250)
    invertor_button.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=button_handler)
    if not pressed:
      button_logic()
      pressed = True
    else:
      button_logic()
      pressed = False
      
invertor_button.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=button_handler)

        

        
        
        
        
