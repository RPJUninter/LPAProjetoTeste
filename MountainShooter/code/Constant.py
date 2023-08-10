# C
import pygame

COLOR_ORANGE = (255, 168, 0)
COLOR_YELLOW = (255, 255, 128)
COLOR_WHITE = (255, 255, 255)

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')
#  W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# E
EVENT_ENEMY_NUM = pygame.USEREVENT + 1
EVENT_ENEMY_TIME = {'Level1': 2000}

ENTITY_PIXEL_MOV = {'Level1Bg0': 0,
                    'Level1Bg1': 1,
                    'Level1Bg2': 2,
                    'Level1Bg3': 3,
                    'Level1Bg4': 4,
                    'Level1Bg5': 5,
                    'Level1Bg6': 6,
                    'Player1': 5,
                    'Player1Shot': 6,
                    'Enemy1': 3}

# K
KEY_UP = {'Player1': pygame.K_w}
KEY_RIGHT = {'Player1': pygame.K_d}
KEY_DOWN = {'Player1': pygame.K_s}
KEY_LEFT = {'Player1': pygame.K_a}
KEY_SHOT = {'Player1': pygame.K_LCTRL}
