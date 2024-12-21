import json

from src.configs import *
from src.sprites.ghosts import GhostManager
from src.sprites.pacman import Pacman
from src.utils.coord_utils import (get_coords_from_idx, place_elements_offset,
                                   precompute_matrix_coords)
from src.utils.draw_utils import (draw_circle, draw_debug_rects, draw_rect)
from src.log_handle import get_logger
logger = get_logger(__name__)

class PacmanGrid:
    def __init__(self, screen, game_state):
        logger.info("initializing pacman grid")
        self.function_mapper = {
            "void": self.draw_void,
            "wall": self.draw_wall,
            "dot": self.draw_dot,
            "spoint": self.draw_special_point,
            "power": self.draw_power,
            "null": self.draw_void,
            "elec": self.draw_elec,
        }
        self._screen = screen
        self._game_state = game_state
        self._level_number = self._game_state.level
        self.load_level(self._level_number)
        logger.info("level loaded")
        self.load_sprites()
        
    def load_sprites(self):
        self.pacman = Pacman(
            PACMAN[0],
            PACMAN[1],
            self._game_state,
            self._pacman_pos,
            self.start_x,
            self.start_y,
            self._matrix,
            self._screen,
            self._coord_matrix,
        )
        logger.info("pacman created")
        self.ghost = GhostManager(self.ghost_den,
                                  self.start_x, self.start_y,
                                  self._matrix,
                                  self.elec_pos,
                                  self._game_state,
                                  self._screen)
        logger.info("ghosts created")

    def check_reload_level(self):
        if self._game_state.is_pacman_dead:
            self.load_sprites()
            self._game_state.is_pacman_dead = False

    def get_json(self, path):
        with open(path) as fp:
            payload = json.load(fp)
        return payload

    def load_level(self, level_number):
        level_path = f"levels/level{level_number}.json"
        level_json = self.get_json(level_path)
        num_rows = level_json["num_rows"]
        num_cols = level_json["num_cols"]
        self.ghost_den = level_json['ghost_den']
        self._matrix = level_json["matrix"]
        self._pacman_pos = level_json["pacman_start"]
        self.elec_pos = level_json['elec']
        self.start_x, self.start_y = place_elements_offset(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            CELL_SIZE[0] * num_cols,
            CELL_SIZE[0] * num_rows,
            0.15,
            0.5,
        )
        self._coord_matrix = precompute_matrix_coords(
            self.start_x, self.start_y, CELL_SIZE[0], num_rows, num_cols
        )
        self.num_rows = num_rows
        self.num_cols = num_cols

    def draw_void(self, **kwargs): ...

    def draw_wall(self, **kwargs):
        draw_rect(
            kwargs["x"],
            kwargs["y"],
            kwargs["w"],
            kwargs["h"],
            self._screen,
            Colors.WALL,
        )

    def draw_dot(self, **kwargs):
        dot_x = kwargs["x"] + kwargs["w"]
        dot_y = kwargs["y"] + kwargs["h"]
        draw_rect(dot_x, dot_y, 5, 5, self._screen, Colors.WHITE)

    def draw_special_point(self): ...

    def draw_power(self, **kwargs):
        circle_x = kwargs["x"] + kwargs["w"]
        circle_y = kwargs["y"] + kwargs["h"]
        draw_circle(circle_x, circle_y, 7, self._screen, Colors.YELLOW)

    def draw_elec(self, **kwargs):
        draw_rect(kwargs["x"], kwargs["y"], kwargs["w"], 1, self._screen, Colors.RED)

    def draw_level(self):
        curr_x, curr_y = self.start_x, self.start_y
        for _, row in enumerate(self._matrix):
            for _, col in enumerate(row):
                draw_func = self.function_mapper[col]
                draw_func(x=curr_x, y=curr_y, w=CELL_SIZE[0], h=CELL_SIZE[0])
                curr_x += CELL_SIZE[0]
            curr_x = self.start_x
            curr_y += CELL_SIZE[0]

    def draw_outliners(self):
        draw_debug_rects(
            self.start_x, self.start_y, 128, 140, 5, Colors.GREEN, self._screen
        )
        draw_debug_rects(
            self.start_x,
            self.start_y,
            self.num_rows,
            self.num_cols,
            CELL_SIZE[0],
            Colors.BLUE,
            self._screen,
        )
