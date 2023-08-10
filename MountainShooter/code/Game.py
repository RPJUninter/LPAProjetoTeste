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
        while True:
            menu = Menu(self.window)
            menu_return = menu.loop()
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                new_level = Level(self.window, "Level1", menu_return)
                new_level.loop()
