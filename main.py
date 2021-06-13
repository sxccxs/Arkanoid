from board import Board
from paddle import Paddle
from block import Block
from ball import Ball
from score import Score
import pygame as pg


def setup():
    '''Sets up default game scene'''
    global paddle, board, ball, score, blocks

    score = Score(BLOCK_WIDTH // 2, BLOCK_HEIGHT//10, 'Comic Sans MS', 24,
                  '#ffffff')

    ball = Ball(SCREEN_WIDTH//2 - BALL_RADIUS,
                SCREEN_HEIGHT//2 - BALL_RADIUS, BALL_RADIUS)

    paddle = Paddle(SCREEN_WIDTH//2 - PADDLE_WIDTH//2,
                    SCREEN_HEIGHT - 2*PADDLE_HEIGHT, PADDLE_WIDTH,
                    PADDLE_HEIGHT)

    blocks = []
    i = 0
    for y in range(BLOCK_HEIGHT*2, BLOCK_HEIGHT * 5 + 1,
                   BLOCK_HEIGHT + BLOCK_HEIGHT//3):
        for x in range(BLOCK_WIDTH//2, SCREEN_WIDTH - BLOCK_WIDTH//2,
                       BLOCK_WIDTH + BLOCK_WIDTH//5):
            blocks.append(Block(x, y, BLOCK_WIDTH, BLOCK_HEIGHT, 3-i))
        i += 1

    board = Board(SCREEN_WIDTH, SCREEN_HEIGHT, paddle,
                  ball, blocks, score,  r'img\board_bg.png', SCREEN_BORDERS)


pg.init()

# Setting caption text and icon
pg.display.set_caption("Arkanoid")
icon = pg.image.load(r'img\app_icon.png')
pg.display.set_icon(icon)

# Constants
SCREEN_WIDTH = 560
SCREEN_HEIGHT = 400
BLOCK_WIDTH = 40
BLOCK_HEIGHT = 20
PADDLE_WIDTH = 150
PADDLE_HEIGHT = 20
BALL_RADIUS = 10
SCREEN_BORDERS = {
    'left': BLOCK_WIDTH // 4,
    'right': SCREEN_WIDTH - BLOCK_WIDTH // 4,
    'top': BLOCK_HEIGHT
}

clock = pg.time.Clock()

setup()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                paddle.neg_velocity()
            elif event.key == pg.K_RIGHT:
                paddle.pos_velocity()
    if board.need_restart:
        setup()
    board.update()
    pg.display.update()
    clock.tick(60)
