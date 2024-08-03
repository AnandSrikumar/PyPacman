import pygame
from src.gui.components.fonts import Fonts, FontSingleton
from src.configs.colors import Colors

class Table:
    def __init__(self,
                 rows=None,
                 cols=None,
                 cell_dims:tuple = None, #width and height of cell
                 x=None,
                 y=None,
                 content_list=None,
                 font=None,
                 font_size=None,
                 font_color=None,
                 table_border_color=None,
                 content_offset=None,
                 screen=None,
                 line_width=None):
        self.rows = rows
        self.cols = cols
        self.cell_dims = cell_dims
        self.x = x
        self.y = y
        self.content_list = content_list
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.table_border_color = table_border_color
        self.content_offset = content_offset
        self.screen = screen
        self.line_width = line_width

    def get_fonts(self, text):
        font_obj, font_rect = FontSingleton.get_instance().\
                        render_text(self.font, 
                                    text, 
                                    self.font_color, 
                                    self.font_size)
        return font_obj, font_rect
        
    def render_table(self):
        if self.cell_dims is None or self.screen is None:
            return
        
        # cell_width, cell_height = self.cell_dims
        start_x = self.x
        start_y = self.y

        for row in range(self.rows):
            current_x = start_x
            for col in range(self.cols):
                # Define the cell rectangle
                cell_width, cell_height = self.cell_dims.get(col)
                cell_rect = pygame.Rect(current_x, start_y, cell_width, cell_height)
                
                # Draw the cell border (if needed)
                if self.table_border_color:
                    pygame.draw.rect(self.screen, self.table_border_color, cell_rect, self.line_width)
                
                if self.content_list and row < len(self.content_list) and \
                      col < len(self.content_list[0]):
                    text = self.content_list[row][col]
                    font_obj, font_rect = self.get_fonts(str(text))
                    font_rect.topleft = (cell_rect.x+int(cell_rect.x * 0.05),
                                         cell_rect.y + cell_rect.height//2)
                    self.screen.blit(font_obj, font_rect)
                
                # Move to the next column
                current_x += cell_width

            # Move to the next row
            start_y += cell_height
            # Reset x position for the next row
            start_x = self.x


class TableBuilder:
    def __init__(self, screen):
        self.screen = screen
        self.table = Table(screen=self.screen)

    def set_rows(self, rows):
        self.table.rows = rows
        return self

    def set_cols(self, cols):
        self.table.cols = cols
        return self

    def set_cell_dims(self, cell_dims):
        self.table.cell_dims = cell_dims
        return self

    def set_x(self, x):
        self.table.x = x
        return self

    def set_y(self, y):
        self.table.y = y
        return self

    def set_content_list(self, content_list):
        self.table.content_list = content_list
        return self

    def set_font(self, font):
        self.table.font = font
        return self

    def set_font_size(self, font_size):
        self.table.font_size = font_size
        return self

    def set_font_color(self, font_color):
        self.table.font_color = font_color
        return self

    def set_table_border_color(self, table_border_color):
        self.table.table_border_color = table_border_color
        return self

    def set_content_offset(self, content_offset):
        self.table.content_offset = content_offset
        return self
    
    def set_line_width(self, line_width):
        self.table.line_width = line_width
        return self

    def build(self):
        return self.table

    
class TableDirector:
    def __init__(self, builder, x, y,  
                 content_list,
                 font_size,
                 rows=5,
                 cols=3,
                 cell_dims=None):
        self.builder = builder
        self.cell_dims=cell_dims
        self.x = x
        self.y = y
        self.content_list = content_list
        self.font_size = font_size
        self.rows = rows
        self.cols = cols

    def create_high_score_table(self):
        fixed_height = self.cell_dims[1]
        variable_widths = {0:(40, fixed_height), 
                           1:(220, fixed_height), 2:(160, fixed_height)}
        table = (self.builder.set_rows(self.rows)
              .set_cols(self.cols)
              .set_cell_dims(variable_widths)
              .set_x(self.x)
              .set_y(self.y)
              .set_content_list(self.content_list)
              .set_font(Fonts.INFO)  # Replace with actual font
              .set_font_size(self.font_size)
              .set_font_color(Colors.WHITE.value)  # White color
              .set_table_border_color(Colors.PINK.value)  # Black border
              .set_content_offset(5)
              .set_line_width(-1)
              .build())
        return table