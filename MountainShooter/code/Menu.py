#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect, KEYDOWN, K_UP, K_DOWN, K_RETURN
from pygame.font import Font

from code.Constant import COLOR_ORANGE, WIN_WIDTH, MENU_OPTION, COLOR_YELLOW, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf: Surface = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect: Rect = self.surf.get_rect(left=0, top=0)

    def loop(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play()
        op_selected = 0  # opção selecionada
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # desenhar imagem de fundo do menu
            # lógica para desenhar o título do menu
            self.menu_text(50, "Mountain", COLOR_ORANGE, (WIN_WIDTH / 2, 70))  # linha 1 do título
            self.menu_text(50, "Shooter", COLOR_ORANGE, (WIN_WIDTH / 2, 120))  # linha 2 do título
            # lógica desenhar as opções do menu
            for menu_op in range(len(MENU_OPTION)):
                if menu_op == op_selected:
                    self.menu_text(20, MENU_OPTION[menu_op], COLOR_YELLOW, (WIN_WIDTH / 2, 200 + 30 * menu_op))
                else:
                    self.menu_text(20, MENU_OPTION[menu_op], COLOR_WHITE, (WIN_WIDTH / 2, 200 + 30 * menu_op))
            pygame.display.flip()  # atualizar tela

            # iterar lista de eventos
            for event in pygame.event.get():
                # evento de fechar janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # evento de tecla pressionada
                if event.type == KEYDOWN:
                    # lógica para tecla seta para baixo
                    if event.key == K_DOWN:
                        if op_selected < len(MENU_OPTION) - 1:
                            op_selected += 1
                        else:
                            op_selected = 0
                    # lógica para tecla seta para cima
                    elif event.key == K_UP:
                        if op_selected > 0:
                            op_selected -= 1
                        else:
                            op_selected = len(MENU_OPTION) - 1
                    # lógica para tecla enter
                    elif event.key == K_RETURN:
                        return MENU_OPTION[op_selected]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center)
        self.window.blit(source=text_surf, dest=text_rect)
