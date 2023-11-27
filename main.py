import pygame
import os
import ctypes
import pandas as pd
import time

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
boundary_width = 10
GRAPHICS_LEVELS = ["low", "medium", "high", "ultra", "raw_extra"]
graphics_level = GRAPHICS_LEVELS[0]
# Define boundary zones as pygame.Rect objects
left_boundary = pygame.Rect(0, 0, boundary_width, HEIGHT)
right_boundary = pygame.Rect(WIDTH - boundary_width, 0, boundary_width, HEIGHT)
top_boundary = pygame.Rect(0, 0, WIDTH, boundary_width)
bottom_boundary = pygame.Rect(0, HEIGHT - boundary_width, WIDTH, boundary_width)

# Paths of differents Assets
ASSETS_PATH = os.path.join("assets") 
MAPPING_PATH = os.path.join(ASSETS_PATH, "mapping")
MENU_PATH = os.path.join(ASSETS_PATH, "home_menu")
BUILDING_PATH = os.path.join(ASSETS_PATH, "buildings")# , graphics_level
ICON_PATH = os.path.join(ASSETS_PATH, "icons")
SCIENCE_PATH = os.path.join(ASSETS_PATH, "science")
RESOURCES_PATH = os.path.join(ASSETS_PATH, "resources")
DEPOSITS_PATH = os.path.join(ASSETS_PATH, "deposits")

# Define the color for the shapes (brown with alpha)
shape_color = (139, 69, 19, 177)  # 128 is the alpha value for semi-transparency

# Create surfaces for the trapezoid and rectangle with per-pixel alpha
trapezoid_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
rectangle_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

# Define the points for trapezoids shape Layout resources
upper_trapezoid_points_left = [(0, 0), ((WIDTH / 2) - 77, 0), ((WIDTH / 2) - 242, 77), (0, 77)] 
upper_trapezoid_points_right = [(WIDTH, 0), ((WIDTH / 2) + 77, 0), ((WIDTH / 2) + 242, 77), (WIDTH, 77)] 
lower_trapezoid_points_left = [(0, HEIGHT), (0, HEIGHT - 77), ((WIDTH / 2) - 242, HEIGHT - 77), ((WIDTH / 2) - 77, HEIGHT)]
lower_trapezoid_points_right = [(WIDTH, HEIGHT), (WIDTH, HEIGHT - 77), ((WIDTH / 2) + 242, HEIGHT - 77), ((WIDTH / 2) + 77, HEIGHT)]

# Draw the shapes on their respective surfaces
pygame.draw.polygon(trapezoid_surface, shape_color, upper_trapezoid_points_left)
pygame.draw.polygon(rectangle_surface, shape_color, upper_trapezoid_points_right)
# Draw the lower trapezoids on their respective surfaces
pygame.draw.polygon(trapezoid_surface, shape_color, lower_trapezoid_points_left)
pygame.draw.polygon(rectangle_surface, shape_color, lower_trapezoid_points_right)

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
BUILDINGS_DATA_FILE_PATH = os.path.join("buildings_data.csv") 
SEPARATOR= ";"
# Paths for the differents building types images
df_buildings = pd.read_csv(BUILDINGS_DATA_FILE_PATH, sep=SEPARATOR)
buildings_data = df_buildings
# print(buildings_data["icon_path"])

TIME_INTERVAL = 1

deposits_types = {
    "coal_deposit": os.path.join(DEPOSITS_PATH, "coal_deposit.png"),
    "steel_deposit": os.path.join(DEPOSITS_PATH, "steel_deposit.png")
}
# Scale images to desired sizes
def scale_icon(image, type):
    if type == "resources_inventory":
        scaled_icon = pygame.transform.scale(image, (77, 77))
    return scaled_icon


# Assuming you have loaded the resource icons somewhere in your code
resource_icons = {
    "water": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "water.png")).convert_alpha(), "resources_inventory"),
    "food": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "food.png")).convert_alpha(), "resources_inventory"),
    "wood": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "wood.png")).convert_alpha(), "resources_inventory"),
    "gold": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "gold.png")).convert_alpha(), "resources_inventory"),
    "energy":scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "energy.png")).convert_alpha(), "resources_inventory"),
    "stone": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "stone.png")).convert_alpha(), "resources_inventory"),
    "concrete": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "concrete.png")).convert_alpha(), "resources_inventory"),
    "heavy_duty_reinforced_concrete":scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "heavy_duty_reinforced_concrete.png")).convert_alpha(), "resources_inventory"), 
    "sand":scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "sand_perfect.png")).convert_alpha(), "resources_inventory"),
    "glass":scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "glass.png")).convert_alpha(), "resources_inventory"),
    "coal":scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "coal.png")).convert_alpha(), "resources_inventory"),
    "uranium":scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "uranium.png")).convert_alpha(), "resources_inventory"),
    "U235_Combustible_fully_enriched":scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "U235_Combustible_fully_enriched.png")).convert_alpha(), "resources_inventory"),
    "steel": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "steel.png")).convert_alpha(), "resources_inventory"),
    "stainless_steel_long_product_bloom": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "stainless_steel_long_product_bloom.png")).convert_alpha(), "resources_inventory"),
    "chromium_bars": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "chromium_bars.png")).convert_alpha(), "resources_inventory"),
    "laminated_stainless_steel_alloy": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "laminated_stainless_steel_alloy.png")).convert_alpha(), "resources_inventory"),
    "HSS_Structural_hollow_steel_section": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "HSS_Structural_hollow_steel_section.png")).convert_alpha(), "resources_inventory"),
    "wirerod": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "wirerod.png")).convert_alpha(), "resources_inventory")
    # ... add more resources as needed
}

