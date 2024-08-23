import pygame

class ScreenDimensionCalculator:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def calculate_screen_rect(self):
        """Calculate the screen rectangle that is 85% of the screen size and centered."""
        width = int(self.screen_width * 0.80)
        height = int(self.screen_height * 0.80)
        x = (self.screen_width - width) // 2
        y = (self.screen_height - height) // 2
        return pygame.Rect(x, y, width, height)

    def calculate_cell_size(self, screen_rect):
        """Calculate the size of each cell based on the number of rows and columns."""
        cell_width = screen_rect.width // 28
        cell_height = screen_rect.height // 31
        print(cell_width, cell_height,'are cell dims')
        return cell_width, cell_height
    
    def get_pacman_start_coords(self, cell_width, 
                                cell_height, screen_x, 
                                screen_y, x_pos, y_pos):
        x = screen_x + (cell_width * x_pos)
        y = screen_y + (cell_height * y_pos)
        return x, y