import pygame
from circleshape import *
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        pass

    def draw(self, screen):
        bullet_color = pygame.Color("white")
        pygame.draw.circle(screen, bullet_color, self.position, self.radius)
        pass

    def update(self, dt):
        self.position += self.velocity * dt
    