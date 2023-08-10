#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Constant import ENTITY_PIXEL_MOV
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_PIXEL_MOV['Enemy1']

    def update(self):
        self.move()