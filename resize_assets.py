import os
from PIL import Image

from config import *

def resize_images(input_dir, output_dir, target_width, target_height):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir): 
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # Construct full file path
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            # Open and resize the image
            with Image.open(input_path) as image:
                if target_height == "full" or target_width == "full":
                    image.save(output_path)
                else:# Using LANCZOS resampling for high quality
                    image = image.resize((target_width, target_height), Image.LANCZOS)
                    image.save(output_path)



ASSETS_PATH = os.path.join("assets")
BUILDINGS_PATH = os.path.join(ASSETS_PATH, "buildings")
RESOURCES_PATH = os.path.join(ASSETS_PATH, "resources")
ICONS_PATH = os.path.join(ASSETS_PATH, "icons")

# input_folder = os.path.join(BUILDINGS_PATH, "input") # Replace with your input folder path
input_folder = RESOURCES_PATH
for graphic_level in GRAPHICS_LEVELS:
    output_folder = os.path.join(input_folder, graphic_level) # Replace with your output folder path 
    target_width = IMAGES_QUALITY[GRAPHICS_LEVELS.index(graphic_level)]
    target_height = IMAGES_QUALITY[GRAPHICS_LEVELS.index(graphic_level)]
    resize_images(input_folder, output_folder, target_width, target_height)#, target_height
scale = 0.5  # Replace with your desired scale (e.g., 0.5 for half size)
print("Images Scaled")