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

# E
EVENT_ENEMY_NUM = pygame.USEREVENT + 1
EVENT_ENEMY_TIME = {'Level1': 3000}

ENTITY_HEALTH = {'Level1Bg0': 9999,
                 'Level1Bg1': 9999,
                 'Level1Bg2': 9999,
                 'Level1Bg3': 9999,
                 'Level1Bg4': 9999,
                 'Level1Bg5': 9999,
                 'Level1Bg6': 9999,
                 'Player1': 300,
                 'Player1Shot': 1,
                 'Player2': 300,
                 'Player2Shot': 1,
                 'Enemy1': 100,
                 'Enemy1Shot': 1,
                 'Enemy2': 100,
                 'Enemy2Shot': 1,
                 'Enemy3': 100,
                 'Enemy3Shot': 1,
                 'Enemy4': 100,
                 'Enemy4Shot': 1}

ENTITY_PIXEL_MOV = {'Level1Bg0': 0,
                    'Level1Bg1': 1,
                    'Level1Bg2': 2,
                    'Level1Bg3': 3,
                    'Level1Bg4': 4,
                    'Level1Bg5': 5,
                    'Level1Bg6': 6,
                    'Player1': 5,
                    'Player1Shot': 6,
                    'Player2': 5,
                    'Player2Shot': 6,
                    'Enemy1': 3,
                    'Enemy1Shot': 4,
                    'Enemy2': 3,
                    'Enemy2Shot': 4,
                    'Enemy3': 3,
                    'Enemy3Shot': 4,
                    'Enemy4': 3,
                    'Enemy4Shot': 4}

ENTITY_SHOT_DELAY = {'Player1': 20,
                     'Player2': 20,
                     'Enemy1': 60,
                     'Enemy2': 60,
                     'Enemy3': 60,
                     'Enemy4': 60}

# K
KEY_UP = {'Player1': pygame.K_w, 'Player2': pygame.K_UP}
KEY_RIGHT = {'Player1': pygame.K_d, 'Player2': pygame.K_RIGHT}
KEY_DOWN = {'Player1': pygame.K_s, 'Player2': pygame.K_DOWN}
KEY_LEFT = {'Player1': pygame.K_a, 'Player2': pygame.K_LEFT}
KEY_SHOT = {'Player1': pygame.K_LCTRL, 'Player2': pygame.K_RCTRL}

#  W
WIN_WIDTH = 576
WIN_HEIGHT = 324
