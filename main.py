import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock_obj = pygame.time.Clock()
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (1,1,1))
        pygame.display.flip()
        # End of loop - tick
        dt = clock_obj.tick(60) / 1000


if __name__ == "__main__":
    main()
