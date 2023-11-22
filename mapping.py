import pygame
import sys

# Initialize Pygame
pygame.init()

# Define constants
TILE_SIZE = 42
MAP_TILE_WIDTH = 37
MAP_TILE_HEIGHT = 19
SCREEN_WIDTH = TILE_SIZE * MAP_TILE_WIDTH
SCREEN_HEIGHT = TILE_SIZE * MAP_TILE_HEIGHT
FPS = 60

# Define colors in case of images assets loading failure 
GRASS_COLOR = (0, 255, 0)
WATER_COLOR = (0, 0, 255)

# Define the map - 0 for grass, 1 for water
tile_map = [
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0] 
    # ... (fill in the rest of the map)
]

# Create the Pygame screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simple Pygame Map')

# Load tile images (if you have images)
grass_image = pygame.image.load('assets/mapping/grass.png').convert()
water_image = pygame.image.load('assets/mapping/water.png').convert()
west_coast_asset_image = pygame.image.load("assets/mapping/west_coast.png").convert()
east_coast_asset_image = pygame.image.load("assets/mapping/east_coast.png").convert()
north_coast_asset_image = pygame.image.load("assets/mapping/north_coast.png").convert()
south_coast_asset_image = pygame.image.load("assets/mapping/south_coast.png").convert()

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the map
    for row_index, row in enumerate(tile_map):
        for col_index, tile in enumerate(row):
            if tile == 0:
                # Draw grass
                #pygame.draw.rect(screen, GRASS_COLOR, (col_index * TILE_SIZE, row_index * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                # If you have images, blit the grass image instead
                screen.blit(grass_image, (col_index * TILE_SIZE, row_index * TILE_SIZE))
            elif tile == 1:
                # Draw water
                #pygame.draw.rect(screen, WATER_COLOR, (col_index * TILE_SIZE, row_index * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                # If you have images, blit the water image instead
                screen.blit(water_image, (col_index * TILE_SIZE, row_index * TILE_SIZE))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
