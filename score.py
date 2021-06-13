import pygame as pg
from pygame.math import Vector2


class Score:
    '''Score Text object'''

    def __init__(self, x: float, y: float,
                 font: str, font_size: str, color: str = '#000000'):
        self.position = Vector2(x, y)
        self.color = pg.Color(color)
        self.font = pg.font.SysFont(font, font_size)

    def draw(self, screen: pg.Surface, score: int):
        ''' Draws score text on given screen with given value'''
        text = self.font.render(f'Score: {score}', True, self.color)
        screen.blit(text, self.position)
