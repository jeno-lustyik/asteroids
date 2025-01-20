import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill("black")
        pygame.display.flip()
        player.draw(screen)

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
