import pygame
from config import *

from buildings import BuildingManager 

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        # Initialize other button properties

    def draw(self, window):
        # Draw button
        pygame.draw.rect(window, (255, 0, 0), self.rect)
        # Render and draw text

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    # Additional methods as needed
    
    
class UIManager:
    def __init__(self, screen):
        self.screen = screen
        # Initialize UI elements here 
        # Define the color for the shapes (brown with alpha)
        self.shape_color = (139, 69, 19, 177)  # 128 is the alpha value for semi-transparency

        # Create surfaces for the trapezoid and rectangle with per-pixel alpha
        self.trapezoid_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.rectangle_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

        # Define the points for trapezoids shape
        self.upper_trapezoid_points_left = [(0, 0), ((WIDTH / 2) - 77, 0), ((WIDTH / 2) - 242, 77), (0, 77)]  # Replace with your actual points
        # Layout resources
        self.upper_trapezoid_points_right = [(WIDTH, 0), ((WIDTH / 2) + 77, 0), ((WIDTH / 2) + 242, 77), (WIDTH, 77)] 

        # Draw the shapes on their respective surfaces
        pygame.draw.polygon(self.trapezoid_surface, self.shape_color, self.upper_trapezoid_points_left)
        pygame.draw.polygon(self.rectangle_surface, self.shape_color, self.upper_trapezoid_points_right) 

        # Build icon and menu variables
        self.build_icon = pygame.image.load(os.path.join(ICON_PATH, "build_menu.png")).convert_alpha()  # Placeholder for an icon 
        # Position the build icon at the top center of the screen
        self.build_icon_rect = self.build_icon.get_rect()
        self.build_icon_rect.centerx = WIDTH // 2
        self.build_icon_rect.y = 10  # Small margin from the top
        # self.build_menu_visible = False
        self.build_menu_rect = pygame.Rect(0, HEIGHT - MENU_HEIGHT, WIDTH, MENU_HEIGHT)
        # Calculate the number of icons per row based on the width of the build menu and the size of the icons plus padding
        self.icons_per_row = self.build_menu_rect.width // (ICON_SIZE + ICON_PADDING)
        self.buildings = []
        self.building_selected = False
        # Load the map
        self.map_image = pygame.image.load(os.path.join(MAPPING_PATH, "q_mapping.png")).convert()
        self.map_rect = self.map_image.get_rect()
 

        # Define the font for the resource amounts display
        self.resource_font = pygame.font.SysFont(None, 24)
        # Font for building names
        self.buildings_font = pygame.font.SysFont(None, 24)

        self.resources = 10000
        # Assuming you have loaded the resource icons somewhere in your code
        self.resource_icons = {
        "gold": self.scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "gold.png")).convert_alpha(), "resources_inventory"),
        "wood": self.scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "wood.png")).convert_alpha(), "resources_inventory"),
        "stone": self.scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "stone.png")).convert_alpha(), "resources_inventory"),
        "food": self.scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "food.png")).convert_alpha(), "resources_inventory"),
        "water": self.scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "water.png")).convert_alpha(), "resources_inventory"),
        "steel": self.scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "steel.png")).convert_alpha(), "resources_inventory"),
        "bloom": self.scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "bloom.png")).convert_alpha(), "resources_inventory"),
        "chromium_bars": self.scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "chromium_bars.png")).convert_alpha(), "resources_inventory"),
        "wirerod": self.scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "wirerod.png")).convert_alpha(), "resources_inventory"),
        "laminated_stainless_steel_alloy": self.scale_icon(pygame.image.load(os.path.join(RESOURCES_PATH, "laminated_stainless_steel_alloy.png")).convert_alpha(), "resources_inventory")
        # ... add more resources as needed
        }
        # Paths for the differents building types images
        self.building_types = {
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
    def scale_icon(self, image, type):
        if type == "resources_inventory":
            scaled_icon = pygame.transform.scale(image, (77, 77))
        return scaled_icon

    # def handle_mouse_event(self, event, map_position, zoom_level, selected_building):
        
    #     # Handle mouse events
    #     print("mouse handling")
    #     mouse_position = event.pos

    #     # Toggle build menu visibility
    #     if self.build_icon_rect.collidepoint(event.pos) and not self.building_selected:
    #         self.build_menu_visible = not self.build_menu_visible
    #         # continue  # Skip the rest of the loop to avoid other interactions

    #     # Selecting a building from the menu
    #     if self.build_menu_visible and self.build_menu_rect.collidepoint(mouse_position):
    #         # Calculate the position relative to the build menu
    #         relative_x = mouse_position[0] - self.build_menu_rect.x
    #         relative_y = mouse_position[1] - self.build_menu_rect.y

    #         # Calculate the row and column where the click occurred
    #         col = relative_x // (ICON_SIZE + ICON_PADDING)
    #         row = relative_y // (ICON_SIZE + ICON_PADDING + TEXT_HEIGHT)

    #         # Check if the click was inside the bounds of an icon
    #         icon_left_bound = col * (ICON_SIZE + ICON_PADDING) + ICON_PADDING
    #         icon_top_bound = row * (ICON_SIZE + ICON_PADDING + TEXT_HEIGHT) + ICON_PADDING
    #         icon_right_bound = icon_left_bound + ICON_SIZE
    #         icon_bottom_bound = icon_top_bound + ICON_SIZE

    #         if icon_left_bound <= relative_x <= icon_right_bound and \
    #            icon_top_bound <= relative_y <= icon_bottom_bound:
    #             # Calculate the index of the selected building
    #             index = row * self.icons_per_row + col
    #             if 0 <= index < len(self.building_types):
    #                 selected_building_type, building_path = list(self.building_types.items())[index]
    #                 if self.resources >= 50:  # Placeholder resource check
    #                     self.resources -= 50  # Deduct resources
    #                     selected_building = (selected_building_type, building_path) 
    #                     self.building_selected = True  # Indicate that a building has been selected
    #                     self.build_menu_visible = False  # Optionally hide the menu after selection
    #                 else:
    #                     print("Not enough resources to build that one")
    #                     selected_building = "" 
    #                     self.building_selected = False

    #     # Place building after selection
    #     elif self.building_selected:
    #         if pygame.mouse.get_pressed()[0]:  # Left mouse click
    #             mouse_position = pygame.mouse.get_pos()
                
    #             # Get the building type and image path
    #             building_type, building_path = selected_building
                
    #             # Create a temporary Building object to get the width and height
    #             temp_building = BuildingManager(building_path, (0, 0))
                
    #             # Calculate the center position to place the building
    #             # We adjust by half the width and height of the scaled building image
    #             center_x = (mouse_position[0] - map_position[0]) / zoom_level
    #             center_y = (mouse_position[1] - map_position[1]) / zoom_level
    #             map_click_pos = (
    #                 center_x - (temp_building.width / 11) * zoom_level,
    #                 center_y - (temp_building.height / 11) * zoom_level
    #             )
                
    #             # Add the new building to the list of buildings
    #             self.buildings.append(BuildingManager(building_path, map_click_pos))
    #             selected_building = ""
    #             self.building_selected = False  # Reset the building selected flag
    #             return self.buildings, selected_building

    def handle_keyboard_event(self, keys, map_position):
        # Handle keyboard events
        # print("keyboard handling")
        #             if event.key in [pygame.K_PLUS, pygame.K_EQUALS]:
        #         zoom_level += zoom_speed
        #         print(zoom_level)
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]: 
            camera_speed = CAMERA_FAST 
            zoom_speed = ZOOM_FAST
            
        # Movement controls
        if keys[pygame.K_LEFT]:
            map_position[0] += camera_speed
        if keys[pygame.K_RIGHT]:
            map_position[0] -= camera_speed
        if keys[pygame.K_UP]:
            map_position[1] += camera_speed
        if keys[pygame.K_DOWN]:
            map_position[1] -= camera_speed

        return map_position, zoom_speed
    
    def handle_mousewheel_event(self, y_event, zoom_level, zoom_speed):
        if y_event == 1 and zoom_level < maximum_zoom:
            zoom_level += zoom_speed
        elif y_event == -1 and zoom_level > minimum_zoom:
            zoom_level -= zoom_speed

        return zoom_level

    def update(self, map_position, zoom_level, build_menu_visible): 
        # Clear self.screen
        self.screen.fill((0, 0, 0)) 
        # Blit the surfaces onto the main self.screen
        self.screen.blit(self.trapezoid_surface, (0,0))
        self.screen.blit(self.rectangle_surface, (0,0))

        # Draw the scaled map
        scaled_map = pygame.transform.scale(self.map_image,
                    (int(self.map_rect.width * zoom_level),
                    int(self.map_rect.height * zoom_level)))
        self.screen.blit(scaled_map, map_position)

        # Draw build icon at its new position
        self.screen.blit(self.build_icon, self.build_icon_rect.topleft) 
        # Draw left side resources
        self.draw_resources(self.screen, self.resource_icons, left_side_resources, self.resource_font, 10, 10, "right")#, 77
        
        # # Draw right side resources
        # right_start_x = WIDTH - 10  # Start from the right edge of the self.screen
        # #for amount in right_side_resources.values():
        # #    right_start_x -= (resource_font.size(str(amount))[0] + ICON_SIZE + RESOURCE_PADDING * 2)  # Adjust starting X position based on the width of the resources
        
        # draw_resources(self.screen, resource_icons, right_side_resources, resource_font, right_start_x, 10, "left", 77)
        
        # Draw buildings
        for building in self.buildings:
            building.draw(self.screen, map_position, zoom_level) 

        # Draw build menu if visible
        if build_menu_visible:
            self.draw_build_menu(self.screen, self.build_menu_rect, self.building_types, self.buildings_font)
        
    # Function to draw the build menu

    def draw_build_menu(self, surface, menu_rect, icons, font):
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

    # Function to draw the resources on the screen
    def draw_resources(self, surface, resources, amounts, font, start_x, start_y, direction, icon_size=42): 
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

# # Scale images to desired sizes
# def scale_icon(image, type):
#     if type == "resources_inventory":
#         scaled_icon = pygame.transform.scale(image, (77, 77))
#     return scaled_icon
