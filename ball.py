import pygame.draw

from config import config
from score import score


class Ball:
    COLOR = (255, 255, 255)


    def __init__(self, pos, radius, speed):
        self.original_x = pos[0]
        self.original_y = pos[1]
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.width = radius
        self.original_x_speed = speed[0]
        self.original_y_speed = speed[1]
        self.x_speed = speed[0]
        self.y_speed = speed[1]
        self.collision_sound = pygame.mixer.Sound('assets/collision.wav')

    def draw(self, SCREEN):
        pygame.draw.rect(surface=SCREEN, color=self.COLOR, rect=pygame.Rect(self.x_pos, self.y_pos, self.width, self.width))

    def move(self):
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed

    def collisions_4_walls(self, WIDTH, HEIGHT, WALL_THICKNESS):
        if self.x_pos <= 0+WALL_THICKNESS or self.x_pos+self.width >= WIDTH-WALL_THICKNESS:
            self.x_speed *= -1
            pygame.mixer.Sound.play(self.collision_sound)
        if self.y_pos+self.width >= HEIGHT-WALL_THICKNESS or self.y_pos <= 0+WALL_THICKNESS:
            self.y_speed *= -1
            pygame.mixer.Sound.play(self.collision_sound)

    def handleCollisionLeft(self, WALL_THICKNESS):
        return self.x_pos <= WALL_THICKNESS

    def handleCollisionRight(self, WIDTH, WALL_THICKNESS):
        return self.x_pos+self.width >= WIDTH-WALL_THICKNESS

    def handleCollisionDown(self, HEIGHT, WALL_THICKNESS):
        return self.y_pos + self.width >= HEIGHT - WALL_THICKNESS

    def handleCollisionTop(self, WALL_THICKNESS):
        return self.y_pos <= 0 + WALL_THICKNESS

    def handleWallCollisionDoublePlayer(self):
        WIDTH = config['width']
        HEIGHT = config['height']
        WALL_THICKNESS = config['WALL_THICKNESS']

        if self.handleCollisionDown(HEIGHT, WALL_THICKNESS) or self.handleCollisionTop(WALL_THICKNESS):
            self.y_speed *= -1
            pygame.mixer.Sound.play(self.collision_sound)
        if self.handleCollisionRight(WIDTH, 0) or self.handleCollisionLeft(0):
            if self.handleCollisionLeft(0):
                score['right'] += 1
            elif self.handleCollisionRight(WIDTH, 0):
                score['left'] += 1

            self.reset()


    def handlePaddleRCollision(self, right_paddle):
        if self.y_pos >= right_paddle.y_pos and self.y_pos <= right_paddle.y_pos + right_paddle.height:
            if self.x_pos + self.width >= right_paddle.x_pos:
                self.x_speed *= -1
                pygame.mixer.Sound.play(self.collision_sound)

    def handlePaddleLCollision(self, left_paddle):
        if self.y_pos >= left_paddle.y_pos and self.y_pos <= left_paddle.y_pos + left_paddle.height:
            if self.x_pos <= left_paddle.x_pos + left_paddle.width:
                self.x_speed *= -1
                pygame.mixer.Sound.play(self.collision_sound)

    def handleCollisionDoublePlayer(self, paddleR, paddleL):
        self.handleWallCollisionDoublePlayer()

        self.handlePaddleRCollision(paddleR)
        self.handlePaddleLCollision(paddleL)

    def handleWallCollisionSinglePlayer(self):
        WIDTH = config['width']
        HEIGHT = config['height']
        WALL_THICKNESS = config['WALL_THICKNESS']

        if self.handleCollisionDown(HEIGHT, WALL_THICKNESS) or self.handleCollisionTop(WALL_THICKNESS):
            self.y_speed *= -1
            pygame.mixer.Sound.play(self.collision_sound)
        if self.handleCollisionRight(WIDTH, WALL_THICKNESS):
            self.x_speed *= -1
            pygame.mixer.Sound.play(self.collision_sound)
        if self.handleCollisionLeft(WALL_THICKNESS):
            self.reset()
            score['left'] += 1

    def handleCollisionSinglePlayer(self, paddle):
        self.handleWallCollisionSinglePlayer()

        self.handlePaddleLCollision(paddle)

    def reset(self):
        self.x_pos = self.original_x
        self.y_pos = self.original_y
        self.x_speed *= -1
        self.y_speed *= -1
