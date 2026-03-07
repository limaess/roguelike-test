import pygame as pg
import random as r

from rogueliketestClasses import *
from rogueliketestItems import *

pg.init()

def drawtext(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

font = pg.font.SysFont('Arial', 30)

screen = pg.display.set_mode((1920, 1080))
clock = pg.time.Clock()

isActive = True
while isActive:
    dt = clock.tick(75) // 1000
    screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    keys = pg.key.get_just_pressed()

    if keys[pg.K_q]:
        waveHandler.endWave()


    drawtext(waveHandler.currentWaveType, font, (255,255,255), 0,0)
    drawtext(f'next element: {waveTypes[1]}', font, (255,255,255), 100,0)

    pg.display.flip()

pg.quit()