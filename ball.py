from typing import Union
from pygame.math import Vector2
from block import Block
from paddle import Paddle
import pygame as pg
import random
import os


class Ball:
    '''Ball object'''

    directions = {
        'bottom': (0, 1),
        'top': (0, -1),
        'left': (-1, 0),
        'right': (1, 0),
    }
    collision_border = 10

    def __init__(self, x: float, y: float, r: float,
                 v: float = 3, start_direction: tuple = (),
                 color: str = '#02ccfe'):
        self.radius = r
        self.velocity = v
        if start_direction == ():
            # Making sure that none of dirctions is 0
            while not start_direction or 0 in start_direction:
                # Changing random seed to get different
                #   directions in one programm run
                random.seed(os.urandom(10))
                start_direction = (random.uniform(-0.9, 0.9),
                                   random.uniform(0.3, 0.9))

        self.direction = pg.math.Vector2(start_direction).normalize()
        self.color = pg.Color(color)
        self.rect = pg.Rect(x - r, y - r, 2*r, 2*r)

    def draw(self, screen: pg.Surface) -> None:
        '''Draws ball'''
        pg.draw.circle(screen, self.color, self.rect.center, self.radius)

    def game_over(self, screen_height: int) -> bool:
        '''Returns true if ball is outside of the screen'''
        return self.rect.top >= screen_height + 2*self.radius

    def reflect(self, new_direction: tuple):
        '''Changes ball's direction to given'''
        self.direction = self.direction.reflect(Vector2(new_direction))

    def update(self) -> None:
        '''Updates ball's position after movement'''
        self.rect.center += self.direction * self.velocity

    def collide_other(self, other: Union[Block, Paddle]):
        '''Makes ball to collide with paddle and blocks'''
        if self.rect.colliderect(other.rect):
            # If given object is block, reduce its lifetime
            if isinstance(other, Block):
                other.collided()

            # Check if collision was on bottom of the ball
            if (abs(other.rect.top - self.rect.bottom) <
                self.collision_border
               and self.direction.y > 0):
                self.reflect(self.directions.get('top'))
            # Check if collision was on top of the ball
            elif (abs(other.rect.bottom - self.rect.top) <
                  self.collision_border
                  and self.direction.y < 0):
                self.reflect(self.directions.get('bottom'))
            # Check if collision was on left of the ball
            elif (abs(other.rect.right - self.rect.left) <
                  self.collision_border
                  and self.direction.x < 0):
                self.reflect(self.directions.get('right'))
            # Check if collision was on right of the ball
            elif (abs(other.rect.left - self.rect.right) <
                  self.collision_border
                  and self.direction.x > 0):
                self.reflect(self.directions.get('left'))

    def collide_walls(self, screen_borders: dict[str, int]):
        '''Makes ball not to go out of the borders'''
        if self.rect.left <= screen_borders.get('left'):
            self.rect.x = screen_borders.get('left')
            self.reflect(self.directions.get('right'))
        elif self.rect.top <= screen_borders.get('top'):
            self.rect.y = screen_borders.get('top')
            self.reflect(self.directions.get('bottom'))
        elif self.rect.right >= screen_borders.get('right'):
            self.rect.right = screen_borders.get('right')
            self.reflect(self.directions.get('left'))
