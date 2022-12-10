import pygame
import pygame.key
import pong

# Initialize Pygame
pygame.init()
pygame.font.init()
big_font = pygame.font.Font('fonts/startfont.ttf', 100)
little_font = pygame.font.Font('fonts/startfont.ttf', 48)
tiny_font = pygame.font.Font('fonts/Bebas.ttf', 20)

# Set the width and height of the screen
info = pygame.display.Info()
screen_height = info.current_h
screen_width = info.current_w
size = (screen_width, screen_height)
flags = pygame.FULLSCREEN
screen = pygame.display.set_mode(size, flags, vsync=0)

# Set the screen background
bg_color = (255, 255, 255)
screen.fill(bg_color)

# Define the text to render
text1 = big_font.render("Pong", True, (0, 0, 0))
text2 = little_font.render("Play", True, (0, 0, 0))
text3 = little_font.render("Quit", True, (0, 0, 0))
text4 = tiny_font.render("\u00a9 Cole Tebou 2022", True, (0, 0, 0))

# Set the position of the text
text1_rect = text1.get_rect()
text1_rect.centerx = screen.get_rect().centerx
text1_rect.centery = screen.get_rect().centery - 100

text2_rect = text2.get_rect()
text2_rect.centerx = screen.get_rect().centerx
text2_rect.centery = screen.get_rect().centery

text3_rect = text3.get_rect()
text3_rect.centerx = screen.get_rect().centerx
text3_rect.centery = screen.get_rect().centery + 75

text4_rect = text4.get_rect()
text4_rect.centerx = screen.get_rect().centerx
text4_rect.centery = screen.get_rect().bottom - 30

# Draw the text on the screen
screen.blit(text1, text1_rect)
screen.blit(text2, text2_rect)
screen.blit(text3, text3_rect)
screen.blit(text4, text4_rect)

# Update the screen
pygame.display.flip()

# Define the game loop
running = True
while running:

    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            pos = pygame.mouse.get_pos()
            # Check if the user clicked on the "Play" button
            if text2_rect.collidepoint(pos):
                # Start the game
                pong.start_game()
            # Check if the user clicked on the "Quit" button
            elif text3_rect.collidepoint(pos):
                running = False

# Quit Pygame
pygame.quit()
