import os
# from ui_elements import scale_icon

# Screen dimensions
WIDTH, HEIGHT = 1920, 1080
MENU_HEIGHT = 742
ICON_SIZE = 142  # Assuming square icons for simplicity
ICON_PADDING = 17
RESOURCE_SIZE = 100
RESOURCE_PADDING = 242
TEXT_HEIGHT = 20
BUILD_MENU_ROWS = 2  # Number of rows in build menu
MAXIMUM_FPS = 60
DEVELOPER_OPTION = False
building_selected = False  # Flag to indicate if a building is selected

GRAPHICS_LEVELS = ["low", "medium", "high", "ultra", "extra"]
GRAPHICS_LEVEL = GRAPHICS_LEVELS[0]

# Paths of differents Assets
ASSETS_PATH = os.path.join("assets") 
MAPPING_PATH = os.path.join(ASSETS_PATH, "mapping")
MENU_PATH = os.path.join(ASSETS_PATH, "home_menu")
BUILDING_PATH = os.path.join(ASSETS_PATH, "buildings", GRAPHICS_LEVEL)
ICON_PATH = os.path.join(ASSETS_PATH, "icons")
SCIENCE_PATH = os.path.join(ASSETS_PATH, "science")
RESOURCES_PATH = os.path.join(ASSETS_PATH, "resources")

# Define the color for the shapes (brown with alpha)
SHAPE_COLOR = (139, 69, 19, 177)  # 128 is the alpha value for semi-transparency

# # Define the font for the resource amounts display
# resource_font = pygame.font.SysFont(None, 24)
# # Font for building names
# buildings_font = pygame.font.SysFont(None, 24)

# Default Speeds camera movement
camera_speed = 5 
# Default Speeds of zooming
zoom_speed = 0.01                  
# Maximum zoom
maximum_zoom = 1.7
# Minimum zoom
minimum_zoom = 0.2
# Faster camera
CAMERA_FAST = 7
# Faster zoom
ZOOM_FAST = 0.05

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

 
# # Assuming you have loaded the resource icons somewhere in your code
# resource_icons = {
#     "gold": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "gold.png")).convert_alpha(), "resources_inventory"),
#     "wood": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "wood.png")).convert_alpha(), "resources_inventory"),
#     "stone": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "stone.png")).convert_alpha(), "resources_inventory"),
#     "food": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "food.png")).convert_alpha(), "resources_inventory"),
#     "water": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "water.png")).convert_alpha(), "resources_inventory"),
#     "steel": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "steel.png")).convert_alpha(), "resources_inventory"),
#     "bloom": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "bloom.png")).convert_alpha(), "resources_inventory"),
#     "chromium_bars": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "chromium_bars.png")).convert_alpha(), "resources_inventory"),
#     "wirerod": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "wirerod.png")).convert_alpha(), "resources_inventory"),
#     "laminated_stainless_steel_alloy": scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "laminated_stainless_steel_alloy.png")).convert_alpha(), "resources_inventory")
#     # ... add more resources as needed
# }

# Define the starting amounts for resources, this should be dynamic in playing actual game
resource_amounts = {
    "gold": 2000000,
    "wood": 200000000,
    "stone": 42000,
    "food": 10000,
    "water": 10000,
    "steel": 1000,
    "bloom": 700,
    "chromium_bars": 500,
    "wirerod": 250,
    "laminated_stainless_steel_alloy": 42
    # ... add more resources as needed
}

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

selected_building = None
resources = 10000  # Placeholder for player's resources
 

# Add other constants and configurations here