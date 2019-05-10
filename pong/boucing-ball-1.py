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

positionX = 32
speedX = 1

while True:
  gb.waitForUpdate()
  gb.display.clear()

  positionX = positionX + speedX

  gb.display.print("positionX: ")
  gb.display.print(positionX)
  gb.display.print("\nspeedX: ")
  gb.display.print(speedX)

  gb.display.fillRect(positionX, 32, 4, 4)

