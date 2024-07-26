import pygame
from src.game_state.state_variables import State
from src.game_state.events import EventHandler
from src.gui.screens.screen_factory import ScreenFactory
from src.logger import Logger

# Initialize Pygame
class Game:
    def __init__(self):
        self.state = State()
        self.events = EventHandler(self.state)
        self.logger = Logger.get_instance()

    def load_pygame_screen(self):
        pygame.init()
        self.logger.log("*"*15+"RUN"+"*"*15)
        self.logger.log("Initiated the screen")
        self.info = pygame.display.Info()
        self.screen_width, self.screen_height = self.info.current_w, self.info.current_h
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
        self.screen_factory = ScreenFactory(self.state, self.screen)
    
    def game_loop(self):
        while self.state.running:
            self.events.handle_events()
            self.screen.fill((0, 0, 0))
            self.screen_factory.render_screen()
            pygame.display.flip()

    def run_game(self):
        self.load_pygame_screen()
        self.game_loop()