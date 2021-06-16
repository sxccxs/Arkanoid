import pygame as pg


class Paddle:
    '''Paddle object which is controlable by player'''

    def __init__(self, x: float, y: float, w: float,
                 h: float, v: float = 3, color: str = '#d0d0d0'):
        self.width = w
        self.height = h
        self.velocity = v
        self.color = pg.Color(color)
        self.rect = pg.Rect(x, y, w, h)

    def draw(self, screen: pg.Surface) -> None:
        '''Draws paddle'''
        pg.draw.rect(screen, self.color, self.rect)

    def reflect_velocity(self) -> None:
        '''Makes paddle to go other way than it did before'''
        self.velocity *= -1

    def pos_velocity(self) -> None:
        '''Makes paddle to go right'''
        self.velocity = abs(self.velocity)

    def neg_velocity(self) -> None:
        '''Makes paddle to go left'''
        self.velocity = -1 * abs(self.velocity)

    def update(self) -> None:
        '''Updates paddle's position after movement'''
        self.rect.left += self.velocity

    def collide_walls(self, screen_borders: dict[str, int]) -> None:
        '''Makes paddle not to go out of the borders'''
        if self.rect.left <= screen_borders.get('left'):
            self.rect.x = screen_borders.get('left')
            self.reflect_velocity()
        elif self.rect.right >= screen_borders.get('right'):
            self.rect.right = screen_borders.get('right')
            self.reflect_velocity()
