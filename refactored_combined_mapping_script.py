# This script creates a Pygame window with a tile-based map that supports camera movement and zooming.

import pygame

import sys


# Initialize Pygame

def initialize_screen():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Simple Pygame Map')
    return screen

# Load tile images (if you have images)
try:
    grass_image = pygame.image.load('assets/mapping/grass.png').convert()
except Exception as e:
    print(f"Error loading image: {e}")
try:
    water_image = pygame.image.load('assets/mapping/water.png').convert()
except Exception as e:
    print(f"Error loading image: {e}")
try:
    west_coast_asset_image = pygame.image.load("assets/mapping/west_coast.png").convert()
except Exception as e:
    print(f"Error loading image: {e}")
try:
    east_coast_asset_image = pygame.image.load("assets/mapping/east_coast.png").convert()
except Exception as e:
    print(f"Error loading image: {e}")
try:
    north_coast_asset_image = pygame.image.load("assets/mapping/north_coast.png").convert()
except Exception as e:
    print(f"Error loading image: {e}")
try:
    south_coast_asset_image = pygame.image.load("assets/mapping/south_coast.png").convert()
except Exception as e:
    print(f"Error loading image: {e}")

# Main game loop
running = True
clock = pygame.time.Clock()


# Camera properties
camera_x, camera_y = 0, 0
zoom_level = 1.0
# Default Speeds camera movement
camera_speed = 1
# Default Speeds of zooming
zoom_speed = 1.001

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    # Default Speeds camera movement
    camera_speed = 1
    # Default Speeds of zooming
    zoom_speed = 1.001
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]: 
        camera_speed = 7 
        zoom_speed = 1.01   
    if keys[pygame.K_LEFT]:
        camera_x -= camera_speed 
    if keys[pygame.K_RIGHT]:
        camera_x += camera_speed
    if keys[pygame.K_UP]:
        camera_y -= camera_speed 
    if keys[pygame.K_DOWN]:
        camera_y += camera_speed 
    if keys[pygame.K_a]:  # Zoom out
        zoom_level /= zoom_speed 
    if keys[pygame.K_s]:  # Zoom in
        zoom_level *= zoom_speed

    # Clear the screen
    screen.fill((0, 0, 0))

    
    # Draw the map with camera and zooming
    for row_index, row in enumerate(tile_map):
        for col_index, tile in enumerate(row):
            tile_x = (col_index * TILE_SIZE - camera_x) * zoom_level
            tile_y = (row_index * TILE_SIZE - camera_y) * zoom_level
            zoomed_tile_size = TILE_SIZE * zoom_level
            if tile == 0:
                # Draw grass
                screen.blit(pygame.transform.scale(grass_image, (int(zoomed_tile_size), int(zoomed_tile_size))), (tile_x, tile_y))
            elif tile == 1:
                # Draw water
                screen.blit(pygame.transform.scale(water_image, (int(zoomed_tile_size), int(zoomed_tile_size))), (tile_x, tile_y))
            # Add more tile types as needed


    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
