#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Constant import WIN_WIDTH, ENTITY_MOV_DELAY
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_MOV_DELAY[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
