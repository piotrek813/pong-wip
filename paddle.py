import pygame.draw

from config import config


class Paddle:
    speed = 10

    def __init__(self, pos, width, height, keyUp, keyDown, color=(255, 255, 255)):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.width = width
        self.height = height
        self.keyUp = keyUp
        self.keyDown = keyDown
        self.color = color

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x_pos, self.y_pos, self.width, self.height))

    def move(self, keys):

        if keys[self.keyDown]:
            if self.y_pos + self.height + self.speed <= config['height'] - config['WALL_THICKNESS']:
                self.y_pos += self.speed
        elif keys[self.keyUp]:
            if self.y_pos - self.speed >= config['WALL_THICKNESS']:
                self.y_pos -= self.speed
