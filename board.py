from paddle import Paddle
from ball import Ball
from block import Block
from score import Score
import pygame as pg


class Board:
    '''Main game screen which contains all other objects on game scene'''

    def __init__(self, w: int, h: int, paddle: Paddle,
                 ball: Ball, blocks: list[Block], scoreText: Score,
                 image_name: str, screen_borders: dict[str, int]):
        self.screen = pg.display.set_mode((w, h))
        self.paddle = paddle
        self.ball = ball
        self.blocks = blocks
        self.scoreText = scoreText
        self.score = 0
        self.need_restart = False
        self.screen_borders = screen_borders
        self.bg_image = pg.image.load(image_name)

    def draw_blocks(self) -> None:
        '''Draws all blocks to the screen'''
        for block in self.blocks:
            block.draw(self.screen)

    def ball_collision(self) -> None:
        '''Call all colliding logic of the ball with blocks,
            paddle, screen borders'''

        # Check if ball collides with each block and
        #   delete block from the list if its lifetime is 0
        for block in self.blocks:
            self.ball.collide_other(block)
            if not block.lifetime:
                self.blocks.remove(block)
                self.score += 1

        # Check collisions with paddle and screen borders
        self.ball.collide_other(self.paddle)
        self.ball.collide_walls(self.screen_borders)

    def update(self) -> None:
        '''Draws background and updates all objects values'''
        if not self.ball.game_over(self.screen.get_height()):

            # Drawing background
            w, h = self.screen.get_size()
            x_step, y_step = self.bg_image.get_size()
            for y in range(0, h+1, y_step):
                for x in range(0, w+1, x_step):
                    self.screen.blit(self.bg_image, (x, y))

            # drawing blocks
            self.draw_blocks()

            # drawing ball
            self.ball.draw(self.screen)
            self.ball.update()
            self.ball_collision()

            # drawing paddle
            self.paddle.draw(self.screen)
            self.paddle.update()
            self.paddle.collide_walls(self.screen_borders)

            # drawing score text
            self.scoreText.draw(self.screen, self.score)
        else:
            self.need_restart = True
