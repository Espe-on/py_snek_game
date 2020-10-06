import pygame as game_board;
from game_settings import colors, board_width, board_height, pixel_width, pixel_height;

game_board.init();
display = game_board.display.set_mode((board_width, board_height));
game_board.display.update();
game_board.display.set_caption("Py_Snek_Game");

game_running = True;

while game_running:
    for event in game_board.event.get():
        if event.type == game_board.QUIT:
            game_running = False;
        game_board.draw.rect(display, colors["main"], [int(board_width/2), int(board_height/2), pixel_width, pixel_height]);
        game_board.display.update();
        print(event);

game_board.quit();
quit();
