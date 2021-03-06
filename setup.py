# Created by jmlm at 15/02/2020-23:10 - test2
"""
Les constantes globales
"""


# defines
MAP_FILE = "ressource/map01.txt"
NB_ITEMS = 3
PATH_BLOCK = "."
WALL_BLOCK = "w"
START_BLOCK = "S"
GOAL_BLOCK = "G"
NB_COLS = 14
NB_LINES = 14
MC_GYVER = "M"
CHOICES = {
    'R': 'right',
    'L': 'left',
    'U': 'up',
    'D': 'down',
    'Q': 'quit',
    'S': 'save'
    }

# pygame
SCREEN_WIDTH = 630
SCREEN_HEIGTH = 630
SPRITE_HEIGTH = SCREEN_HEIGTH / NB_COLS
SPRITE_WIDTH = SCREEN_WIDTH / NB_COLS
BG_FILE = "ressource/background.jpg"
MC_GYVER_FILE = "ressource/MacGyver.png"
GUARD_FILE = "ressource/Gardien.png"
WALL_FILE = "ressource/wall.png"
ITEM1_FILE = "ressource/aiguille.png"
ITEM2_FILE = "ressource/ether.png"
ITEM3_FILE = "ressource/tube_plastique.png"
LOOSE_MUSIC = "ressource/8548.mp3"
WIN_MUSIC = "ressource/8548-1.mp3"

# fonts
font_freesansbold = "freesansbold.ttf"
font_dejavu = "ressource/DejaVuSans.ttf"
font_bebas = "ressource/BebasNeue-Regular.ttf"

# colors
colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'orange': (255, 165, 0)
}
# counter color --> depens of items caught
msg_couleur = {
    0: 'black',
    1: 'red',
    2: 'orange',
    3: 'green'
}