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
