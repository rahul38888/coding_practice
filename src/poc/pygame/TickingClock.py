import enum
import math
from datetime import datetime
from typing import List

import pygame
import sys
from pygame import Surface
from pygame.color import Color
from pygame.locals import QUIT

pygame.init()

width = 600
height = 300
surface = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Tick Tock!')

black = Color(0, 0, 0)
white = Color(200, 200, 200)
red = Color(255, 0, 0)
blue = Color(0, 0, 255)
green = Color(0, 255, 0)

font = pygame.font.SysFont('Calibri', 40, True, False)
text = font.render("Clock", True, green)
frame_rate = 1
clock = pygame.time.Clock()

surface.blit(text, [250, 260])

# music = pygame.mixer.Sound('match5.wav')
# music.play(0,0,0)


class TimeAttr(enum.Enum):
    SECOND = ("second", 60)
    MINUTE = ("minute", 60)
    HOUR = ("hour", 12)


class ClockHand:
    def __init__(self, parent_clock: "ClockObject", time_att: TimeAttr, length: int, color: Color):
        self.parent_clock = parent_clock
        self.time_att = time_att
        self.length = length
        self.color = color
        self.world_pos = None

    def recalculate(self, time=datetime.now()):
        att_max = self.time_att.value[1]
        value = int(time.__getattribute__(self.time_att.value[0]))
        angle = (2 * math.pi * value) / att_max
        w_offset = self.parent_clock.center[0] + self.length * math.sin(angle)
        h_offset = self.parent_clock.center[1] - self.length * math.cos(angle)
        self.world_pos = (w_offset, h_offset)

    def render(self, display: Surface):
        pygame.draw.line(display, self.color, self.parent_clock.center, self.world_pos, 3)


class ClockObject:
    def __init__(self, center: tuple, radius: int, color: Color, boundary_width: int = 5, knob_radius: int = 6):
        self.center = center
        self.radius = radius
        self.color = color
        self.boundary_width = boundary_width
        self.knob_radius = knob_radius
        self.hands: List[ClockHand] = list()

    def add_hand(self, time_att: TimeAttr, length: int, color: Color):
        self.hands.append(ClockHand(self, time_att, length, color))

    def recalculate(self, time=datetime.now()):
        for hand in self.hands:
            hand.recalculate(time)

    def render(self, display: Surface):
        pygame.draw.ellipse(display, self.color, (self.center[0] - self.radius, self.center[1] - self.radius,
                                                  2 * self.radius, 2 * self.radius), self.boundary_width)
        for hand in self.hands:
            hand.render(display)

        pygame.draw.circle(display, self.color, self.center, self.knob_radius)


start_time = datetime.now()
clock_object = ClockObject((width // 2, height // 2), 110, black)
clock_object.add_hand(TimeAttr.HOUR, 70, blue)
clock_object.add_hand(TimeAttr.MINUTE, 100, green)
clock_object.add_hand(TimeAttr.SECOND, 90, red)

if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(surface, white, (0, 0, width, height))
        clock_object.recalculate(datetime.now())
        clock_object.render(surface)

        pygame.display.update()
        clock.tick(frame_rate)
