import pygame
from src.game_state.state_variables import State
from src.gui.components.fonts import Fonts, FontSingleton
from src.configs.colors import Colors

class HighScores:
    def __init__(self, state: State, screen: pygame.Surface):
        self.state = state
        self.screen = screen
        self.screen_size = self.screen.get_size()

    def render_text(self):
        # Create text surface
        text = "HighScores"
        font_name = Fonts.GUI
        font, font_rect = FontSingleton.get_instance().\
                        render_text(font_name, text, Colors.WHITE.value, 74)
        font_rect.center = (self.screen_size[0] // 2, self.screen_size[1] // 2)
        self.screen.blit(font, font_rect)

    def render_screen(self):
        self.render_text()
