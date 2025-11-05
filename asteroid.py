import pygame
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)        
        pass

    def draw(self, screen):
        asteroid_color = pygame.Color("white")
        pygame.draw.circle(screen, asteroid_color, self.position, self.radius)
        pass

    def update(self, dt):
        self.position += self.velocity * dt 
    