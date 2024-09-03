#National Flag
import pygame, sys
from pygame.locals import *

pygame.init()

fps = 30
clock = pygame.time.Clock()

D = pygame.display.set_mode((600, 300), 0, 32)
pygame.display.set_caption('Flag of India')

W = (255, 255, 255)
R = (255, 0, 0)
G = (0, 204, 0)
M = (255, 128, 0)
B = (0, 0, 255)
BL = (0, 0, 0)
D.fill(W)

pygame.draw.rect(D, M, (0, 0, 600, 100))
pygame.draw.rect(D, G, (0, 200, 600, 100))

chakra1 = pygame.image.load('chakra1.png')
chakra2 = pygame.image.load('chakra2.png')
chakra3 = pygame.image.load('chakra3.png')

x = 250
y = 100

pre = chakra1
if __name__ == '__main__':
    while True:
        D.blit(pre, (x, y))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        pygame.draw.rect(D, W, (250, 100, 100, 100))
        if pre == chakra1:
            pre = chakra2
        elif pre == chakra2:
            pre = chakra3
        else:
            pre = chakra1
        clock.tick(fps)
