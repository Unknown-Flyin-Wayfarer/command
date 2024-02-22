from machine import Pin 
import time
from lora import Lora    

led = Pin(25, Pin.OUT)
lora = Lora() 
 
while lora.isBusy: pass
    # Parse the received data to corresponding functions.
while True:
#     E_angles =input("Enter Euler Angles:")
#     lora.transmit(E_angles)
#     time.sleep_ms(100)
    while True:
        lora.transmit("d")
        time.sleep_ms(500)
        #s = lora.receive()
        #if len(s)>0: 
        #    print(str(s))	 
        #time.sleep_ms(50)
        
# rotmat()




