import pygame
import sys

# Initialize Pygame
pygame.init()

# # Set up the screen (1080p)
# screen_width, screen_height = 1920, 1080
# screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the screen (720p)
screen_width, screen_height = 1080, 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Camera properties
camera_x, camera_y = 0, 0
zoom_level = 1.0
# Default Speeds camera movement
camera_speed = 1
# Default Speeds of zooming
zoom_speed = 1.001

# Map properties (example with colored rectangles)
map_elements = [
    {"color": (0, 125, 0), "rect": pygame.Rect(1, 1, 300, 300)},
    {"color": (255, 0, 0), "rect": pygame.Rect(-100, 100, 400, 300)},
    {"color": (0, 255, 0), "rect": pygame.Rect(-600, 400, 300, 300)},
    {"color": (125, 0, 0), "rect": pygame.Rect(42, 42, 300, 300)},
    # Add more elements as needed
]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    print(camera_speed, zoom_speed)
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

    # Draw the map elements
    for element in map_elements:
        zoomed_rect = pygame.Rect(
            (element["rect"].left - camera_x) * zoom_level,
            (element["rect"].top - camera_y) * zoom_level,
            element["rect"].width * zoom_level,
            element["rect"].height * zoom_level
        )
        pygame.draw.rect(screen, element["color"], zoomed_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
