#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Constant import EVENT_ENEMY_NUM, EVENT_ENEMY_TIME, MENU_OPTION, COLOR_WHITE
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator


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
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, 10))
            self.level_text(14, f'entities: {len(self.entity_list)}', COLOR_WHITE, (10, 30))
            EntityMediator.verify_colission(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            pygame.display.flip()  # atualizar tela
            for event in pygame.event.get():
                # evento de fechar janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY_NUM:
                    self.entity_list.append(EntityFactory.get_entity('Enemy1'))

    def level_text(self, text_size: int, text: str, text_color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(left=text_position[0], top=text_position[1])
        self.window.blit(source=text_surf, dest=text_rect)
