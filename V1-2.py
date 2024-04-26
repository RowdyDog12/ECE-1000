# Import the necessary libraries
from machine import Pin, ADC, PWM,
import utime

# Joystick Input Variables
joy_button = Pin(19, Pin.IN)
joystick_x = ADC(Pin(26))
joystick_y = ADC(Pin(27))

# Define the min and max PWM for our servos 
MID = 1500000
MIN = 500000
MAX = 2500000

# Set which pins are used for PWM
pwmX = PWM(Pin(16))
pwmY = PWM(Pin(17))
pwm3 = PWM(Pin(18))

# Set frequencies for servos
pwmX.freq(50)
pwmY.freq(50)
pwm3.freq(50)

while True:
    # Read the joystick/Button values and store them into the correct variables
    xValue = joystick_x.read_u16()
    yValue = joystick_y.read_u16()
    buttonValue= joy_button.value()
        
    #Convert x Value from joystick into servo value 
    xConverted = int(((xValue / 32.6395) * 1000) + 500000)
    
    #Set max value
    if xConverted > 2500000:
        xConverted = 2500000
        
    #Set min value
    if xConverted < 500000:
        xConverted = 500000
      
    #Convert y Values from joystick into sero Value
    yConverted = int(((yValue / 32.6395) * 1000) + 500000)
    
    #Set max value
    if yConverted > 2500000:
        yConverted = 2500000
     
    #Set min value
    if yConverted < 500000:
        yConverted = 500000
    
    #Move X and Y servo based on joystick values
    pwmX.duty_ns(xConverted)
    pwmY.duty_ns(yConverted)
    
    #Move grip servo to Max
    if buttonValue == 1:
        pwm3.duty_ns(MAX)
        
    #Move grip servo to Min
    if buttonValue == 0:
        pwm3.duty_ns(MIN)
    
    # A reasonable delay
    utime.sleep(0.1)


