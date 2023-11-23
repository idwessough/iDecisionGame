import pygame
import os
import ctypes
import pandas as pd

# Function to set DPI Awareness 
def set_dpi_awareness():
    try:
        # Try to use the most recent DPI awareness function
        ctypes.windll.shcore.SetProcessDpiAwareness(2) # 2 = Per Monitor DPI Aware
    except AttributeError:
        # If the above function is not available, use the older one
        ctypes.windll.user32.SetProcessDPIAware()

# DPI Awareness in order to avoid Windows scaling (e.g. "150% recommanded") to break resolution renderer
set_dpi_awareness()

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1920, 1080
MENU_HEIGHT = 742
ICON_SIZE = 142  # Assuming square icons for simplicity
ICON_PADDING = 17
RESOURCE_SIZE = 100
RESOURCE_PADDING = 242
TEXT_HEIGHT = 20
BUILD_MENU_ROWS = 2  # Number of rows in build menu

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
maximum_fps = 60
developer_option = False
building_selected = False  # Flag to indicate if a building is selected

graphics_levels = ["low", "medium", "high", "ultra", "extra"]
graphics_level = graphics_levels[0]

# Paths of differents Assets
ASSETS_PATH = os.path.join("assets") 
MAPPING_PATH = os.path.join(ASSETS_PATH, "mapping")
MENU_PATH = os.path.join(ASSETS_PATH, "home_menu")
BUILDING_PATH = os.path.join(ASSETS_PATH, "buildings", graphics_level)
ICON_PATH = os.path.join(ASSETS_PATH, "icons")
SCIENCE_PATH = os.path.join(ASSETS_PATH, "science")
RESOURCES_PATH = os.path.join(ASSETS_PATH, "resources")

# Define the color for the shapes (brown with alpha)
shape_color = (139, 69, 19, 177)  # 128 is the alpha value for semi-transparency

# Create surfaces for the trapezoid and rectangle with per-pixel alpha
trapezoid_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
rectangle_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

# Define the points for trapezoids shape
upper_trapezoid_points_left = [(0, 0), ((WIDTH / 2) - 77, 0), ((WIDTH / 2) - 242, 77), (0, 77)]  # Replace with your actual points
# Layout resources
upper_trapezoid_points_right = [(WIDTH, 0), ((WIDTH / 2) + 77, 0), ((WIDTH / 2) + 242, 77), (WIDTH, 77)] 

# Draw the shapes on their respective surfaces
pygame.draw.polygon(trapezoid_surface, shape_color, upper_trapezoid_points_left)
pygame.draw.polygon(rectangle_surface, shape_color, upper_trapezoid_points_right)

# Build icon and menu variables
build_icon = pygame.image.load(os.path.join(ICON_PATH, "build_menu.png")).convert_alpha()  # Placeholder for an icon 
# Position the build icon at the top center of the screen
build_icon_rect = build_icon.get_rect()
build_icon_rect.centerx = WIDTH // 2
build_icon_rect.y = 10  # Small margin from the top
build_menu_visible = False
build_menu_rect = pygame.Rect(0, HEIGHT - MENU_HEIGHT, WIDTH, MENU_HEIGHT)
# Calculate the number of icons per row based on the width of the build menu and the size of the icons plus padding
icons_per_row = build_menu_rect.width // (ICON_SIZE + ICON_PADDING)

