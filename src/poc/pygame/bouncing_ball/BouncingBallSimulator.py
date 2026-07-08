import pygame, sys, math, random
from pygame.locals import *


def cal_pos(t):
    u = 75
    g = 10
    x = 0

    while True:
        if t == 0:
            x = 0
        x = u * t - (g * t * t) / 2
        y = math.floor(x)
        return y


pygame.init()

D = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Text formating')

W = (255, 255, 255)
R = (255, 0, 0)
B = (210, 210, 255)
G = (100, 255, 100)
S = (150, 150, 150)
BACK = B

i = 0
fps = 480
time = 0
pos_x = 0
pos_y = 400
speed_y = 0
tree1_x = random.randint(0, 750)
tree2_x = (tree1_x + 200) % 800
tree3_x = (tree2_x + 200) % 800
rock_x = (tree3_x + 200) % 800
cloud_speed = 1 / 4
cloud1_y = 800
cloud1_x = random.randint(0, 300)
cloud2_y = 300
cloud2_x = (cloud1_y + 80) % 400
cloud3_y = 50
cloud3_x = (cloud1_y + 200) % 400

move_x = False
move_y = False

clock = pygame.time.Clock()

# images
tree1 = pygame.image.load('Tree_Short.png')
tree2 = pygame.image.load('Tree_Tall.png')
tree3 = pygame.image.load('Tree_Ugly.png')
rock = pygame.image.load('Rock.png')
ball_shadow = pygame.image.load('ball_shadow.png')
ball = pygame.image.load('ball.png')
grass = pygame.image.load('grass.png')
ground = pygame.image.load('ground.png')
cloud1 = pygame.image.load('cloud1.png')
cloud2 = pygame.image.load('cloud2.png')
cloud3 = pygame.image.load('cloud2.png')

D.fill(BACK)

if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit("Exiting")
            elif event.type == KEYDOWN:
                user = pygame.key.get_pressed()
                if event.key == K_UP:
                    # time=0
                    # pos_x=0
                    move_x = True
                elif event.key == K_DOWN:
                    move_x = "Stop"

                elif event.key == K_RIGHT:
                    speed_y += 1
                    move_y = True

                elif event.key == K_LEFT:
                    speed_y += -1
                    move_y = True

                elif event.key == K_TAB:
                    time = 0
                    pos_x = 0
                    pos_y = 400
                    speed_y = 0
                    tree1_x = random.randint(0, 750)
                    tree2_x = (tree1_x + 200) % 800
                    tree3_x = (tree2_x + 200) % 800
                    rock_x = (tree3_x + 200) % 800
                    move_x = False

                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit("Exiting")

        if move_x == True:
            y = cal_pos(time)
            if y >= 0:
                pos_x = y
            else:
                pos_x = 0
            if pos_x == 0:
                time = 0
                pos_x = 0
                move_x = True
            time = time + 1 / 10
        elif move_x == "Stop":
            y = cal_pos(time)
            if y >= 0:
                pos_x = y
            else:
                pos_x = 0
            time = time + 1 / 10
            move_y = "Stop"

        if move_y == True:
            pos_y = (pos_y + speed_y) % 800
        elif move_y == "Stop":
            if pos_x != 0:
                pos_y = (pos_y + speed_y) % 800
            else:
                speed_y = 0

        if cloud1_y == -160:
            cloud1_x = random.randint(0, 300)
            cloud1_y = 800
        else:
            cloud1_y -= cloud_speed + 1 / 4

        if cloud2_y == -160:
            cloud2_x = random.randint(0, 300)
            cloud2_y = 800
        else:
            cloud2_y -= cloud_speed

        if cloud3_y == -160:
            cloud3_x = random.randint(0, 300)
            cloud3_y = 800
        else:
            cloud3_y -= cloud_speed + 1 / 8

        pygame.draw.rect(D, BACK, [0, 0, 800, 600])
        D.blit(cloud1, (cloud1_y, cloud1_x))
        D.blit(cloud2, (cloud2_y, cloud2_x))
        D.blit(grass, (0, 458))
        D.blit(ground, (0, 500))
        D.blit(tree1, (tree1_x, 475))
        D.blit(tree3, (tree3_x, 480))
        D.blit(rock, (rock_x, 470))
        if 0 <= pos_x <= 40:
            D.blit(ball_shadow, (pos_y - 10, 545 - pos_x))

        D.blit(ball, (pos_y + 10, 530 - pos_x))
        D.blit(tree2, (tree2_x, 530))

        pygame.display.update()
        clock.tick(fps)