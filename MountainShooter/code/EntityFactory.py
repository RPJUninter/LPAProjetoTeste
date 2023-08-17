#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from abc import ABC

from code.Background import Background
from code.Constant import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player
from code.PlayerShot import PlayerShot


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

            case 'Player1':
                return Player(name='Player1', position=(30, WIN_HEIGHT / 2 - 30))

            case 'Player2':
                return Player(name='Player2', position=(30, WIN_HEIGHT / 2 + 30))

            case 'Enemy1':
                return Enemy(name='Enemy1', position=(WIN_WIDTH, random.randint(30, WIN_HEIGHT - 30)))

            case 'Enemy2':
                return Enemy(name='Enemy2', position=(WIN_WIDTH, random.randint(30, WIN_HEIGHT - 30)))

            case 'Enemy3':
                return Enemy(name='Enemy3', position=(WIN_WIDTH, random.randint(30, WIN_HEIGHT - 30)))

            case 'Enemy4':
                return Enemy(name='Enemy4', position=(WIN_WIDTH, random.randint(30, WIN_HEIGHT - 30)))
