import pygame
import sys
import os
import webbrowser

# Initialize Pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("iDecision: Harvest Resources - Home Menu")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

# Define fonts
font = pygame.font.Font(None, 36)

# Menu options
menu_items = ['Play Game', 'Settings', 'Source Code', 'Exit']

# Function to draw text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Define your resources
class Inventory:
    def __init__(self):
        self.food = 0
        self.wood = 0
        self.iron = 0
        self.gold = 0

    def add_resource(self, resource, amount):
        if resource == 'food':
            self.food += amount
        elif resource == 'wood':
            self.wood += amount
        elif resource == 'iron':
            self.iron += amount
        elif resource == 'gold':
            self.gold += amount

    # ... Add more methods as needed for resource management

# Define a collector building
class CollectorBuilding:
    def __init__(self, resource_type, gathering_rate):
        self.resource_type = resource_type
        self.gathering_rate = gathering_rate
        self.timer = 0

    def update(self, delta_time, inventory):
        # Add resources to the inventory based on the gathering rate
        self.timer += delta_time
        if self.timer >= self.gathering_rate:
            inventory.add_resource(self.resource_type, 1)
            self.timer = 0  # Reset the timer

# ... Add more game logic, classes and methods as needed




class Button:
    def __init__(self, text, width, height, pos, elevation, action = None):
        
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        self.action = action

        # Top rectangle 
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#475F77'

        # Text
        self.text_surf = font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

        # Bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(width,height))
        self.bottom_color = '#354B5E'
        # Original method for button drawing
        self.draw()

    def draw(self):
        # Elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius = 11)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius = 11)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        #pygame.time.wait(200)
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                if not self.pressed:
                    self.pressed = True
                    if self.action:  # If the button has an action assigned, call it
                        self.action()
            else:
                self.dynamic_elevation = self.elevation
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77'
            if self.pressed:
                self.pressed = False

# Define the action for the exit button
def quit_game():
    pygame.quit()
    sys.exit()
    
# Define the action for the source code button
def open_link():
    webbrowser.open('http://github.com/idwessough/iDecisionGame') #Resource Harvest


# Main menu loop
def main_menu():
    play_button = Button('Play Game', 200, 40, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2), 5)
    settings_button = Button('Settings', 200, 40, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50), 5)
    source_button = Button('Source Code', 200, 40, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100), 5)
    exit_button = Button('Exit', 200, 40, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 150), 5)
    background_image = pygame.image.load(os.path.join("assets", "home_menu", "Main_Menu_Background_Game_Image.png") )
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    inventory = Inventory()
    wood_collector = CollectorBuilding('wood', 5)  # Gather wood every 5 seconds
    
    while True:
        # Draw the background image
        print(screen)
        screen.blit(background_image, (0, 0)) 
        exit_button = Button('Exit', 200, 40, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 150), 5, action=quit_game)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Create a button for source code with the action to open the hyperlink
        source_button = Button('Source Code', 200, 40, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100), 5, action=open_link)

        # Create a button for settings with the action to open the settings menu
        settings_button = Button('Settings', 200, 40, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50), 5, action=open_settings)

        # Draw buttons
        for button in [play_button, settings_button, source_button, exit_button]:
            button.draw()
                    
        # In your game loop, update the collector
        delta_time = 1  # This would actually be the time since the last update
        wood_collector.update(delta_time, inventory)
        print(inventory.wood)
        # Update the display
        pygame.display.update()

# Run the main menu
main_menu()
