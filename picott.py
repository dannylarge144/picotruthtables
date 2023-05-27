import machine
import utime
print("--- Welcome to light up truth tables! ---")
led_ex = machine.Pin(15, machine.Pin.OUT)
led_ex2 = machine.Pin(14, machine.Pin.OUT)
led_onboard = machine.Pin(25, machine.Pin.OUT)
while True:
    operator = input("Select A: AND, O: OR, N: NAND, R: NOR, X: XOR, E: EQUIV/XNOR, I: IMPLICATION")
    if(operator == "A"):
        led_ex.value(1)
        led_ex2.value(1)
        for i in range(2):
            led_ex2.toggle()
            for j in range(2):
                led_ex.toggle()
                if(led_ex.value() and led_ex2.value()):
                    led_onboard.value(1)
                else:
                    led_onboard.value(0)
                utime.sleep(1)
    elif(operator == "O"):
        led_ex.value(1)
        led_ex2.value(1)
        for i in range(2):
            led_ex2.toggle()
            for j in range(2):
                led_ex.toggle()
                if(led_ex.value() or led_ex2.value()):
                    led_onboard.value(1)
                else:
                    led_onboard.value(0)
                utime.sleep(1)
    elif(operator == "N"):
        led_ex.value(1)
        led_ex2.value(1)
        for i in range(2):
            led_ex2.toggle()
            for j in range(2):
                led_ex.toggle()
                if(not (led_ex.value() and led_ex2.value())):
                    led_onboard.value(1)
                else:
                    led_onboard.value(0)
                utime.sleep(1)
    elif(operator == "R"):
        led_ex.value(1)
        led_ex2.value(1)
        for i in range(2):
            led_ex2.toggle()
            for j in range(2):
                led_ex.toggle()
                if(not(led_ex.value() or led_ex2.value())):
                    led_onboard.value(1)
                else:
                    led_onboard.value(0)
                utime.sleep(1)
    elif(operator == "X"):
        led_ex.value(1)
        led_ex2.value(1)
        for i in range(2):
            led_ex2.toggle()
            for j in range(2):
                led_ex.toggle()
                if((led_ex.value() or led_ex2.value()) and not (led_ex.value() and led_ex2.value())):
                    led_onboard.value(1)
                else:
                    led_onboard.value(0)
                utime.sleep(1)
    elif(operator == "E"):
        led_ex.value(1)
        led_ex2.value(1)
        for i in range(2):
            led_ex2.toggle()
            for j in range(2):
                led_ex.toggle()
                if(led_ex.value() == led_ex2.value()):
                    led_onboard.value(1)
                else:
                    led_onboard.value(0)
                utime.sleep(1)
    elif(operator == "I"):
        led_ex.value(1)
        led_ex2.value(1)
        for i in range(2):
            led_ex2.toggle()
            for j in range(2):
                led_ex.toggle()
                if(led_ex.value()):
                    if(led_ex2.value()):
                        led_onboard.value(1)
                    else:
                        led_onboard.value(0)
                else:
                    led_onboard.value(1)
                utime.sleep(1)
    else:
        print("Please select an item from the list.")
    led_ex.value(0)
    led_ex2.value(0)
    led_onboard.value(0)
 
