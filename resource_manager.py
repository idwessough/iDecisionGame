import pygame
from config import *

class ResourceManager:
    def __init__(self):
        self.loaded_images = {}

    def load_image(self, path):
        if path not in self.loaded_images:
            self.loaded_images[path] = pygame.image.load(path).convert_alpha()
        return self.loaded_images[path]
    
    def update(self):
        # Update resources here
        print("update")

    # Add methods for other resources like fonts, sounds, etc.
    