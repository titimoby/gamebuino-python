# ----------------------------------------------------------
# Read analog value on aport
# Used in video Gamebuino 01 - Découverte de la console et premiers montages électroniques
# https://youtu.be/NQbfONUid2U
# ----------------------------------------------------------
# Author: TitiMoby
# Date: May 2019
# ----------------------------------------------------------
import gamebuino_meta as gb
import time
import board
from analogio import AnalogIn
 
analog_in = AnalogIn(board.A1) 
 
def get_voltage(pin):
    # Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 3.3V)
    # max voltage mesured 3.8V fully charged but I added a protection resistor so, it's an almost
    return (pin.value * 3.3) / 1023.0
 
while True:
    gb.waitForUpdate()
    gb.display.clear()
    print(print((analog_in.value,)))
    gb.display.setColor(gb.color.WHITE)
    gb.display.setFontSize(3)
    gb.display.print(8, 8, analog_in.value)