#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC

from code.Background import Background
from code.Constant import WIN_WIDTH


class EntityFactory(ABC):

    @staticmethod
    def get_entity(name: str, position=(0, 0)):
        match name:
            case 'Level1Bg':
                bg_list = []
                for i in range(7):
                    bg_list.append(Background(f'Level1Bg{i}', (0, 0)))
                    bg_list.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return bg_list
