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

  # Draw text to screen
  gb.display.print("Hello world\nis a tradition\nsince\n\n")

  # Change size of text
  gb.display.setFontSize(2)
  gb.display.print("1978")

  # Change color and revert to original size
  gb.display.setColor(gb.color.BROWN)
  gb.display.setFontSize(1)
  gb.display.print("\n\n\n     - GAMEBUINO")

