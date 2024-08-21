import sys

import pygame

from src.game_engine.level_manager import LevelManager
from src.game_engine.sprite_management import PacmanSprite

from src.game_state.state_variables import State
from src.configs.colors import Colors
from src.gui.components.game_component import Dot, Wall
from src.configs.component_config import component_mapper
from src.configs.sprite_lists import *

class Pacman:
    def __init__(self, state: State, screen):
        self.state = state
        self.screen = screen
        self.level_manager = None
        self.pacman = None

    def preload_screen(self):
        if not self.level_manager:
            level = self.state.level
            screen_width = self.screen.get_width()
            screen_height = self.screen.get_height()
            self.level_manager = LevelManager(level, screen_width, 
                                              screen_height)
            self.preload_matrix_objects()
            self.preload_pacman()
    
    def preload_matrix_objects(self):
        matrix = self.level_manager.get_level_data()['matrix']
        cell_dims = self.level_manager.get_cell_size()
        # print(cell_dims[0], cell_dims[1],'..')
        screen_dims = self.level_manager.get_screen_rect()
        x, y, w, h = screen_dims
        for idx, row in enumerate(matrix):
            x = screen_dims[0]
            for idx2, col in enumerate(row):
                if col != 0:
                    obj = component_mapper[col]((x, y), 
                                                (cell_dims[0], cell_dims[1]))
                    # print(f"Creating object {component_mapper[col]} at ({idx}, {idx2}) with id: {id(obj)}")
                    self.level_manager.modify_level_data(idx, idx2, obj)
                x += cell_dims[0]
            y += cell_dims[1]

    def preload_pacman(self):
        pacman_list = PACMAN
        screen_dims = self.level_manager.get_screen_rect()
        screen_x, screen_y = screen_dims[0], screen_dims[1]
        width, height = self.level_manager.get_cell_size()
        start_pos = self.level_manager.get_pacman_start_pos(width, 
                                                            height,
                                                            screen_x,
                                                            screen_y)
        self.pacman = PacmanSprite(pos=start_pos, 
                                   width=height*2, 
                                   height=height*2,
                                   images=pacman_list)
        print(f"pacman drawn at {start_pos} with width: {width}, height: {height}")
        print(f"actual screen dims {screen_dims}")

    def draw_matrix(self):
        matrix = self.level_manager.get_level_data()['matrix']
        for idx, row in enumerate(matrix):
            for idx2, col in enumerate(row):
                if col != 0:
                    col.render(self.screen)

    def draw_matrix(self):
        matrix = self.level_manager.get_level_data()['matrix']
        cell_dims = self.level_manager.get_cell_size()
        screen_dims = self.level_manager.get_screen_rect()
        x, y, w, h = screen_dims
        for idx, row in enumerate(matrix):
            x = screen_dims[0]
            for idx2, col in enumerate(row):
                if col != 0:
                    col.render(self.screen)
                pygame.draw.rect(self.screen,
                                 (255, 0, 0),
                                 (x, y, cell_dims[0], cell_dims[1]),
                                 1)
                x += cell_dims[0]
            y += cell_dims[1]

    def sprites_blitter(self):
        self.pacman.update()
        self.screen.blit(self.pacman.image, self.pacman.rect)
        pygame.display.flip()

    def render_screen(self):
        self.preload_screen()
        self.draw_matrix()
        self.sprites_blitter()
        