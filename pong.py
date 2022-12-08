import pygame
import pygame.key

# Initialize Pygame
pygame.init()

# Set the window size
size = (800, 600)
screen = pygame.display.set_mode(size)

# Set the window title
pygame.display.set_caption("Pong")

# Set up the players and their rectangles
player1 = pygame.Rect(10, 250, 20, 100)  # Left edge of the screen
player2 = pygame.Rect(770, 250, 20, 100)  # Right edge of the screen

# Set the initial position and velocity of the circle
x = 400  # Initial x position
y = 300  # Initial y position
dx = 10  # Initial x velocity
dy = 10  # Initial y velocity

# Define the ball as a rectangle
ball = pygame.Rect(x-25, y-25, 50, 50)

# Set up the game loop
running = True
clock = pygame.time.Clock()  # Create a clock to control the frame rate
while running:
  # Check for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Check if the up or down keys are being pressed
  keys = pygame.key.get_pressed()
  if keys[pygame.K_UP]:
    player1.move_ip(0, -5)  # Move player1 up by 5
  if keys[pygame.K_DOWN]:
    player1.move_ip(0, 5)  # Move player1 down by 5
  if keys[pygame.K_w]:
    player2.move_ip(0, -5)  # Move player1 up by 5
  if keys[pygame.K_s]:
    player2.move_ip(0, 5)  # Move player1 down by 5

  # Update the game state
  x += dx  # Update the x position
  y += dy  # Update the y position
  ball.x = x - 25  # Update the ball rectangle's x position
  ball.y = y - 25  # Update the ball rectangle's y position

  # Check if the ball rectangle is colliding with any of the player rectangles or the edge of the screen
  if ball.colliderect(player1) or ball.colliderect(player2) or ball.left < 0 or ball.right > size[0]:
    dx = -dx  # Reverse the x velocity
  if ball.top < 0 or ball.bottom > size[1]:
    dy = -dy  # Reverse the y velocity

  # Draw the game state
  screen.fill((0, 0, 0))  # Fill the screen with black

  #Draw the player rectangles
  pygame.draw.rect(screen, (255, 255, 255), player1)
  pygame.draw.rect(screen, (255, 255, 255), player2)

  # Draw a white circle at the updated position
  pygame.draw.circle(screen, (255, 255, 255), (x, y), 25)

  pygame.display.flip()  # Update the display

  clock.tick(30)  # Limit the frame rate to 30 frames per second

# Clean up
pygame.quit()
