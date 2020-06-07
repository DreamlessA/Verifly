import RPi.GPIO as GPIO
import time

from enum import Enum
class Button(Enum):
    START = 0
    TRYAGAIN = 1
    QUIT = 2
    HELP = 3
for member in Button:
    globals()[member.name] = member

BUTTON_PINs =   {
                Button.START : 22,
                Button.TRYAGAIN: 17,
                Button.QUIT: 27,
                Button.HELP: 4
                }

for pin in BUTTON_PINs.values():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def wait_for_button_press(buttons, timeout=None):
    start_time = time.time()
    while timeout == None or time.time() < start_time + timeout:
        for button in buttons:
            button_status = GPIO.input(BUTTON_PINs[button])
            if button_status:
                return button
    return None