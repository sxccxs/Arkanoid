import pygame as pg


class Block:
    '''Block objects'''

    colors = {
        1: '#00ff12',
        2: '#f0ff00',
        3: '#ff0000',
    }

    def __init__(self, x: float, y: float, w: float,
                 h: float, lifetime: int = 1):
        self.width = w
        self.height = h
        self.lifetime = lifetime
        self.rect = pg.Rect(x, y, self.width, self.height)

    def get_color(self) -> pg.Color:
        '''Returns block's color depending on the lifetime'''
        return pg.Color(self.colors.get(self.lifetime))

    def draw(self, screen: pg.Surface) -> None:
        '''Draws block if lifetime is bigger then 0'''
        if self.lifetime:
            pg.draw.rect(screen, self.get_color(), self.rect)
        else:
            self.rect = pg.Rect(-1, -1, 0, 0)

    def collided(self):
        '''Reduces lifetime after collision'''
        self.lifetime -= 1
