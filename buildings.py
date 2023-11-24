import pygame
from config import *


class BuildingManager:
    def __init__(self, image_path, map_position):
        # Initialize buildings here
        self.buildings = []
        self.original_image = pygame.image.load(image_path)
        print(image_path) 
        self.width = self.original_image.get_width()
        self.height = self.original_image.get_height()
        self.original_pos = map_position


    def update(surface, map_position, zoom_level, buildings):#: list = []
        # if not buildings:
        #     buildings = []
        # Update buildings here
        for building in buildings:
            building.draw(surface, map_position, zoom_level)

    def draw(self, surface, map_position, zoom):
        # Scale building size and calculate the new width and height
        
        scaled_image = pygame.transform.scale(self.original_image,
                        (int(self.width * zoom), int(self.height * zoom)))
        scaled_width = scaled_image.get_width()
        scaled_height = scaled_image.get_height()

        # Calculate current position on the screen with the center at the original position
        screen_pos = [self.original_pos[0] * zoom + map_position[0] - scaled_width // 2,
                      self.original_pos[1] * zoom + map_position[1] - scaled_height // 2]
        print("draw", scaled_image, screen_pos)
        surface.blit(scaled_image, screen_pos)
    # Additional methods for building management can be added here
