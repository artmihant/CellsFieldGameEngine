import itertools

import numpy as np
import pygame as pg
from pygame.locals import QUIT
from random import randint

class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    CYAN = (0, 255, 255)
    MAGNETA = (255, 0, 255)
    YELLOW = (255, 255, 0)

    GRAY = (128, 128, 128)

    BROWN = (128, 0, 0)
    DARKGREEN = (0, 128, 0)
    DARKBLUE = (0, 0, 128)

    DARKCYAN = (0, 128, 128)
    DARKMAGNETA = (128, 0, 128)
    SWARM = (128, 128, 0)

    LIGHTRED = (255, 128, 128)
    LIGHTGREEN = (128, 255, 128)
    LIGHTBLUE = (128, 128, 255)


    LIGHTCYAN = (128, 255, 255)
    LIGHTMAGNETA = (255, 128, 255)
    LIGHTYELLOW = (255, 255, 128)

    SKY = (0, 128, 255)
    SEA = (0, 255, 128)

    PURPLE = (128, 0, 255)
    GRASS = (128, 255, 0)

    PINK = (255, 0, 128)
    ORANGE = (255, 128, 0)

EVENTKEYS = {
    pg.K_LEFT : 'left',
    pg.K_RIGHT: 'right',
    pg.K_UP: 'up',
    pg.K_DOWN: 'down',
    pg.K_SPACE: 'space',
    pg.K_PAGEDOWN: 'pagedown',
    pg.K_PAGEUP: 'pageup',
}


class State:
    def __init__(self, width=10, height=10, interval=0):
        self.interval = interval
        self.height = height
        self.width = width
        self.field = np.zeros((width, height), dtype=int)
        self.prevfield = np.zeros((width, height), dtype=int)

    def randomcell(self):
        return randint(0, self.width - 1), randint(0, self.height - 1)

    @property
    def range(self):
        return itertools.product(range(self.width), range(self.height))


class Game:
    cells = [{
        'name': 'empty',
        'color': Color.WHITE,
        'alt': None # TODO сделать так, что бы альт выводился на клетке
    }]

    grid = {
        'view': True,
        'color': Color.BLACK
    }

    cellsize = 10
    fps = 60

    interval = 1000

    state = {}

    def __init__(self, width=100, height=100):

        self.width = width
        self.height = height
        self.ticks = pg.time.get_ticks()
        self.clock = pg.time.Clock()
        self.state = State(width, height, interval = self.interval)

    def add_cell(self, name, color=None, alt=None):
        if color is None:
            color = self.cells[0]['color']

        self.cells.append({'name': name, 'color': color, 'alt': alt})

    @staticmethod
    def turn(state):
        return state

    @staticmethod
    def start(state):
        return state

    @staticmethod
    def click(state, pos):
        return state

    @staticmethod
    def keydown(state, key):
        return state

    def frameupdate(self, display):
        differences = (self.state.field != self.state.prevfield)

        for index in self.state.range:
            if differences[index]:
                pg.draw.rect(display, self.cells[self.state.field[index]]['color'],
                             [index[0] * self.cellsize, index[1] * self.cellsize,
                              self.cellsize, self.cellsize])

        if self.grid['view']:
            for i in range(self.height):
                pg.draw.line(display, self.grid['color'],
                             (0, i * self.cellsize), (display.get_width(), i * self.cellsize))

            for i in range(self.width):
                pg.draw.line(display, self.grid['color'],
                             (i * self.cellsize, 0), (i * self.cellsize, display.get_height()))
        pg.display.update()

    def play(self):

        self.state.cell = {x['name']: i for i, x in enumerate(self.cells)}

        display = pg.display.set_mode((self.width * self.cellsize, self.height * self.cellsize))

        display.fill(self.cells[0]['color'])

        self.state = self.start(self.state)
        self.frameupdate(display)

        self.ticks = pg.time.get_ticks()

        while True:

            for event in pg.event.get():

                if event.type == QUIT:
                    quit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    width, height = event.pos
                    width = width // self.cellsize
                    height = height // self.cellsize
                    self.state = self.click(self.state, (width, height))
                    self.frameupdate(display)

                if event.type == pg.KEYDOWN:

                    if event.key in EVENTKEYS:
                        key = EVENTKEYS[event.key]
                    else:
                        key = event.key

                    self.state = self.keydown(self.state, key)
                    self.frameupdate(display)

            if self.state.interval is not None and \
                    pg.time.get_ticks() - self.ticks > self.state.interval:
                self.ticks = pg.time.get_ticks()

                self.state.prevfield = self.state.field.copy()
                self.state = self.turn(self.state)
                self.frameupdate(display)

            self.clock.tick(self.fps)
