# Draw a square with pygame
# Import and initialize the pygame library
import pygame

def main():
    pygame.init()

    # Set up the drawing window
    display = pygame.display.set_mode([100, 100])


    # Run until the user asks to quit
    #running = True
    # while running:
        # Close the window is user clicked close button
        # for event in pygame.event.get():
        #    if event.type == pygame.QUIT:
        #        running = False
    
  # Set colors
    WHITE=(255,255,255)
    BLUE=(0,0,255)
    
  # Fill the background with white
    display.fill(WHITE)

    # Draw a rectangle
    pygame.draw.rect(display, BLUE, (20,20,20,20))

    # Draw it
    pygame.display.update()

# Run it
main()

# Quit the game
pygame.quit()