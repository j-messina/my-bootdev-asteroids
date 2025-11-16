import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock_obj = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shootable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable)
    # 11/15/2025 AAHHHH EVERYTHING'S FUCKED BECAUSE OF THIS STUPID LOGGING UPDATE. ITS ALL FUCKED
    shots = []
    my_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots=shots)
    my_asteroid_field = AsteroidField()
    
    
    


    # start of game loop
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (1,1,1))

        # in the game loop each frame:
        # for s in shots:
        #     s.update(dt)
        # for s in shots:
        #     s.draw(screen)

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
