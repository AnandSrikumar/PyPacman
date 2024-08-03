import pygame
from src.gui.components.fonts import Fonts, FontSingleton
from src.configs.colors import Colors

class Button:
    def __init__(self, 
                 rect=None,
                 line_width=None,
                 text=None,
                 text_xy=None,
                 font=None,
                 font_size=None,
                 text_color=None,
                 line_color=None,
                 hover_color=None,
                 callback=None,
                 screen = None):
        self.rect = rect
        self.line_width = line_width
        self.text = text
        self.text_xy = text_xy
        self.font = font
        self.font_size = font_size
        self.text_color = text_color
        self.line_color = line_color
        self.hover_color = hover_color
        self.callback = callback
        self.screen = screen
        self.__selected = False

    def render_button(self):
        pygame.draw.rect(self.screen, 
                         self.line_color, 
                         self.rect,
                         self.line_width)
        # print("button drawn", self.line_color, self.rect)
    def _calculate_text_coords(self, font_rect):
        # Get button dimensions
        button_width, button_height = self.rect.width, self.rect.height
        
        # Get text dimensions from font_rect
        text_width, text_height = font_rect.width, font_rect.height
        
        # Calculate position to center the text within the button
        x = self.rect.x + (button_width - text_width) // 2
        y = self.rect.y + (button_height - text_height) // 2
        
        return x, y

    def render_text_in_button(self):
        font_obj, font_rect = FontSingleton.get_instance().\
                        render_text(self.font, 
                                    self.text, 
                                    self.text_color, 
                                    self.font_size)
        font_x, font_y = self._calculate_text_coords(font_rect)
        font_rect.topleft = (font_x, font_y)
        # Render the text on the button
        self.screen.blit(font_obj, font_rect)

    def hover_check(self):
        if self.selected:
            self.text_color = Colors.PINK.value
        else:
            self.text_color = Colors.WHITE.value

    def is_clicked(self, mouse_pos, mouse_left_clicked, enter_clicked):
        if self.rect.collidepoint(mouse_pos) and mouse_left_clicked:
            return True
        
        if mouse_left_clicked and self.selected:
            return True
        
        if enter_clicked and self.selected:
            return True
        
        return False

    @property
    def selected(self):
        return self.__selected
    
    @selected.setter
    def selected(self, val):
        self.__selected = val


class ButtonBuilder:
    def __init__(self, screen):
        self.screen = screen
        self.button = Button(screen=self.screen)  # Initialize Button with the screen

    def set_rect(self, rect):
        self.button.rect = rect
        return self
    
    def set_line_width(self, line_width):
        self.button.line_width = line_width
        return self
    
    def set_line_color(self, line_color):
        self.button.line_color = line_color
        return self
    
    def set_text(self, text):
        self.button.text = text
        return self
    
    def set_text_xy(self, text_xy):
        self.button.text_xy = text_xy
        return self
    
    def set_font(self, font):
        self.button.font = font
        return self
    
    def set_font_size(self, font_size):
        self.button.font_size = font_size
        return self
    
    def set_text_color(self, text_color):
        self.button.text_color = text_color
        return self
    
    def set_image(self, image):
        self.button.image = image
        return self
    
    def set_image_coords(self, image_coords):
        self.button.image_coords = image_coords
        return self
    
    def set_hover_color(self, hover_color):
        self.button.hover_color = hover_color
        return self
    
    def set_callback(self, callback):
        self.button.callback = callback
        return self
    
    def build(self):
        return self.button


class ButtonDirector:
    def __init__(self, builder, rect, font_size, text):
        self.builder = builder
        self.rect = rect
        self.font_size = font_size
        self.text = text
    
    def create_gui_borderless_button(self):
        button = (self.builder
                  .set_rect(self.rect)
                  .set_line_width(-1)  # Borderless button
                  .set_line_color(Colors.WHITE.value)  # White line color
                  .set_text(self.text)
                  .set_text_color(Colors.WHITE.value)  # White text color
                  .set_hover_color(Colors.PINK.value)  # Pink hover color
                  .set_font(Fonts.GUI)
                  .set_font_size(self.font_size)
                  .set_callback(None)  # No callback for this example
                  .build())
        return button
    
    def create_gui_filled_button(self):
        button = (self.builder
                  .set_rect(self.rect)
                  .set_line_width(0)  # Borderless button
                  .set_line_color(Colors.WHITE.value)  # White line color
                  .set_text(self.text)
                  .set_text_color(Colors.BLACK.value)  # White text color
                  .set_hover_color(Colors.PINK.value)  # Pink hover color
                  .set_font(Fonts.GUI)
                  .set_font_size(self.font_size)
                  .set_callback(None)  # No callback for this example
                  .build())
        return button