import pygame
import os

#import main

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
MENU_HEIGHT = 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
developer_option = False

# Build icon and menu variables
build_icon = pygame.Surface((50, 50))  # Placeholder for an icon
build_icon.fill((255, 0, 0))  # Red square as a placeholder
build_menu_visible = False
build_menu_rect = pygame.Rect(0, HEIGHT - MENU_HEIGHT, WIDTH, MENU_HEIGHT)
visibility_changes = False


map_path = os.path.join(MAPPING_PATH, "q_mapping.png")
print(map_path)

# Load the map
map_image = pygame.image.load(map_path)
map_rect = map_image.get_rect()
map_position = [0, 0]  # Initial position
zoom_level = 1.0  # Initial zoom level

# Class for Buildings

# List to store buildings
buildings = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        
        # Display all events in case it is needed (developer option)
        if developer_option:
            if event:
                print(event)

        # Handle quitting event by user    
        if event.type == pygame.QUIT:
            running = False
    #building_menu = Button
        # Mouse click 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse is down and store this state
            if event.button == 1:  # Left click
                mouse_down = True
            # Mouse position when clicking down 
            mouse_position = event.pos    


    # Clear screen
    screen.fill((0, 0, 0))


    # Draw build icon
    screen.blit(build_icon, (0, HEIGHT - 50))


    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()