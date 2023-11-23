import pygame
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1920, 1080
MENU_HEIGHT = 742

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
maximum_fps = 60
developer_option = False
 

graphics_levels = ["low", "medium", "high", "ultra", "extra"]
graphics_level = graphics_levels[0]

# Paths of differents Assets
ASSETS_PATH = os.path.join("assets") 
MAPPING_PATH = os.path.join(ASSETS_PATH, "mapping")
MENU_PATH = os.path.join(ASSETS_PATH, "home_menu")
BUILDING_PATH = os.path.join(ASSETS_PATH, "buildings", graphics_level)

 

# Paths for the differents building types images
building_types = {
    "House": os.path.join(BUILDING_PATH, "house.png"),
    "Factory": os.path.join(BUILDING_PATH, "factory.png"),
    "School": os.path.join(BUILDING_PATH, "school.png"),
    "Steel_Mill": os.path.join(BUILDING_PATH, "steel_mill.png"),
    "Town_Hall": os.path.join(BUILDING_PATH, "town_hall.png"),
    "1": os.path.join(BUILDING_PATH, "factory_future.png"),
    "2": os.path.join(BUILDING_PATH, "factory.png"),
    "3": os.path.join(BUILDING_PATH, "school.png"),
    "4": os.path.join(BUILDING_PATH, "steel_mill.png"),
    "5": os.path.join(BUILDING_PATH, "town_hall.png"),
    "6": os.path.join(BUILDING_PATH, "house.png"),
    "7": os.path.join(BUILDING_PATH, "factory.png"),
    "8": os.path.join(BUILDING_PATH, "school.png"),
    "9": os.path.join(BUILDING_PATH, "steel_mill.png"),
    "10": os.path.join(BUILDING_PATH, "town_hall.png"),
    "11": os.path.join(BUILDING_PATH, "house.png"),
    "12": os.path.join(BUILDING_PATH, "factory.png"),
    "13": os.path.join(BUILDING_PATH, "school.png"),
    "14": os.path.join(BUILDING_PATH, "steel_mill.png"),
    "15": os.path.join(BUILDING_PATH, "town_hall.png"),
    "16": os.path.join(BUILDING_PATH, "house.png"),
    "17": os.path.join(BUILDING_PATH, "factory.png"),
    "18": os.path.join(BUILDING_PATH, "school.png"),
    "19": os.path.join(BUILDING_PATH, "steel_mill.png"),
    "21": os.path.join(BUILDING_PATH, "town_hall.png"),
    "22": os.path.join(BUILDING_PATH, "house.png"),
    "23": os.path.join(BUILDING_PATH, "factory.png"),
    "24": os.path.join(BUILDING_PATH, "school.png"),
    "25": os.path.join(BUILDING_PATH, "steel_mill.png"),
    "26": os.path.join(BUILDING_PATH, "town_hall.png"),
    "27": os.path.join(BUILDING_PATH, "house.png"),
    "28": os.path.join(BUILDING_PATH, "factory.png"),
    "29": os.path.join(BUILDING_PATH, "school.png"),
    "30": os.path.join(BUILDING_PATH, "steel_mill.png"),
    "31": os.path.join(BUILDING_PATH, "town_hall.png"),
    "32": os.path.join(BUILDING_PATH, "house.png"),
    "33": os.path.join(BUILDING_PATH, "factory.png"),
    "34": os.path.join(BUILDING_PATH, "school.png"),
    "35": os.path.join(BUILDING_PATH, "steel_mill.png"),
    "36": os.path.join(BUILDING_PATH, "town_hall.png"),
    "37": os.path.join(BUILDING_PATH, "house.png"),
    "38": os.path.join(BUILDING_PATH, "factory.png"),
    "39": os.path.join(BUILDING_PATH, "school.png"),
    "40": os.path.join(BUILDING_PATH, "steel_mill.png"),
    "41": os.path.join(BUILDING_PATH, "town_hall.png"),
    "42": os.path.join(BUILDING_PATH, "house.png")
}
 

# Load the map
map_image = pygame.image.load(os.path.join(MAPPING_PATH, "q_mapping.png")).convert()
map_rect = map_image.get_rect()
map_position = [0, 0]  # Initial position
zoom_level = 1.0  # Initial zoom level
 

# Class for Buildings
class Building:
    def __init__(self, image_path, map_pos):
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.original_pos = map_pos  # Center position relative to the map
        self.width = self.original_image.get_width()
        self.height = self.original_image.get_height()

    def draw(self, surface, map_pos, zoom):
        # Scale building size and calculate the new width and height
        scaled_image = pygame.transform.scale(self.original_image,
                        (int(self.width * zoom), int(self.height * zoom)))
        scaled_width = scaled_image.get_width()
        scaled_height = scaled_image.get_height()

        # Calculate current position on the screen with the center at the original position
        screen_pos = [self.original_pos[0] * zoom + map_pos[0] - scaled_width // 2,
                      self.original_pos[1] * zoom + map_pos[1] - scaled_height // 2]

        surface.blit(scaled_image, screen_pos)
        
# List to store buildings
buildings = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if developer_option and event:
            print(event)

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
 

        # Default Speeds camera movement
        camera_speed = 5
        # Default Speeds of zooming
        zoom_speed = 0.01                   
        # Maximum zoom
        maximum_zoom = 1.7
        # Minimum zoom
        minimum_zoom = 0.2
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]: 
            camera_speed = 7 

        # Zoom controls
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_PLUS, pygame.K_EQUALS]:
                zoom_level += zoom_speed
                print(zoom_level)
        elif event.type == pygame.MOUSEWHEEL:
            if event.y == 1 and zoom_level < maximum_zoom:
                zoom_level += zoom_speed
            elif event.y == -1 and zoom_level > minimum_zoom:
                zoom_level -= zoom_speed
                
    # Movement controls
    if keys[pygame.K_LEFT]:
        map_position[0] += camera_speed
    if keys[pygame.K_RIGHT]:
        map_position[0] -= camera_speed
    if keys[pygame.K_UP]:
        map_position[1] += camera_speed
    if keys[pygame.K_DOWN]:
        map_position[1] -= camera_speed

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw the scaled map
    scaled_map = pygame.transform.scale(map_image,
                    (int(map_rect.width * zoom_level),
                     int(map_rect.height * zoom_level)))
    screen.blit(scaled_map, map_position)

    # Draw build icon at its new position
    screen.blit(build_icon, build_icon_rect.topleft)
 
    # Draw buildings
    for building in buildings:
        building.draw(screen, map_position, zoom_level) 
 
    clock.tick(maximum_fps)
    #print(clock.get_fps())
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
