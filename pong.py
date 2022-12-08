import pygame
import pygame.key

# Initializations 
pygame.init()
pygame.font.init()
font = pygame.font.Font('fonts/myfont.ttf', 24)

# Set the window size
size = (800, 600)
screen = pygame.display.set_mode(size)

# Set the window title
pygame.display.set_caption("Pong")

# Set up the players and their rectangles
player = pygame.Rect(20, 250, 20, 100)  # Left edge of the screen
player_score = 0
ai = pygame.Rect(760, 250, 20, 100)  # Right edge of the screen

# Set the initial position and velocity of the circle
x = 400  # Initial x position
y = 300  # Initial y position
dx = 10  # Initial x velocity
dy = 10  # Initial y velocity
radius = 20

#Speeds
ai_speed = 7
player_speed = 10

# Define the ball as a rectangle
ball = pygame.Rect(x-25, y-25, 2*radius, 2*radius)

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
    player.move_ip(0, -player_speed)  # Move player1 up by 5 on up arrow
  if keys[pygame.K_DOWN]:
    player.move_ip(0, player_speed)  # Move player1 down by 5 on down arrow
  if ball.y < ai.y:
    ai.move_ip(0, -ai_speed)  # Move player2 closer to ball
  if ball.y > ai.y:
    ai.move_ip(0, ai_speed)  # Move player2 closer to ball

  # Update the game state
  x += dx  # Update the x position
  y += dy  # Update the y position
  ball.x = x - 25  # Update the ball rectangle's x position
  ball.y = y - 25  # Update the ball rectangle's y position

  # Check if the ball rectangle is colliding with any of the player rectangles or the edge of the screen
  if ball.colliderect(player) or ball.colliderect(ai) or ball.left < 0 or ball.right > size[0]:
    dx = -dx  # Reverse the x velocity
  if ball.top < 0 or ball.bottom > size[1]:
    dy = -dy  # Reverse the y velocity

  # Draw the game state
  screen.fill((0, 0, 0))  # Fill the screen with black
  player_score_text = font.render(f'Score: {player_score}', True, (255,255,255))
  screen.blit(player_score_text, (10, 10))

  #Draw the player rectangles
  pygame.draw.rect(screen, (255, 255, 255), player)
  pygame.draw.rect(screen, (255, 255, 255), ai)

  # Draw a white circle at the updated position
  pygame.draw.circle(screen, (255, 255, 255), (x, y), radius)

  pygame.display.flip()  # Update the display

  clock.tick(30)  # Limit the frame rate to 30 frames per second

# Clean up
pygame.quit()
