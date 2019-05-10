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
speedX = 2
positionY = 32
speedY = 1
ballSize = 8

while True:
  gb.waitForUpdate()
  gb.display.clear()

  # Update horizontal position
  positionX = positionX + speedX

  # If the ball reaches the left side of the screen
  if(positionX < 0):
    # Go right
    speedX = 1

  # If the ball reaches the right side of the screen
  if(positionX > gb.display.width() - ballSize):
    # Go left
    speedX = -1

  # Update vertical position
  positionY = positionY + speedY

  # If the ball reaches the top side of the screen
  if(positionY < 0):
    # Go down
    speedY = 1

  # If the ball reaches the bottom side of the screen
  if(positionY > gb.display.height() - ballSize):
    # Go up
    speedY = -1

  gb.display.setColor(gb.color.BROWN)
  gb.display.print("positionX: ")
  gb.display.print(positionX)
  gb.display.print("\nspeedX: ")
  gb.display.print(speedX)


  gb.display.print("\npositionY: ")
  gb.display.print(positionY)
  gb.display.print("\nspeedY: ")
  gb.display.print(speedY)


  gb.display.setColor(gb.color.WHITE)
  gb.display.fillRect(positionX, positionY, ballSize, ballSize)

