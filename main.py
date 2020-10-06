import pygame;
from game_objects.game_settings import GameSettings
from game import game_loop

pygame.init();
game_settings = GameSettings();
display = pygame.display.set_mode((game_settings.display_size[0], game_settings.display_size[1]));
pygame.display.set_caption("Py_Snek_Game");

game_loop(pygame, display, game_settings);
