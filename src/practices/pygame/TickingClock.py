# National Flag
import pygame, sys
import math
from pygame.locals import *

pygame.init()

D = pygame.display.set_mode((600, 300), 0, 32)
pygame.display.set_caption('Tick Tock!')

i = 0
p = 0
a = 0
b = 0
j = math.pi / 60

W = (255, 255, 255)
R = (255, 0, 0)
B = (0, 0, 255)
G = (0, 255, 0)

font = pygame.font.SysFont('Calibri', 40, True, False)
text = font.render("Clock", True, G)
clock = pygame.time.Clock()

D.fill(W)
pygame.draw.ellipse(D, B, (190, 40, 220, 220), 1)
D.blit(text, [250, 260])

# music=pygame.mixer.Sound('match5.wav')
# music.play(0,0,0)

if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # for i in range(20000):
        pygame.draw.rect(D, W, (a - 5, b - 5, 10, 10))
        a = 300 + 100 * math.cos(i)
        b = 150 + 100 * math.sin(i)
        pygame.draw.ellipse(D, R, (a - 5, b - 5, 10, 10))
        p = p + 1
        i = p * j

        pygame.display.update()
        clock.tick(1)