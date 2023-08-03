#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface

from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window: Surface, name: str, mode: str):
        self.window: Surface = window
        self.name: str = name
        self.mode: str = mode  # NEW GAME 1P','NEW GAME 2P - COOPERATIVE','NEW GAME 2P - COMPETITIVE',
        self.entity_list: list = []
        self.entity_list.extend(EntityFactory.get_entity(name=f'Level1Bg'))

    def loop(self):
        clock = pygame.time.Clock()
        pygame.mixer_music.load('./asset/Level1.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play()
        while True:
            clock.tick(120)
            [self.window.blit(ent.surf, ent.rect) for ent in self.entity_list]
            [ent.move() for ent in self.entity_list]
            pygame.display.flip()  # atualizar tela
            for event in pygame.event.get():
                # evento de fechar janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
