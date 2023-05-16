import pygame

import config
from utils.settings import readSettings
from screens.game import start_double_player
from screens.main_menu import main_menu
from config import GameMode
from pygame.locals import *
from config import flags
from config import config
from screens.game import start_single_player
from screens.rankingShow import rankingSHOW

settings = readSettings()
pygame.init()

pygame.event.set_allowed([QUIT, KEYDOWN, MOUSEBUTTONDOWN])  # If you need event to be handled - add it to the list.
# Only add these events, which are needed to save performance

# Screen initialisation
SCREEN = pygame.display.set_mode((settings["width"], settings["height"]), flags, 1)
SCREEN.set_alpha(None)
pygame.display.set_caption("Pong")

# First screen
#
print("\nPong game")
print("Resolution: "+str(config['width'])+"x"+str(config["height"]))
main_menu(SCREEN)
#start_single_player()
# start_double_player(SCREEN)
#rankingSHOW(SCREEN, 'single')