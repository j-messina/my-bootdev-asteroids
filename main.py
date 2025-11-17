import pygame
import sys
from constants import *
from logger import log_state
from logger import log_event
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)


    clock = pygame.time.Clock()
    dt = 0

    my_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    my_asteroidfield = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        for obj in asteroids:
            for a_shot in shots:
                if obj.collides_with(a_shot):
                    log_event("asteroid_shot")
                    a_shot.kill()
                    obj.split()

        for obj in asteroids:
            if my_player.collides_with(obj):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        dt = clock.tick(60) / 1000
        pygame.display.flip()



if __name__ == "__main__":
    main()
