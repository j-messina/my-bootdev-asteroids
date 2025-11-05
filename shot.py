import pygame
from circleshape import *
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y, radius = SHOT_RADIUS):
        self.super().__init__(x, y, radius)
        pass

    def draw(self, screen):
        bullet_color = pygame.Color("green")
        pygame.draw.circle(screen, bullet_color, self.position, self.radius)
        pass

    def update(self, dt):
        self.position = self.velocity * dt
    