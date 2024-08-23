from src.game_state.screen_state import GameScreen
from src.game_state.state_variables import State
from src.gui.screens.main_menu import MainMenu
from src.gui.screens.high_scores import HighScores
from src.gui.screens.pacman_game import Pacman

from src.logger import Logger

import pygame

class ScreenFactory:
    def __init__(self, state: State,
                 screen: pygame.Surface):
        self.state = state
        self.screen = screen
        self.objects_repo = {}
        self.logger = Logger.get_instance()
        self.screen_mapper = {GameScreen.GAME:Pacman,
                         GameScreen.MAIN_MENU: MainMenu,
                         GameScreen.HIGHSCORES: HighScores}

    def render(self, screen_state, screen_cls):
        render_obj = self.objects_repo.get(screen_state, 
                                           screen_cls(self.state, 
                                                      self.screen))
        self.objects_repo[screen_state] = render_obj
        render_obj.render_screen()

    def render_screen(self):
        self.render(self.state.game_screen, 
                    self.screen_mapper[self.state.game_screen])

