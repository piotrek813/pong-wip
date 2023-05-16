from enum import Enum

from pygame import FULLSCREEN, DOUBLEBUF, SCALED
from utils.settings import readSettings

settings = readSettings()

config = settings
config['TEXT_COLOR'] = (255, 255, 255)
config['TEXT_COLOR_HOVER'] = (147, 149, 153)
config['WALL_THICKNESS'] = 40


class GameMode(Enum):
    SINGLE = 'single'
    DOUBLE = 'double'


# Settings from the JSON
settings = readSettings()

if settings["fullscreen"]:
    flags = FULLSCREEN | DOUBLEBUF  # Enable double buffered fullscreen
else:
    flags = SCALED | DOUBLEBUF  # Enable double buffered windowed
