# ----------------------------------------------------------
# Pong
# Gamebuino Academy Workshop
# 
# This is a CircuitPython port of the original C++ code
# Maybe not the more pythonic, but as close as possible
# to the original to be able to understand
# Original workshop: https://gamebuino.com/academy/workshop/make-your-very-first-games-with-pong/hello-world
# ----------------------------------------------------------
# Author: TitiMoby
# Date: May 2019
# ----------------------------------------------------------

import gamebuino_meta as gb

while True:
  gb.waitForUpdate()
  gb.display.clear()

  if(gb.buttons.pressed(BUTTON_UP)):
    counter = counter + 1
    gb.sound.playOK()

  if(gb.buttons.pressed(BUTTON_DOWN)):
    counter = counter - 1
    gb.sound.playCancel()

  if(gb.buttons.pressed(BUTTON_MENU)):
    counter = 0
    gb.sound.playTick()

  gb.display.setColor(BROWN)
  gb.display.fillRect(0, 0, counter, gb.display.height())

  gb.display.setColor(WHITE)
  gb.display.setFontSize(4)
  gb.display.setCursor(8,8)
  gb.display.print(counter)
