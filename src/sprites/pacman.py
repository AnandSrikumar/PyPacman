from math import ceil

from pygame import image, transform
from pygame.sprite import Sprite
import pygame.time as pytime

from src.configs import CELL_SIZE, PACMAN_SPEED
from src.sprites.sprite_configs import *
from src.utils.coord_utils import get_coords_from_idx, get_idx_from_coords, get_tiny_matrix


class Pacman(Sprite):
    def __init__(
        self,
        width,
        height,
        game_state,
        pacman_pos,
        start_x,
        start_y,
        matrix,
        screen,
        coord_matrix,
        frame_rate=5,
    ):
        super().__init__()
        x, y = get_coords_from_idx(
            pacman_pos,
            start_x,
            start_y,
            CELL_SIZE[0],
            CELL_SIZE[1],
            len(matrix),
            len(matrix[0]),
        )
        self.screen = screen
        self.load_all_frames(width, height)
        self.frames = self.right_frames
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect_x, self.rect_y = x, y
        self.rect = self.image.get_rect(topleft=(x, y))
        self.frame_rate = frame_rate
        self.counter = 0
        self.game_state = game_state
        self.xidx, self.yidx = pacman_pos
        self.start_x = start_x
        self.start_y = start_y
        self.matrix = matrix
        self.coord_matrix = coord_matrix
        self.tiny_matrix = get_tiny_matrix(self.matrix, CELL_SIZE[0], PACMAN_SPEED)
        self.subdiv = CELL_SIZE[0] // PACMAN_SPEED
        self.tiny_start_x = self.xidx * self.subdiv
        self.tiny_start_y = self.yidx * self.subdiv
        self.move_direction = self.game_state.direction
        self.is_move = True

    def build_bounding_box(self, x, y):
        self.rect.x = x + (CELL_SIZE[0] * 2 - self.rect.width) // 2
        self.rect.y = y + (CELL_SIZE[1] * 2 - self.rect.height) // 2

    def load_all_frames(self, width, height):
        def frame_helper(direction):
            return [
                transform.scale(image.load(path).convert_alpha(), (width, height))
                for path in PACMAN_PATHS[direction]
            ]

        self.left_frames = frame_helper("left")
        self.right_frames = frame_helper("right")
        self.down_frames = frame_helper("down")
        self.up_frames = frame_helper("up")
        self.direction_mapper = {
            "l": self.left_frames,
            "r": self.right_frames,
            "u": self.up_frames,
            "d": self.down_frames,
        }

    def frame_update(self):
        self.counter += 1
        if self.counter >= self.frame_rate:
            self.counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
        self.build_bounding_box(self.rect_x, self.rect_y)

    def frame_direction_update(self):
        direc = self.move_direction
        if direc != "":
            self.frames = self.direction_mapper[direc]

    def edges_helper_vertical(self, row, col, additive):
        for r in range(self.subdiv * 2):
            if self.tiny_matrix[row + r][col + additive] == "wall":
                return False
        return True

    def edge_helper_horizontal(self, row, col, additive):
        for c in range(self.subdiv * 2):
            if self.tiny_matrix[row + additive][col + c] == "wall":
                return False
        return True

    def boundary_check(self):
        bound_x = int(ceil(self.tiny_start_x / PACMAN_SPEED))
        if (self.tiny_start_y + self.subdiv * 2) >= len(self.tiny_matrix[0]) - 1:
            self.tiny_start_y = 0
            self.rect_x = self.coord_matrix[bound_x][0][0]

        elif (self.tiny_start_y - 1) < 0:
            self.tiny_start_y = len(self.tiny_matrix[0]) - (self.subdiv * 3)
            self.rect_x = self.coord_matrix[bound_x][-3][0]

    def movement_bind(self):
        if self.game_state.direction == "l":
            if self.edges_helper_vertical(self.tiny_start_x, self.tiny_start_y, -1):
                self.move_direction = "l"

        elif self.game_state.direction == "r":
            if self.edges_helper_vertical(
                self.tiny_start_x, self.tiny_start_y, self.subdiv * 2
            ):
                self.move_direction = "r"

        elif self.game_state.direction == "u":
            if self.edge_helper_horizontal(self.tiny_start_x, self.tiny_start_y, -1):
                self.move_direction = "u"

        elif self.game_state.direction == "d":
            if self.edge_helper_horizontal(
                self.tiny_start_x, self.tiny_start_y, self.subdiv * 2
            ):
                self.move_direction = "d"

    def move_pacman(self):
        if self.move_direction == "l":
            if self.edges_helper_vertical(self.tiny_start_x, self.tiny_start_y, -1):
                self.rect_x -= PACMAN_SPEED
                self.tiny_start_y -= 1
        elif self.move_direction == "r":
            if self.edges_helper_vertical(
                self.tiny_start_x, self.tiny_start_y, self.subdiv * 2
            ):
                self.rect_x += PACMAN_SPEED
                self.tiny_start_y += 1
        elif self.move_direction == "u":
            if self.edge_helper_horizontal(self.tiny_start_x, self.tiny_start_y, -1):
                self.rect_y -= PACMAN_SPEED
                self.tiny_start_x -= 1
        elif self.move_direction == "d":
            if self.edge_helper_horizontal(
                self.tiny_start_x, self.tiny_start_y, self.subdiv * 2
            ):
                self.rect_y += PACMAN_SPEED
                self.tiny_start_x += 1
        self.game_state.pacman_rect = (self.rect.x, self.rect.y, 
                                       self.rect.width, self.rect.height)

    def eliminate_dots(self):
        r, c = get_idx_from_coords(
            self.rect.x, self.rect.y, self.start_x, self.start_y, CELL_SIZE[0]
        )
        if self.matrix[r][c] == "dot":
            self.matrix[r][c] = "void"
        elif self.matrix[r][c] == 'power':
            self.matrix[r][c] = 'void'
            self.game_state.is_pacman_powered = True

    def update(self):
        self.frame_update()
        self.movement_bind()
        self.boundary_check()
        self.frame_direction_update()
        self.move_pacman()
        self.eliminate_dots()
