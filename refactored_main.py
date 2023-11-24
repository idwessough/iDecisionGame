
# main.py
import pygame
from resource_manager import ResourceManager
from buildings import BuildingManager
from ui_elements import UIManager
from config import *
import ctypes

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

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# Create surfaces for the trapezoid and rectangle with per-pixel alpha
trapezoid_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
rectangle_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
# To Move to UI_elements ?

# Build icon and menu variables
build_icon = pygame.image.load(os.path.join(ICON_PATH, "build_menu.png")).convert_alpha()  # Placeholder for an icon 
# Position the build icon at the top center of the screen
build_icon_rect = build_icon.get_rect()
build_icon_rect.centerx = WIDTH // 2
build_icon_rect.y = 10  # Small margin from the top
build_menu_visible = False
build_menu_rect = pygame.Rect(0, HEIGHT - MENU_HEIGHT, WIDTH, MENU_HEIGHT)


if __name__ == "__main__":

    ui_manager = UIManager(screen) 
    resource_manager = ResourceManager()
    #building_manager = BuildingManager()
    # Calculate the number of icons per row based on the width of the build menu and the size of the icons plus padding
    icons_per_row = build_menu_rect.width // (ICON_SIZE + ICON_PADDING)

    map_position = [0, 0]  # Initial position
    zoom_level = 1.0  # Initial zoom level
    buildings = []
    building_selected = False
    selected_building = None
    running = True 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]: 
                    camera_speed = CAMERA_FAST 
                    zoom_speed = ZOOM_FAST                
                map_position = ui_manager.handle_keyboard_event(keys)

            elif event.type == pygame.MOUSEWHEEL:
                zoom_level = ui_manager.handle_mousewheel_event(event.y, zoom_level, zoom_speed)                

            elif event.type == pygame.MOUSEBUTTONDOWN:
                #buildings, selected_building = ui_manager.handle_mouse_event(event, map_position, zoom_level, selected_building)
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
                        temp_building = BuildingManager(building_path, (0, 0))
                        
                        # Calculate the center position to place the building
                        # We adjust by half the width and height of the scaled building image
                        center_x = (mouse_position[0] - map_position[0]) / zoom_level
                        center_y = (mouse_position[1] - map_position[1]) / zoom_level
                        map_click_pos = (
                            center_x - (temp_building.width / 11) * zoom_level,
                            center_y - (temp_building.height / 11) * zoom_level
                        )
                        
                        # Add the new building to the list of buildings
                        buildings.append(BuildingManager(building_path, map_click_pos))
                        selected_building = None
                        building_selected = False  # Reset the building selected flag
                        
        screen.fill((0, 0, 0))
        #resource_manager.update()
        #screen = 
        
        #BuildingManager.update(screen, map_position, zoom_level, buildings)
        #
        
        for building in buildings:
            building.draw(screen, map_position, zoom_level)
        ui_manager.update(map_position, zoom_level, build_menu_visible)

        # ui_manager.draw_resources(screen, resource_icons, left_side_resources, resource_font, 10, 10, "right", 77) for instance prefere calling draw_resources() method from UI Manager class

        # Update the display
        pygame.display.flip()
        
        clock.tick(MAXIMUM_FPS)

    pygame.quit()
 
 