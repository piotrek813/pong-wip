import sys

import pygame

from ball import Ball
from button import Button
from config import config, GameMode
from utils.get_font import get_font


def draw_game_mode(SCREEN, ball):
    SCREEN.fill("black")
    ball.draw(SCREEN)

    OPTIONS_TEXT = get_font(75).render("SELECT GAME MODE", True, config['TEXT_COLOR'])
    OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 200))
    SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

    SINGLE_PLAYER_BUTTON = Button(pos=(640, 320),
                                  text_input="SINGLE PLAYER GAME", font=get_font(50))
    DOUBLE_PLAYER_BUTTON = Button(pos=(640, 400),
                                  text_input="DOUBLE PLAYER GAME", font=get_font(50))
    BACK_BUTTON = Button(pos=(640, 510),
                         text_input="BACK", font=get_font(75))

    OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

    for button in [SINGLE_PLAYER_BUTTON, DOUBLE_PLAYER_BUTTON, BACK_BUTTON]:
        button.changeColor(OPTIONS_MOUSE_POS)
        button.update(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if BACK_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                from screens.main_menu import main_menu
                main_menu(SCREEN)
            if SINGLE_PLAYER_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                from screens.game import game
                game(SCREEN, mode=GameMode.SINGLE)
            if DOUBLE_PLAYER_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                from screens.game import game
                game(SCREEN, mode=GameMode.DOUBLE)

    pygame.display.update()


def game_mode(SCREEN):
    BALL = Ball([100, 100], 30, [5, 5])

    while 1:
        draw_game_mode(SCREEN, BALL)
        BALL.draw(SCREEN)
        BALL.move()
        BALL.collisions_4_walls(config['width'], config['height'], 0)  # WALL THICKNESS
