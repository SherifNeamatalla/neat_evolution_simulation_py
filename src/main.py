# Import Modules
import os

import pygame as pg

from src.view.pygame.pygame_window import PyGameWindow

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "../data")

width = 1500
height = 900
title = 'NEAT Evolution Simulation'

game_window = PyGameWindow(width, height, title)

while True:
    game_window.tick()
