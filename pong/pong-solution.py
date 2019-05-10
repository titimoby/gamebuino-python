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
from random import randint

# ball attributes
ball_posX = 20
ball_posY = 20
ball_speedX = 1
ball_speedY = 1
ball_size = 3

# paddle1 attributes
paddle1_posX = 10
paddle1_posY = 30

# paddle2 attributes
paddle2_posX = gb.display.width() - 13
paddle2_posY = 30

# Dimensions for both paddles
paddle_height = 10
paddle_width = 3

# For the AI
paddle2_speedY = 0  # Vertical speed of the AI's paddle

# Scores
score1 = 0  # Player 1's score
score2 = 0  # Player 2's score

difficulty = 3  # Level of difficulty. 3 = EASY et 2 = HARD

while True:
  gb.waitForUpdate()
  gb.display.clear()

  # Difficulty switch
  if (gb.buttons.pressed(gb.buttons.MENU)):
    if (difficulty == 3): # Easy
      difficulty = 2  # Change difficulty
    else:  # Hard
      difficulty = 3  # Change difficulty

  # Update paddle 1 (player controlled paddle)
  if (gb.buttons.repeat(gb.buttons.UP, 0)):
    paddle1_posY = paddle1_posY - 1 
  if (gb.buttons.repeat(gb.buttons.DOWN, 0)):
    paddle1_posY = paddle1_posY + 1

  # Update paddle2 (AI controlled paddle)
  if (ball_posY > paddle2_posY + paddle_height / 2 and randint(0, difficulty) == 1):
    paddle2_speedY = 2
  elif (ball_posY < paddle2_posY + paddle_height / 2 and randint(0, difficulty) == 1):
    paddle2_speedY = -2
  
  paddle2_posY = paddle2_posY + paddle2_speedY  # Update paddle2's position

  # Update ball
  ball_posX = ball_posX + ball_speedX
  ball_posY = ball_posY + ball_speedY

  # Collisions with walls
  if (ball_posY < 0):
    ball_speedY = 1 
  if (ball_posY > gb.display.height() - ball_size):
    ball_speedY = -1

  # Collision with paddle1
  if ( (ball_posX == paddle1_posX + paddle_width) \
       and (ball_posY + ball_size >= paddle1_posY) \
       and (ball_posY <= paddle1_posY + paddle_height) ):
    ball_speedX = 1
  
  # Collision with paddle2
  if ( (ball_posX + ball_size == paddle2_posX) \
       and (ball_posY + ball_size >= paddle2_posY) \
       and (ball_posY <= paddle2_posY + paddle_height) ):
    ball_speedX = -1
  
  # Check if the ball exited the screen
  if (ball_posX < 0):
    # Reset the ball
    ball_posX = 20
    ball_posY = randint(20, gb.display.height() - 20)  # Random position along the Y axis
    ball_speedX = 1

    if (randint(0, 2) == 1):  # 50% of the time, this is true
      ball_speedY = 1
    else:  # Other 50% of the time
      ball_speedY = -1

    # Increment player 2's score
    score2 = score2 + 1

  if (ball_posX > gb.display.width()):
    # Reset ball
    ball_posX = 20
    ball_posY = randint(20, gb.display.height() - 20)  # Random position along the Y axis
    ball_speedX = 1

    if (randint(0, 2) == 1):  # 50% of the time, this is true
      ball_speedY = 1
    else:  # Other 50% of the time
      ball_speedY = -1

    # Increment player 1's score
    score1 = score1 + 1

  # Draw ball
  gb.display.fillRect(ball_posX, ball_posY, ball_size, ball_size)
  # Draw paddle1
  gb.display.fillRect(paddle1_posX, paddle1_posY, paddle_width, paddle_height)
  # Draw paddle2
  gb.display.fillRect(paddle2_posX, paddle2_posY, paddle_width, paddle_height)

  # Draw scores
  # gb.display.setCursor(35, 5) # this method is not present in CircuitPython 0.0.5
  gb.display.print(35, 5, score1)
  # gb.display.setCursor(42, 5) # this method is not present in CircuitPython 0.0.5
  gb.display.print(52, 5, score2)

  # Draw difficulty
  # gb.display.setCursor(33, gb.display.height() - 5) # this method is not present in CircuitPython 0.0.5
  if (difficulty == 3):
    gb.display.print(33, gb.display.height() - 5, "EASY")
  else:
    gb.display.print(33, gb.display.height() - 5, "HARD")
  
