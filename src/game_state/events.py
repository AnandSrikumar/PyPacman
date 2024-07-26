import pygame
from src.game_state.state_variables import State
from src.game_state.screen_state import GameScreen

class EventHandler:
    def __init__(self, state: State):
        self.state: State = state

    def key_press_release_check(self):
        ...

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.state.running = False
                
                if event.key == pygame.K_p:
                    self.state.game_screen = GameScreen.HIGHSCORES

                if event.key == pygame.K_o:
                    self.state.game_screen = GameScreen.MAIN_MENU
                
                if event.key == pygame.K_UP:
                    self.state.up_pressed = True
                
                if event.key == pygame.K_DOWN:
                    self.state.down_pressed = True
                
                if event.key == pygame.K_RETURN:
                    self.state.enter = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.state.up_pressed = False
                
                if event.key == pygame.K_DOWN:
                    self.state.down_pressed = False

                if event.key == pygame.K_RETURN:
                    self.state.enter = False