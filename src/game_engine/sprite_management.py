import pygame
from abc import ABC, abstractmethod

class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, images):
        super().__init__()
        self.width = width
        self.height = height
        self.images = [self.load_image(path) for path in images] # List of images for animation
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)  # Create a transparent surface
        self.image.blit(self.images[0], (0, 0))  # Draw the first image on the surface
        self.rect = self.image.get_rect(topleft=pos)
        self.current_frame = 0
        self.animation_speed = 0.05

    def load_image(self, path):
        image = pygame.image.load(path).convert_alpha()
        image = pygame.transform.scale(image, (self.width, self.height))
        return image

    def update(self):
        # Update animation frame
        self.current_frame += self.animation_speed
        if self.current_frame >= len(self.images):
            self.current_frame = 0
        self.image = self.images[int(self.current_frame)]


class PacmanSprite(BaseSprite):
    ...

class GhostSprite(BaseSprite):
    ...
