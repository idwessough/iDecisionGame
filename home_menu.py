import pygame
import sys
import os
import webbrowser
import screeninfo

# Retrieve all screens connected to the system
monitors = screeninfo.get_monitors()

# Check if there is more than one screen
if len(monitors) > 1:
    print("Multiple screens detected. Using resolution of Screen 1")

# Loop through each screen and print its width and height
for i, monitor in enumerate(monitors):
    first_screen = True
    if first_screen:
        SCREEN_WIDTH = monitor.width
        SCREEN_HEIGHT = monitor.height
    print(f"Screen {i+1}: Width = {monitor.width}, Height = {monitor.height}")
    first_screen = False

# Initialize Pygame
pygame.init()

# Constants for screen dimensions


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

def start_game():
    import main  # Import main.py here to start the game

# Define the action for the source code button
def open_link():
    webbrowser.open('http://github.com/idwessough/iDecisionGame') #Resource Harvest

# Define the action for the settings button
def open_settings():
    # Placeholder for settings functionality
    # Here you can draw a new screen or overlay with settings options
    settings_screen()
    
def set_fullscreen():
    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #, pygame.FULLSCREEN not working as expected
    print("Setting Fullscreen")
    
def set_windowed():
    global screen
    print("Setting Windowed")
    screen = pygame.display.set_mode((SCREEN_WIDTH - (0.2 * SCREEN_WIDTH), SCREEN_HEIGHT - (0.2 * SCREEN_HEIGHT)), pygame.RESIZABLE)
    
# Function to handle the settings screen
def settings_screen():
    running = True
    # Create buttons for windowed and full-screen modes
    windowed_button = Button('Windowed Mode', 200, 40, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2), 5, action=set_windowed) 
    fullscreen_button = Button('Full Screen', 200, 40, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50), 5, action=set_fullscreen)
    # Background of the Settings 
    background_settings = pygame.image.load(os.path.join("assets", "settings_menu", "Settings_Menu_Background_Game_Image.png") )
    background_settings = pygame.transform.scale(background_settings, (SCREEN_WIDTH, SCREEN_HEIGHT))


    while running:
        
        screen.blit(background_settings, (0, 0))

        # Draw buttons
        windowed_button.draw()
        fullscreen_button.draw()

        # Event handling for the settings screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            # Update buttons based on mouse position and click
            mouse_pos = pygame.mouse.get_pos()
            for button in [windowed_button, fullscreen_button]:
                button.top_rect.collidepoint(mouse_pos)
                button.check_click()

        # Update the display
        pygame.display.update()

        

# Main menu loop
def main_menu():
    # play_button = Button('Play Game', 200, 40, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2), 5)
    play_button = Button('Play Game', 200, 40, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2), 5, action=start_game)  # Assign start_game function to the Play Game button
    settings_button = Button('Settings', 200, 40, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50), 5)
    source_button = Button('Source Code', 200, 40, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100), 5)
    exit_button = Button('Exit', 200, 40, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 150), 5)
    background_image = pygame.image.load(os.path.join("assets", "home_menu", "Main_Menu_Background_Game_Image.png") )
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    while True:
        # Draw the background image
        
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
            
        # Update the display
        pygame.display.update()

# Run the main menu
main_menu()
