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

ASSETS_PATH = os.path.join("assets")
MAPPING_PATH = os.path.join(ASSETS_PATH, "mapping")
MENU_PATH = os.path.join(ASSETS_PATH, "home_menu")
BUILDING_PATH = os.path.join(ASSETS_PATH, "buildings")
SCIENCE_PATH = os.path.join(ASSETS_PATH, "science")
# Placeholder for building types
building_types = ["House", "Factory", "School", "Steel_Mill", "Town_Hall"]  # Add more as needed
selected_building = None
# Building images 
house_image = pygame.image.load(os.path.join(BUILDING_PATH, "house"))
factory_image =  pygame.image.load(os.path.join(BUILDING_PATH, "factory"))
school_image =  pygame.image.load(os.path.join(BUILDING_PATH, "school"))
steel_mill_image = pygame.image.load(os.path.join(BUILDING_PATH, "steel_mill"))
town_hall_image = pygame.image.load(os.path.join(BUILDING_PATH, "town_hall"))

map_path = os.path.join(MAPPING_PATH, "q_mapping.png")
print(map_path)

# Load the map
map_image = pygame.image.load(map_path)
map_rect = map_image.get_rect()
map_position = [0, 0]  # Initial position
zoom_level = 1.0  # Initial zoom level

# Class for Buildings
class Building: 
    def __init__(self, map_pos):
        self.building_path = os.path.join("assets", "mapping", "east_coast.png") 
        self.original_image = pygame.image.load(self.building_path)
        self.original_pos = map_pos  # Position relative to the map

    def draw(self, surface, map_pos, zoom):
        # Scale building size
        scaled_image = pygame.transform.scale(self.original_image, 
                        (int(self.original_image.get_width() * zoom), 
                         int(self.original_image.get_height() * zoom)))

        # Calculate current position on the screen
        screen_pos = [self.original_pos[0] * zoom + map_pos[0], 
                      self.original_pos[1] * zoom + map_pos[1]]

        surface.blit(scaled_image, screen_pos)

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


            # Click on build icon
            if build_icon.get_rect(topleft=(0, HEIGHT - 50)).collidepoint(mouse_position):
                build_menu_visible = not build_menu_visible 
                if visibility_changes:
                    print(build_menu_visible)
                    # Selecting a building from the menu
                    if build_menu_visible and build_menu_rect.collidepoint(mouse_position):
                        # Determine which building is selected based on mouse position
                        # For now, let's say each building icon is 50x50 and they're laid out horizontally
                        index = (mouse_position[0] // 50) % len(building_types)
                        selected_building = building_types[index]
                        print(index, selected_building)
                        # build_menu_visible = False
                        if selected_building:
                            print(selected_building)
                            # Convert screen position to map position
                            map_click_pos = [(mouse_position[0] - map_position[0]) / zoom_level, 
                                            (mouse_position[1] - map_position[1]) / zoom_level]
                            buildings.append(Building(map_click_pos))                        
        # Zoom controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                zoom_level += 0.1
            elif event.key == pygame.K_MINUS:
                zoom_level = max(0.1, zoom_level - 0.1)




    # Clear screen
    screen.fill((0, 0, 0))


    # Draw build icon
    screen.blit(build_icon, (0, HEIGHT - 50))
    
    # Draw build menu if visible
    if build_menu_visible:
        pygame.draw.rect(screen, (200, 200, 200), build_menu_rect)  # Draw menu background
        # Draw building icons inside the menu
        for i, building in enumerate(building_types):
            color = (0, 255, 0) if True else (128, 128, 128)  # Check condition here
            building_icon = pygame.Surface((50, 50))
            building_icon.fill(color)
            screen.blit(building_icon, (i * 50, HEIGHT - MENU_HEIGHT))


    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()