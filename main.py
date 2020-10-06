import pygame as game_board;
from game_settings import GameSettings
from game import game_loop

game_board.init();
game_settings = GameSettings();
display = game_board.display.set_mode((game_settings.display_width, game_settings.display_height));
game_board.display.set_caption("Py_Snek_Game");

game_loop(game_board, display, game_settings);
