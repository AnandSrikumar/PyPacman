from src.game_state.screen_state import GameScreen
from src.game_state.state_variables import State
from src.gui.screens.main_menu import MainMenu
from src.gui.screens.high_scores import HighScores
from src.logger import Logger

import pygame

class ScreenFactory:
    def __init__(self, state: State,
                 screen: pygame.Surface):
        self.state = state
        self.screen = screen
        self.objects_repo = {}
        self.logger = Logger.get_instance()

    def render(self, screen_state, screen_cls):
        render_obj = self.objects_repo.get(screen_state, 
                                           screen_cls(self.state, 
                                                      self.screen))
        self.objects_repo[screen_state] = render_obj
        render_obj.render_screen()

    def render_screen(self):
        if self.state.game_screen == GameScreen.MAIN_MENU:
            self.render(GameScreen.MAIN_MENU, MainMenu)
    
        elif self.state.game_screen == GameScreen.HIGHSCORES:
            self.render(GameScreen.HIGHSCORES, HighScores)

