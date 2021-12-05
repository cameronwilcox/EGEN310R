from pyPS4Controller.controller import Controller
from Motor import *
from Led import *
from Buzzer import *
from Command import COMMAND as cmd

PWM = Motor()
led = Led()
buzzer = Buzzer()

lightsOn = False
boost = False
forward = -2500
backward = 2500
 

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        global lightsOn
        if lightsOn:
            led.colorWipe(led.strip, Color(255,255,255))
            lightsOn = False
        else:
            led.colorWipe(led.strip, Color(0,0,0))
            lightsOn = True

    def on_x_release(self):
        global lightsOn
        if lightsOn:
            print("Lights on")
        else:
            print("Lights off")
        
    def on_up_arrow_press(self):
        print("Arrow up")
        PWM.setMotorModel(forward,forward,forward,forward)

    def on_up_down_arrow_release(self):
        PWM.setMotorModel(0,0,0,0)

    def on_down_arrow_press(self):
        PWM.setMotorModel(backward,backward,backward,backward)

    def on_left_arrow_press(self):
        PWM.setMotorModel(2000,2000,-1500,-1500)

    def on_right_arrow_press(self):
        PWM.setMotorModel(-1500,-1500,2000,2000)

    def on_left_right_arrow_release(self):
        PWM.setMotorModel(0,0,0,0)

    def on_circle_press(self):
        buzzer.run('1')

    def on_circle_release(self):
        buzzer.run('0')

    def on_square_press(self):
        global boost
        global forward
        global backward
        if boost:
            forward = -4000
            backward = 4000
            boost = False
        else:
            forward = -1000
            backward = 1000
            boost = True

    def on_square_release(self):
        global boost
        if boost:
            print("Boost off")
        else:
            print("Boost on")
#    def on_L3_left(self):
#        print("Stick left")
        
#    def on_L3_right(self):
#        print("Stick right")
        
#    def on_L3_up(self):
#        print("Stick up")
        
#    def on_L3_down(self):
#        print("Stick down")
        

ledOn = False
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
#controller.debug = True
controller.listen(timeout=60)
