#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface

from code.Constant import EVENT_ENEMY_NUM, EVENT_ENEMY_TIME, MENU_OPTION
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window: Surface, name: str, mode: str):
        self.window: Surface = window
        self.name: str = name
        self.mode: str = mode  # NEW GAME 1P','NEW GAME 2P - COOPERATIVE','NEW GAME 2P - COMPETITIVE',
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(name=f'{self.name}Bg'))
        self.entity_list.append(EntityFactory.get_entity(name='Player1'))
        if mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity(name='Player2'))
        pygame.time.set_timer(EVENT_ENEMY_NUM, EVENT_ENEMY_TIME[self.name])

    def loop(self):
        clock = pygame.time.Clock()
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play()
        while True:
            clock.tick(60)
            [self.window.blit(ent.surf, ent.rect) for ent in self.entity_list]
            for ent in self.entity_list:
                shot = ent.update()
                if shot is not None:
                    self.entity_list.append(shot)
            pygame.display.flip()  # atualizar tela
            for event in pygame.event.get():
                # evento de fechar janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY_NUM:
                    self.entity_list.append(EntityFactory.get_entity('Enemy1'))
