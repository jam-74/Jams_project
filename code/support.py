from os import walk
import pygame

def import_folder(path):
    surface_list = []

    for _, _, img_files in walk(path):
        for image in img_files:
            full_path = path + "/" + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            # Calculate the scaling factors for width and height
            width_scale = 1/7
            height_scale = 1/7
            # Scale the image surface to the new size
            new_width = int(image_surf.get_width() * width_scale)
            new_height = int(image_surf.get_height() * height_scale)
            image_surf = pygame.transform.scale(image_surf, (new_width, new_height))
            surface_list.append(image_surf)

        

    return surface_list


