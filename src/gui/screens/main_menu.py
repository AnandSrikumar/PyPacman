from src.game_state.state_variables import State
from src.gui.components.fonts import Fonts
from src.gui.components.buttons import ButtonBuilder, ButtonDirector
from src.game_state.screen_state import GameScreen
import sys

import pygame

class MainMenu:
    def __init__(self, state: State, 
                 screen: pygame.Surface):
        self.state = state
        self.screen = screen
        self.title_image_path = "pacman-art/title/pacman_title.png"
        self.screen_width, self.screen_height = self.screen.get_size()
        self.button_width = int(self.screen_width * 0.16) 
        self.button_height = int(self.screen_height * 0.04)
        self.button_x = (self.screen_width - self.button_width) // 2
        self.button_map = {}
        self.buttons_list = []
        self.selected_button = 0

    def render_title(self):
        image = pygame.image.load(self.title_image_path)
        image_width = int(self.screen_width * 0.8)
        image_height = int(self.screen_height * 0.45)
        image = pygame.transform.scale(image, (image_width, image_height))
        x = (self.screen_width - image_width) // 2
        y = 10
        self.screen.blit(image, (x, y))

    def render_items(self,name, y_offset, idx, callback=None):
        button = self.button_map.get(name)
        if not button:
            y = int(self.screen_height * y_offset)
            builder = ButtonBuilder(self.screen)
            director = ButtonDirector(builder, 
                                    pygame.Rect(self.button_x,
                                                y,
                                                self.button_width,
                                                self.button_height),
                                                24,
                                                name)
            button = director.create_gui_borderless_button()
            self.button_map[name] = button
            self.buttons_list.append(button)

        mouse_pos = pygame.mouse.get_pos()
        self.mouse_pos = mouse_pos
        self.mouse_pressed = pygame.mouse.get_pressed()
        if button.rect.collidepoint(mouse_pos):
            self.selected_button = idx
        button.hover_check()
        button.render_button()
        button.render_text_in_button()
        self.button_click_check(button, callback)
        return button
    
    def button_click_check(self, button, callback):
        if button.is_clicked(self.mouse_pos,
                             self.mouse_pressed[0],
                             self.state.enter):
            if callback:
                callback()

    def render_start(self):
        button = self.render_items("START", 0.48, 0)
    
    def render_highscores(self):
        def callback_highscore():
            self.state.game_screen = GameScreen.HIGHSCORES

        button = self.render_items('HIGHSCORES', 0.53, 1, callback_highscore)

    def render_about(self):
        button = self.render_items('ABOUT', 0.58, 2)
        
    def render_options(self):
        button = self.render_items('OPTIONS', 0.63, 3)
    
    def render_exit(self):
        def callback():
            sys.exit()
        button = self.render_items('EXIT', 0.68, 4, callback)
    
    def hover_selected(self):
        for b in self.buttons_list:
            b.selected = False
        self.buttons_list[self.selected_button].selected=True
    
    def check_scroll_down(self):
        if self.state.down_pressed:
            if self.selected_button < len(self.buttons_list)-1:
                self.selected_button += 1
            else:
                self.selected_button = 0
            self.state.down_pressed = False

    def check_scroll_up(self):
        if self.state.up_pressed:
            if self.selected_button > 0:
                self.selected_button -= 1
            else:
                self.selected_button = len(self.buttons_list)-1
            self.state.up_pressed = False

    def modify_selected_index(self):
        self.check_scroll_down()
        self.check_scroll_up()
        

    def render_screen(self):
        self.render_title()
        self.render_start()
        self.render_highscores()
        self.render_about()
        self.render_options()
        self.render_exit()
        self.hover_selected()
        self.modify_selected_index()