#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image

from code.Constant import ENTITY_MOV_DELAY


class Entity(ABC):
    def __init__(self, name: str, position: tuple) -> object:
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.mov_delay = ENTITY_MOV_DELAY[name]

    @abstractmethod
    def move(self):
        pass
