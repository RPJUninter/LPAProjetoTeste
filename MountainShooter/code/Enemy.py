#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Constant import ENTITY_PIXEL_MOV, SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_PIXEL_MOV['Enemy1']

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

    def update(self):
        self.move()
        return self.shoot()
