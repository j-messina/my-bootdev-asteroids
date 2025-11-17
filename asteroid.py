from circleshape import *
from constants import *
from logger import log_state
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__( x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            temp_rand = random.uniform(20,50)
            new_ast_1_vec = self.velocity.rotate(temp_rand)
            new_ast_2_vec = self.velocity.rotate(-1 * temp_rand)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_ast_1.velocity = new_ast_1_vec * 1.2
            new_ast_2.velocity = new_ast_2_vec * 1.2
