import machine
import utime

invertor_button = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN) # for step-down convertor: ground on pin 18
relay_switch = machine.Pin(20, machine.Pin.OUT) # for relay: ground on pin 38, 3.3v(out) on pin 36

presses = 0
button_state = False

def button_logic():
  relay_switch.value(1)
  utime.sleep(1.5)
  relay_switch.value(0)

def button_handler(pin):
  global presses
  global button_state
  if button_state == False:
    if presses == 0:
      presses +=1
      button_logic()
  elif button_state == True:
    if presses == 1:
      presses +=1
      button_logic()
      presses = 0

def bounce_handler(pin):
  invertor_button.irq(handler=None)
  utime.sleep_ms(250)
  invertor_button.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=button_handler)
    
invertor_button.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=bounce_handler)

while True:
  if presses == 0 or presses == 2:
      button_state = False
      print(presses)
      print(button_state)
  elif presses == 1:
      button_state = True
      print(presses)
      print(button_state)
    
