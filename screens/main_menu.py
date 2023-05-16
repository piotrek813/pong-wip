import sys

import pygame

from button import Button
from screens.game_mode import game_mode
from screens.options import options
from utils.get_font import get_font
# from config import config


def main_menu(SCREEN):
    while 1:
        SCREEN.fill('black')

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        logo = pygame.image.load('assets/pongologo.png')
        MENU_LOGO = pygame.transform.scale(logo, (580, 580))
        MENU_RECT = MENU_LOGO.get_rect(center=(640, 210))

        PLAY_MODE_BUTTON = Button(pos=(640, 420), text_input="PLAY", font=get_font(75))
        SETTINGS_BUTTON = Button(pos=(640, 540), text_input="SETTINGS", font=get_font(75))
        QUIT_BUTTON = Button(pos=(640, 660), text_input="QUIT", font=get_font(75))

        SCREEN.blit(MENU_LOGO, MENU_RECT)

        for button in [PLAY_MODE_BUTTON, SETTINGS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_MODE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game_mode(SCREEN)
                if SETTINGS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options(SCREEN)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
