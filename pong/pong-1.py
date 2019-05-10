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

# ball attributes
ball_posX = 20
ball_posY = 20
ball_speedX = 1
ball_speedY = 1
ball_size = 4

# paddle1 attributes
paddle1_posX = 10
paddle1_posY = 30

# Dimension of both paddles
paddle_height = 10
paddle_width = 3

while True:
  gb.waitForUpdate()
  gb.display.clear()

  # Update paddle1 position
  if (gb.buttons.repeat(gb.buttons.UP, 0)):
    paddle1_posY = paddle1_posY - 1  
  if (gb.buttons.repeat(gb.buttons.DOWN, 0)):
    paddle1_posY = paddle1_posY + 1

  # Update ball position
  ball_posX = ball_posX + ball_speedX
  ball_posY = ball_posY + ball_speedY

  # Collisions with walls
  if (ball_posY < 0):
    ball_speedY = 1
  if (ball_posY > gb.display.height() - ball_size):
    ball_speedY = -1  
  if (ball_posX > gb.display.width() - ball_size):
    ball_speedX = -1

  # Ball-paddle1 collisions
  if ( (ball_posX == paddle1_posX + paddle_width) \
    and (ball_posY + ball_size >= paddle1_posY) \
    and (ball_posY <= paddle1_posY + paddle_height) ):
    ball_speedX = 1  

  # Check if the ball left the screen (on the left side)
  if (ball_posX < 0):
    # Reset ball
    ball_posX = 20
    ball_posY = 20
    ball_speedX = 1
    ball_speedY = 1  


  # Display ball
  gb.display.fillRect(ball_posX, ball_posY, ball_size, ball_size)
  # Display paddle1
  gb.display.fillRect(paddle1_posX, paddle1_posY, paddle_width, paddle_height)
