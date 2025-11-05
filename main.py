import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock_obj = pygame.time.Clock()
    # player grouping
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    my_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # asteroid grouping
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    # AsteroidField grouping
    AsteroidField.containers = (updatable)
    my_asteroid_field = AsteroidField()

    # start of game loop
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (1,1,1))
        updatable.update(dt)
        for obj in asteroids:
            if my_player.collision_check(obj):
                print("Game over!")
                exit(0)

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        # End of loop - tick
        dt = clock_obj.tick(60) / 1000



if __name__ == "__main__":
    main()
