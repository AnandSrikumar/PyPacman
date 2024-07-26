from .screen_state import GameScreen
class State:
    def __init__(self):
        self.__running: bool = True
        self.__game_screen: int = GameScreen.MAIN_MENU
        self.__down_pressed: bool = False
        self.__up_pressed: bool = False
        self.__enter_clicked: bool = False

    @property
    def running(self):
        return self.__running
    
    @running.setter
    def running(self, val: bool):
        self.__running = val

    @property
    def game_screen(self):
        return self.__game_screen
    
    @game_screen.setter
    def game_screen(self, screen: GameScreen):
        if not isinstance(screen, GameScreen):
            raise ValueError("screen must be an instance of GameScreen Enum")
        self.__game_screen = screen
    
    @property
    def down_pressed(self):
        return self.__down_pressed
    
    @down_pressed.setter
    def down_pressed(self, val):
        self.__down_pressed = val

    @property
    def up_pressed(self):
        return self.__up_pressed
    
    @up_pressed.setter
    def up_pressed(self, val):
        self.__up_pressed = val

    @property
    def enter(self):
        return self.__enter_clicked

    @enter.setter
    def enter(self, val):
        self.__enter_clicked = val