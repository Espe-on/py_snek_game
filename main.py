"""
Snek
"""

import pygame

from game import game_loop
from game_objects.game_settings import GameSettings

pygame.init()
game_settings = GameSettings()
display = pygame.display.set_mode(
    game_settings.display_size,
)

pygame.display.set_caption("Py_Snek_Game")

game_loop(display, game_settings)
