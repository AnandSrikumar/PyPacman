from .screen_dimension_calculator import ScreenDimensionCalculator
from .level_loader import LevelLoader

class LevelManager:
    def __init__(self, level_number, 
                screen_width, 
                screen_height,
                ):
        
        self.level_number = level_number
        self.screen_calculator = ScreenDimensionCalculator(screen_width, screen_height)
        self.level_loader = LevelLoader(level_number)
        self.screen_rect = self.screen_calculator.calculate_screen_rect()
        self.cell_size = self.screen_calculator.calculate_cell_size(self.screen_rect)
        self.level_data = self.level_loader.load_level()

    def get_screen_rect(self):
        """Return the calculated screen rectangle."""
        return self.screen_rect

    def get_level_data(self):
        """Return the loaded level data."""
        return self.level_data
    
    def modify_level_data(self, row, col, new_val):
        self.level_data['matrix'][row][col] = new_val
    
    def get_cell_size(self):
        return self.cell_size
    
    def get_pacman_start_pos(self, cell_width, cell_height,
                             screen_x, screen_y):
        pacman_pos = self.level_data['pacman_start_pos']
        return self.screen_calculator.get_pacman_start_coords(cell_width,
                                                              cell_height,
                                                              screen_x,
                                                              screen_y,
                                                              pacman_pos[0],
                                                              pacman_pos[1])
