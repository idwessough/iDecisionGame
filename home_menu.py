import pygame
import sys
import os
import pandas as pd
import numpy as np

# Initialize Pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('RTS Game Menu')

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

 

# Define the action for the exit button
def quit_game():
    pygame.quit()
    sys.exit()

# Main menu loop
def main_menu():
    play_button = Button('Play Game', 200, 40, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2), 5)
    settings_button = Button('Settings', 200, 40, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50), 5)
    source_button = Button('Source Code', 200, 40, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100), 5)
    exit_button = Button('Exit', 200, 40, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 150), 5)
    background_image = pygame.image.load(os.path.join("resources", "Main_Menu_Background_Game_Image.png") )
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

        # Draw buttons
        for button in [play_button, settings_button, source_button, exit_button]:
            button.draw()

        # Update the display
        pygame.display.update()

# Run the main menu
main_menu()
