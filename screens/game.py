import sys

import pygame

from ball import Ball
from button import Button
from config import GameMode, config
from paddle import Paddle
from score import score
from utils.get_font import get_font
from utils.settings import readSettings
from screens.main_menu import main_menu
from config import settings

def game(SCREEN, mode):
    if mode == GameMode.SINGLE:
        start_single_player(SCREEN)
    if mode == GameMode.DOUBLE:
        start_double_player(SCREEN)

def start_single_player(SCREEN):
    score['left'] = 0
    score['right'] = 0
    score['set'] = 1
    score['setWonByLeft'] = 0
    score['setWonByRight'] = 0
    PADDLE_WIDTH = 25
    PADDLE_HEIGHT = 180
    paddle = Paddle([20, config["height"] // 2 - PADDLE_HEIGHT // 2],
                      PADDLE_WIDTH, PADDLE_HEIGHT, keyUp=pygame.K_UP, keyDown=pygame.K_DOWN)

    ball_width = 30

    ball_pos = ((config['width'] - ball_width) // 2, (config['height'] - ball_width) // 2)
    ball = Ball(ball_pos, ball_width, [2, 2])

    bg = pygame.image.load("assets/bg-single.png")
    heartImg = pygame.image.load('assets/heart.png')

    settings = readSettings()

    max_set_score = 3

    while 1:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        left_score = score['left']

        if (not settings['brown_floyd']):
            SCREEN.fill("black")
        SCREEN.blit(bg, (0, 0))

        # if score['left'] == max_set_score
        #     score['set'] += 1
        #     if left_score == max_set_score:
        #         score['setWonByLeft'] += 1
        #     elif right_score == max_set_score:
        #         score['setWonByRight'] += 1
        #
        #     score['left'] = score['right'] = 0
        #
        #     if (ball.x_speed < 4):
        #         ball.x_speed *= 1.3
        #     if (ball.y_speed < 4):
        #         ball.y_speed *= 1.3
        if left_score == max_set_score:
            main_menu(SCREEN)
            score['left'] = 0

        # RANKING = Button(
        #     pos=(640, 460),
        #     text_input="RANKING",
        #     font=get_font(75),
        #     base_color="White",
        #     hovering_color="Green"
        # )
        #
        # RANKING.changeColor(PLAY_MOUSE_POS)
        # RANKING.update(SCREEN)
        keys = pygame.key.get_pressed()

        ball.draw(SCREEN)
        ball.move()
        ball.handleCollisionSinglePlayer(paddle)

        paddle.draw(SCREEN)
        paddle.move(keys)

        for i in range(1, 4 - score['left']):
            SCREEN.blit(heartImg, (config['width'] - config['WALL_THICKNESS'] - 10 - 64 * i, config['WALL_THICKNESS'] + 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if RANKING.checkForInput(PLAY_MOUSE_POS):
            #         from screens.ranking import ranking
            #         ranking(SCREEN, "single")

        pygame.display.update()

def start_double_player(SCREEN):
    score['left'] = 0
    score['right'] = 0
    score['set'] = 1
    score['setWonByLeft'] = 0
    score['setWonByRight'] = 0
    PADDLE_WIDTH = 25
    PADDLE_HEIGHT = 180
    paddle_r = Paddle([config["width"] - 20 - PADDLE_WIDTH, config["height"] // 2 - PADDLE_HEIGHT // 2],
                      PADDLE_WIDTH, PADDLE_HEIGHT, keyUp=pygame.K_UP, keyDown=pygame.K_DOWN)
    paddle_l = Paddle([20, config["height"] // 2 - PADDLE_HEIGHT // 2],
                      PADDLE_WIDTH, PADDLE_HEIGHT, keyUp=pygame.K_w, keyDown=pygame.K_s)

    paddles = [paddle_l, paddle_r]

    ball_width = 30
    ball_pos = ((config['width'] - ball_width) // 2, (config['height'] - ball_width) // 2)
    ball = Ball(ball_pos, ball_width, [3, 3])

    max_set_score = 3

    settings = readSettings()
    bg = pygame.image.load("assets/bg-double.png")

    while 1:
        left_score = score['left']
        right_score = score['right']
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        if not settings['brown_floyd']:
            SCREEN.fill("black")
        SCREEN.blit(bg, (0, 0))

        # PLAY_TEXT = get_font(45).render("This is the Double GAME screen.", True, "White")
        # PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        # SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        if left_score == max_set_score or right_score == max_set_score:
            score['set'] += 1
            if left_score == max_set_score:
                score['setWonByLeft'] += 1
            elif right_score == max_set_score:
                score['setWonByRight'] += 1

            score['left'] = score['right'] = 0

            if (ball.x_speed < 4):
                ball.x_speed *= 1.3
            if (ball.y_speed < 4):
                ball.y_speed *= 1.3

        if score['setWonByLeft'] == 3 or score['setWonByRight'] == 3:
            from screens.ranking import ranking
            ranking(SCREEN, "double")


        left_score_text = get_font(80).render(f"{left_score}", True, "White")
        right_score_text = get_font(80).render(f"{right_score}", True, "White")

        SCREEN.blit(left_score_text, (config['width'] // 4 + left_score_text.get_width() // 2, 60))
        SCREEN.blit(right_score_text, (config['width'] * (3 / 4) - right_score_text.get_width() // 2, 60))

        # RANKING = Button(
        #     pos=(640, 460),
        #     text_input="RANKING",
        #     font=get_font(75),
        #     base_color="White",
        #     hovering_color="Green"
        # )
        #
        # RANKING.changeColor(PLAY_MOUSE_POS)
        # RANKING.update(SCREEN)
        keys = pygame.key.get_pressed()

        ball.draw(SCREEN)
        ball.move()
        ball.handleCollisionDoublePlayer(paddle_r, paddle_l)

        for paddle in paddles:
                paddle.draw(SCREEN)
                paddle.move(keys)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if RANKING.checkForInput(PLAY_MOUSE_POS):
            #         from screens.ranking import ranking
            #         ranking(SCREEN)

        pygame.display.update()
