import pygame
from src.game_state.screen_state import GameScreen
from src.game_state.state_variables import State
from src.gui.components.buttons import ButtonBuilder, ButtonDirector
from src.gui.components.fonts import Fonts, FontSingleton
from src.configs.colors import Colors
from src.gui.components.tables import TableBuilder, TableDirector

class HighScores:
    def __init__(self, state: State, screen: pygame.Surface):
        self.state = state
        self.screen = screen
        self.screen_size = self.screen.get_size()
        self.object_map = {}

    def render_text(self):
        # Create text surface
        text = "HighScores"
        font_name = Fonts.GUI
        font, font_rect = FontSingleton.get_instance().\
                        render_text(font_name, text, Colors.WHITE.value, 54)
        font_rect.center = (int(self.screen_size[0] *0.49) , int(self.screen_size[1] * 0.15) )
        self.screen.blit(font, font_rect)

    def render_table(self):
        table = self.object_map.get("table")
        if table:
            table.render_table()
            return
        x_start = int(self.screen_size[0]*0.36)
        y_start = int(self.screen_size[1]*0.24)
        builder = TableBuilder(self.screen)
        director = TableDirector(builder, x=x_start, y=y_start,
                                 cell_dims=(90, 60),
                                 content_list=[[1, "anand",500],
                                               [2, 'anand2',450],
                                               [3,'anand3',400],
                                               [4,'anand4',380],
                                               [5,'anand5',150]],
                                 font_size=24)
        table = director.create_high_score_table()
        table.render_table()
        self.object_map['table'] = table

    def _callback(self):
        self.state.game_screen = GameScreen.MAIN_MENU

    def inspect_selection(self, button):
        mouse_pos = pygame.mouse.get_pos()
        self.mouse_pos = mouse_pos
        self.mouse_pressed = pygame.mouse.get_pressed()
        if button.rect.collidepoint(mouse_pos):
            button.selected = True

    def render_back_button(self):
        button = self.object_map.get('button')
        if not button:
            x = int(self.screen_size[0] * 0.30)
            y = int(self.screen_size[1] * 0.60)
            button_width = int(self.screen_size[0] * 0.20)
            button_height = int(self.screen_size[1] * 0.07)
            builder = ButtonBuilder(self.screen)
            director = ButtonDirector(builder, 
                                    pygame.Rect(x,
                                                y,
                                                button_width,
                                                button_height),
                                                24,
                                                "BACK")
            button = director.create_gui_borderless_button()
            self.object_map['button'] = button
        self.inspect_selection(button)
        button.hover_check()
        button.render_button()
        button.render_text_in_button()
        if button.is_clicked(self.mouse_pos,
                             self.mouse_pressed[0],
                             self.state.enter):
            self._callback()
            print("button clicked in highscores")
            button.selected = False

    def render_screen(self):
        self.render_text()
        self.render_table()
        self.render_back_button()
