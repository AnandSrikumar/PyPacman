import pygame
from abc import ABC, abstractmethod

from src.configs.colors import Colors

class GameComponent(ABC):
    def __init__(self, pos, dims):
        self._pos = pos
        self.dims = dims
    
    @abstractmethod
    def render(self, screen):
        pass
    
    @abstractmethod
    def collide(self, other):
        pass
    
    @property
    def pos(self):
        return self._pos
    
    @pos.setter
    def pos(self, new_pos):
        self._pos = new_pos


class Dot(GameComponent):
    def __init__(self, pos, dims, radius_per=0.08, color=Colors.WHITE.value):
        super().__init__(pos, (dims))
        self._radius = dims[0]*radius_per
        x = self.pos[0] + self.dims[0] // 2
        y = self.pos[1] + self.dims[1]
        self.pos = (x, y)
        self.color = color
    
    def render(self, screen):
        pygame.draw.circle(screen, 
                           self.color, 
                           self.pos, self._radius)
    
    def collide(self, other):
        pass

class DebugDot(GameComponent):
    def __init__(self, pos, dims):
        super().__init__(pos, (dims))
        dims = list(dims)
        dims[0] = 2*dims[1]
        dims[1] *= 2
        self.dims = [pos[0], pos[1], dims[0], dims[1]]
    
    def render(self, screen):
        pygame.draw.rect(screen, 
                           Colors.YELLOW.value, 
                           self.dims, 0)
    
    def collide(self, other):
        pass
    
class Wall(GameComponent):
    def __init__(self, pos, dims, color=Colors.BLUE.value):
        super().__init__(pos, dims)
        self.width = dims[0]
        self.height = dims[1]
        self.color = color
    
    def render(self, screen):
        pygame.draw.rect(screen, self.color, 
                         pygame.Rect(self.pos[0], 
                                     self.pos[1], 
                                     self.width, 
                                     self.height),
                                     )
    
    def collide(self, other):
        pass

def create_dot(pos, dims):
    radius_per = 0.08
    color = Colors.WHITE.value
    return Dot(pos, dims, radius_per, color)

def create_power(pos, dims):
    radius_per = 0.16
    color = Colors.ORANGE.value
    return Dot(pos, dims, radius_per, color)

def create_wall(pos, dims):
    return Wall(pos, dims, Colors.BLUE.value)

def create_enemy_wall(pos, dims):
    return Wall(pos, dims, Colors.PINK.value)