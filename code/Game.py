import pygame

from code.Menu import Menu
from code.const import WINDOW_HEIGHT, WIN_WIDTH


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WINDOW_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

    def atualiza_tela(self):
        pass

    def processa_eventos(self):
        pass
