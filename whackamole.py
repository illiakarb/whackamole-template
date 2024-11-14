import pygame
import random

# ILLIA KARBIVNYCHYI 21633064

def main():
    x = 0
    y = 0
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] // 32 == x // 32 and event.pos[1] // 32 == y // 32:
                        x = random.randrange(0, 20) * 32
                        y = random.randrange(0, 16) * 32
            screen.fill("light green")
            for i in range(20):
                pygame.draw.line(screen, 'black', (32 + (i * 32), 0), (32 + (i * 32), 512))
            for i in range(0, 16):
                pygame.draw.line(screen, 'black', (0, 32 + (i * 32)), (640, 32 + (i * 32)))
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
