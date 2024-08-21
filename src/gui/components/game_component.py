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
    def __init__(self, pos, dims):
        super().__init__(pos, (dims))
        self._radius = dims[0]*0.08
        x = self.pos[0] + self.dims[0] // 2
        y = self.pos[1] + self.dims[1] // 2
        self.pos = (x, y)
    
    def render(self, screen):
        pygame.draw.circle(screen, 
                           Colors.WHITE.value, 
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
    def __init__(self, pos, dims):
        super().__init__(pos, dims)
        self.width = dims[0]
        self.height = dims[1]
    
    def render(self, screen):
        pygame.draw.rect(screen, Colors.BLUE.value, 
                         pygame.Rect(self.pos[0], 
                                     self.pos[1], 
                                     self.width, 
                                     self.height),
                                     )
    
    def collide(self, other):
        pass