LEFT_SIDE_START_X = - 42 
RIGHT_SIDE_START_X = (WIDTH // 2) + 177 

# Define two separate dictionaries for left and right side resources 
up_left_side_resources = [
    "water",
    "food",
    "wood",
    "gold",
    "energy"
    ]

up_right_side_resources = [
    "sand",
    "stone",
    "coal",
    "uranium",
    "steel" 
    ] 

down_left_side_resources = [
    "glass",
    "concrete",
    "heavy_duty_reinforced_concrete",
    "U235_Combustible_fully_enriched" 
    ]

down_right_side_resources = [ 
    "stainless_steel_long_product_bloom",
    "chromium_bars",
    "laminated_stainless_steel_alloy",
    "HSS_Structural_hollow_steel_section",
    "wirerod"
    ]
    
    
    # ... other resources to display on the right ..
    
# Define the font for the resource amounts display
resource_font = pygame.font.SysFont(None, 24)


def draw_resources(surface, resources_icon, resources, font, start_x, start_y, location, side, icon_size=42, padding=42, little_padding=17):
    # Calculate the total width available for each resource
    total_resources = len(resources)
    space_per_resource = ((WIDTH // 2) - (242 + 42))  // total_resources

    # Initialize the x-coordinate for resource placement 
    x = start_x
    
    for resource_type in resources:
        # Draw the icon
        icon = resources_icon[resource_type]
        icon_x = x + (space_per_resource - icon_size) // 2  # Center the icon in its allocated space
        surface.blit(icon, (icon_x, start_y))

        # Draw the amount text right after the icon
        text_surf = font.render(f"{resource_manager.get_resource_amount(resource_type)}", True, (255, 255, 255)) 
        text_x = icon_x + icon_size + padding  # Position the text after the icon with a padding
        text_y = (start_y + icon_size // 2) # (start_y + icon_size + (icon_size - text_surf.get_height())) // 2  # Vertically align the text with the icon 
        surface.blit(text_surf, (text_x, text_y))

        # Update x to the next position
        x += space_per_resource + little_padding

    # Ensure that the last resource does not go beyond the screen width
    if x + icon_size > WIDTH:
        x = WIDTH - icon_size
        
selected_building = None
resources = 10000  # Placeholder for player's resources

# Load the map
map_image = pygame.image.load(os.path.join(MAPPING_PATH, graphics_level, "mapping.png")).convert() 
map_rect = map_image.get_rect()
map_position = [0, 0]  # Initial position
zoom_level = 1.0  # Initial zoom level

# Font for building names
font = pygame.font.SysFont(None, 24)

# Function to draw the build menu
def draw_build_menu(surface, menu_rect, icons, font):
    surface.fill((200, 200, 200), menu_rect)  # Draw the menu background

    icons_per_row = menu_rect.width // (ICON_SIZE + ICON_PADDING)  # Icons per row
    for i, icon_path in enumerate(buildings_data["icon_path"]) : # (name, icon_path)
    #for i, (name, icon_path, gathering_rate) in buildings_data.iterrows(): 
        icon_path = os.path.join(BUILDING_PATH, GRAPHICS_LEVELS[0], icon_path) 
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
        name = buildings_data.loc[i, "name"]
        text_surf = font.render(name, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=(x + ICON_SIZE // 2, y + ICON_SIZE + TEXT_HEIGHT // 2))
        surface.blit(text_surf, text_rect)

# Class for Buildings
class Building:
    def __init__(self, image_path, building_name, gathering_rate, building_cost, map_pos):
        self.original_image = pygame.image.load(os.path.join(BUILDING_PATH, graphics_level, image_path)).convert_alpha()
        self.original_pos = map_pos  # Center position relative to the map
        self.width = self.original_image.get_width()
        self.height = self.original_image.get_height()
        self.name = building_name
        self.building_cost = building_cost
        # self.name = name
        self.gathering_rate = gathering_rate  # dict, e.g., {"wood": 5, "steel": 10}

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
        
class ResourceManager:
    def __init__(self):
        self.resources = {
            "water": 10000, 
            "food": 10000,
            "wood": 200000002,
            "gold": 2000000,
            "energy": 42424242,
            "stone": 42000,
            "concrete": 42,
            "steel": 1000,
            "coal": 10,
            "bloom": 700 
            # ... add more resources as needed
        }
        self.last_update = time.time() 
    
    def update_resources(self, current_time, buildings):
        if current_time - self.last_update >= TIME_INTERVAL:
            # Update resources
            self.last_update = current_time 
            # Rest of your update logic
            for building in buildings:
                print(eval(building.gathering_rate)) 
                for resource, rate in eval(building.gathering_rate).items():
                    self.resources[resource] += rate

    def buying(self, cost):
        print(cost)
        for resource_type, cost_amount in eval(cost).items():
            self.resources[resource_type] -= cost_amount

    def get_resource_amount(self, resource):
        return self.resources.get(resource, 0)


# List to store buildings
buildings = []
# ResourceManager instance
resource_manager = ResourceManager()
# Main game loop
running = True
while running:
    current_time = time.time()
    for event in pygame.event.get():
        # Get the current mouse position
        mouse_position = pygame.mouse.get_pos()
        if developer_option and event:
            print(event)

        if event.type == pygame.QUIT:
            running = False
    
        elif event.type == pygame.MOUSEBUTTONDOWN: 
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
                    if 0 <= index < len(buildings_data):
                        selected_building_type, building_path, gathering_rate, cost = list(buildings_data.iloc[index,:]) 
                        
                        if resources >= 50:  # Placeholder resource check
                            resources -= 50  # Deduct resources
                            selected_building = (selected_building_type, building_path, gathering_rate)
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
                    
                    # Get the building type and image path + gathering rate
                    building_type, building_path, gathering_rate = selected_building
                    
                    # Create a temporary Building object to get the width and height
                    temp_building = Building(building_path, building_type, 0, 0, (0, 0))
                    
                    # Calculate the center position to place the building
                    # We adjust by half the width and height of the scaled building image
                    center_x = (mouse_position[0] - map_position[0]) / zoom_level
                    center_y = (mouse_position[1] - map_position[1]) / zoom_level
                    map_click_pos = (
                        center_x - (temp_building.width / 11) * zoom_level,
                        center_y - (temp_building.height / 11) * zoom_level
                    )
                    
                    # Add the new building to the list of buildings
                    buildings.append(Building(building_path, building_type, gathering_rate, cost, map_click_pos))
                    resource_manager.buying(buildings[-1].building_cost)
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
            camera_speed = 17 

        # Zoom controls
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_PLUS, pygame.K_EQUALS]:
                zoom_level += zoom_speed
            elif event.key in [pygame.K_MINUS]:
                zoom_level -= zoom_speed
        elif event.type == pygame.MOUSEWHEEL:
            if event.y == 1 and zoom_level < maximum_zoom:
                zoom_level += zoom_speed
            elif event.y == -1 and zoom_level > minimum_zoom:
                zoom_level -= zoom_speed
                
    # Movement controls Check for screen boundaries and update map position based on mouse positionn
    if left_boundary.collidepoint(mouse_position):
        map_position[0] += camera_speed
    elif right_boundary.collidepoint(mouse_position):
        map_position[0] -= camera_speed
    if top_boundary.collidepoint(mouse_position):
        map_position[1] += camera_speed
    elif bottom_boundary.collidepoint(mouse_position):
        map_position[1] -= camera_speed
    # Arrow controls mapping movements    
    if keys[pygame.K_LEFT]:
        map_position[0] += camera_speed
    if keys[pygame.K_RIGHT]:
        map_position[0] -= camera_speed
    if keys[pygame.K_UP]:
        map_position[1] += camera_speed
    if keys[pygame.K_DOWN]:
        map_position[1] -= camera_speed

    # Updating resources
    resource_manager.update_resources(current_time, buildings) 
    
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
    
    # Draw upper left side resources
    draw_resources(screen, resource_icons, up_left_side_resources, resource_font, LEFT_SIDE_START_X, 10, "up", "left") 
    # Draw upper right side resources
    draw_resources(screen, resource_icons, up_right_side_resources, resource_font, RIGHT_SIDE_START_X, 10, "up", "right") 
    # Draw resources in the lower left corner
    draw_resources(screen, resource_icons, down_left_side_resources, resource_font, LEFT_SIDE_START_X, 1000, "down", "left")
    # Draw resources in the lower right corner 
    draw_resources(screen, resource_icons, down_right_side_resources, resource_font, RIGHT_SIDE_START_X, 1000, "down", "right")
    
    
    # Draw buildings
    for building in buildings:
        building.draw(screen, map_position, zoom_level) 

    # Draw build menu if visible
    if build_menu_visible: 
        draw_build_menu(screen, build_menu_rect, buildings_data["icon_path"], font)
    fps = clock.get_fps()
    # Render FPS
    fps_text = font.render(f"FPS: {int(fps)}", True, (255, 255, 255))
    text_rect = fps_text.get_rect()
    screen.blit(fps_text, (WIDTH - text_rect.width - 10, HEIGHT - text_rect.height - 10))

    clock.tick(120)
    #print()
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