# Paths for the differents building types images
building_types = {
    "House": os.path.join(BUILDING_PATH, "house.png"),
    "Factory": os.path.join(BUILDING_PATH, "factory.png"),
    "School": os.path.join(BUILDING_PATH, "school.png"),
    "Steel_Mill": os.path.join(BUILDING_PATH, "steel_mill.png"),
    "Town_Hall": os.path.join(BUILDING_PATH, "town_hall.png"),
    "1": os.path.join(BUILDING_PATH, "factory.png"),
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

# Scale images to desired sizes
def scale_icon(image, type):
    if type == "resources_inventory":
        scaled_icon = pygame.transform.scale(image, (77, 77))
    return scaled_icon


# Define two separate dictionaries for left and right side resources 
left_side_resources = {
    "gold": resource_amounts["gold"],
    "wood": resource_amounts["wood"],
    "stone": resource_amounts["stone"],
    "food": resource_amounts["food"],
    "water": resource_amounts["water"]
    # ... other resources to display on the left .. 
}

right_side_resources = {
    "steel": resource_amounts["steel"],
    "bloom": resource_amounts["bloom"],
    "chromium_bars": resource_amounts["chromium_bars"],
    "wirerod": resource_amounts["wirerod"],
    "laminated_stainless_steel_alloy": resource_amounts["laminated_stainless_steel_alloy"]
    # ... other resources to display on the right .. 
}

# Define the font for the resource amounts display
resource_font = pygame.font.SysFont(None, 24)


# Function to draw the resources on the screen
def draw_resources(surface, resources, amounts, font, start_x, start_y, direction, icon_size=42):
    x, y = start_x, start_y
    # Text need to appear in the middle of y axes width of the resource icon
    y_text = icon_size / 2
    padding = 7
    
    for resource, amount in amounts.items():
        # Draw the icon
        icon = resources[resource]
        surface.blit(icon, (x, y))

        # Draw the amount text
        text_surf = font.render(f"{amount}", True, (255, 255, 255))
        text_x = x + icon_size if direction == 'right' else x - text_surf.get_width() 
        surface.blit(text_surf, (text_x, y_text))

        # Update x to the next position
        x = x + icon_size + text_surf.get_width() + padding * 2 if direction == 'right' else x - (icon_size + text_surf.get_width() + padding * 2)


selected_building = None
resources = 10000  # Placeholder for player's resources

# Load the map
map_image = pygame.image.load(os.path.join(MAPPING_PATH, "q_mapping.png")).convert()
map_rect = map_image.get_rect()
map_position = [0, 0]  # Initial position
zoom_level = 1.0  # Initial zoom level

# Font for building names
font = pygame.font.SysFont(None, 24)

# Function to draw the build menu
def draw_build_menu(surface, menu_rect, icons, font):
    surface.fill((200, 200, 200), menu_rect)  # Draw the menu background

    icons_per_row = menu_rect.width // (ICON_SIZE + ICON_PADDING)  # Icons per row
    for i, (name, icon_path) in enumerate(icons.items()):
        row = i // icons_per_row
        col = i % icons_per_row
        x = menu_rect.x + col * (ICON_SIZE + ICON_PADDING) + ICON_PADDING
        y = menu_rect.y + row * (ICON_SIZE + TEXT_HEIGHT + ICON_PADDING) + ICON_PADDING

        # Load and draw the icon
        icon = pygame.image.load(icon_path).convert_alpha()
        icon_rect = pygame.Rect(x, y, ICON_SIZE, ICON_SIZE)
        pygame.draw.rect(surface, (0, 0, 0), icon_rect, 1)  # Draw border
        surface.blit(icon, icon_rect)

        # Draw the building name
        text_surf = font.render(name, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=(x + ICON_SIZE // 2, y + ICON_SIZE + TEXT_HEIGHT // 2))
        surface.blit(text_surf, text_rect)

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

            # Toggle build menu visibility
            if build_icon_rect.collidepoint(event.pos) and not building_selected:
                build_menu_visible = not build_menu_visible
                continue  # Skip the rest of the loop to avoid other interactions

            # Selecting a building from the menu
            if build_menu_visible and build_menu_rect.collidepoint(mouse_position):
                # Calculate the position relative to the build menu
                relative_x = mouse_position[0] - build_menu_rect.x
                relative_y = mouse_position[1] - build_menu_rect.y

                # Calculate the row and column where the click occurred
                col = relative_x // (ICON_SIZE + ICON_PADDING)
                row = relative_y // (ICON_SIZE + ICON_PADDING + TEXT_HEIGHT)

                # Check if the click was inside the bounds of an icon
                icon_left_bound = col * (ICON_SIZE + ICON_PADDING) + ICON_PADDING
                icon_top_bound = row * (ICON_SIZE + ICON_PADDING + TEXT_HEIGHT) + ICON_PADDING
                icon_right_bound = icon_left_bound + ICON_SIZE
                icon_bottom_bound = icon_top_bound + ICON_SIZE

                if icon_left_bound <= relative_x <= icon_right_bound and \
                   icon_top_bound <= relative_y <= icon_bottom_bound:
                    # Calculate the index of the selected building
                    index = row * icons_per_row + col
                    if 0 <= index < len(building_types):
                        selected_building_type, building_path = list(building_types.items())[index]
                        if resources >= 50:  # Placeholder resource check
                            resources -= 50  # Deduct resources
                            selected_building = (selected_building_type, building_path)
                            building_selected = True  # Indicate that a building has been selected
                            build_menu_visible = False  # Optionally hide the menu after selection
                        else:
                            print("Not enough resources to build that one")
                            selected_building = None
                            building_selected = False

            # Place building after selection
            elif building_selected:
                if pygame.mouse.get_pressed()[0]:  # Left mouse click
                    mouse_position = pygame.mouse.get_pos()
                    
                    # Get the building type and image path
                    building_type, building_path = selected_building
                    
                    # Create a temporary Building object to get the width and height
                    temp_building = Building(building_path, (0, 0))
                    
                    # Calculate the center position to place the building
                    # We adjust by half the width and height of the scaled building image
                    center_x = (mouse_position[0] - map_position[0]) / zoom_level
                    center_y = (mouse_position[1] - map_position[1]) / zoom_level
                    map_click_pos = (
                        center_x - (temp_building.width / 11) * zoom_level,
                        center_y - (temp_building.height / 11) * zoom_level
                    )
                    
                    # Add the new building to the list of buildings
                    buildings.append(Building(building_path, map_click_pos))
                    selected_building = None
                    building_selected = False  # Reset the building selected flag

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
    
    # Blit the surfaces onto the main screen
    screen.blit(trapezoid_surface, (0,0))
    screen.blit(rectangle_surface, (0,0))
    
    # Draw left side resources
    draw_resources(screen, resource_icons, left_side_resources, resource_font, 10, 10, "right", 77)
    
    # Draw right side resources
    right_start_x = WIDTH - 10  # Start from the right edge of the screen
    #for amount in right_side_resources.values():
    #    right_start_x -= (resource_font.size(str(amount))[0] + ICON_SIZE + RESOURCE_PADDING * 2)  # Adjust starting X position based on the width of the resources
    
    draw_resources(screen, resource_icons, right_side_resources, resource_font, right_start_x, 10, "left", 77)
    
    # Draw buildings
    for building in buildings:
        building.draw(screen, map_position, zoom_level) 

    # Draw build menu if visible
    if build_menu_visible:
        draw_build_menu(screen, build_menu_rect, building_types, font)
    
    clock.tick(maximum_fps)
    #print(clock.get_fps())
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
