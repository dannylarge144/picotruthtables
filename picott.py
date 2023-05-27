import machine
import utime
print("--- Welcome to light up truth tables! ---")
led_ex = machine.Pin(15, machine.Pin.OUT)
led_ex2 = machine.Pin(14, machine.Pin.OUT)
led_onboard = machine.Pin(25, machine.Pin.OUT)
while True:
    operator = input("Select A: AND, O: OR, N: NAND, R: NOR, X: XOR, E: EQUIV/XNOR, I: IMPLICATION").upper()
    if(not(operator == "A" or operator == "O" or operator == "N" or operator == "R" or operator == "X" or operator == "E" or operator == "I")):
         print("Please select an option from the list.")
    else:
        led_ex.value(1)
        led_ex2.value(1)
        for i in range(2):
            led_ex2.toggle()
            for j in range(2):
                led_ex.toggle()
                if(operator == "A"):
                    if(led_ex.value() and led_ex2.value()):
                        led_onboard.value(1)
                    else:
                        led_onboard.value(0)
                elif(operator == "O"):
                    if(led_ex.value() or led_ex2.value()):
                        led_onboard.value(1)
                    else:
                        led_onboard.value(0)
                elif(operator == "N"):
                    if(not(led_ex.value() and led_ex2.value())):
                        led_onboard.value(1)
                    else:
                        led_onboard.value(0)
                elif(operator == "R"):
                    if(not(led_ex.value() or led_ex2.value())):
                        led_onboard.value(1)
                    else:
                        led_onboard.value(0)
                elif(operator == "X"):
                    if((led_ex.value() or led_ex2.value()) and not (led_ex.value() and led_ex2.value())):
                        led_onboard.value(1)
                    else:
                        led_onboard.value(0)
                elif(operator == "E"):
                    if(led_ex.value() == led_ex2.value()):
                        led_onboard.value(1)
                    else:
                        led_onboard.value(0)
                elif(operator == "I"):
                    if(led_ex.value()):
                        if(led_ex2.value()):
                            led_onboard.value(1)
                        else:
                            led_onboard.value(0)
                    else:
                        led_onboard.value(1)
                else:
                    print("This should not be reachable.")
                utime.sleep(1)
    led_ex.value(0)
    led_ex2.value(0)
    led_onboard.value(0)
