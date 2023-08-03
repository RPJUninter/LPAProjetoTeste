#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pygame

from code.Constant import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def loop(self):
        menu_return = None
        level_return = None
        while True:
            menu = Menu(self.window)
            menu_return = menu.loop()
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                for level in [Level(self.window, "Level1", menu_return)]:
                    level_return = level.loop()
