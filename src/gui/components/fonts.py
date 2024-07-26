from enum import Enum
import pygame

class Fonts(Enum):
    DEFAULT = None
    GUI = "georgia"
    GAME = "verdana"
    INFO = "calibri"

class FontSingleton:
    __instance = None
    def __init__(self):
        raise RuntimeError("FontSingleton class can't be instantiated")
    
    @classmethod
    def get_instance(self):
        if self.__instance is None:
            self.__instance = self.__new__(self)
        return self.__instance
    
    def render_text(self, font_enum, text, color, size):
        # Get the font name from the enum
        font_name = font_enum.value
        
        # Create the font object
        font = pygame.font.SysFont(font_name, size)
        
        # Render the text
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        
        return text_surface, text_rect
    
