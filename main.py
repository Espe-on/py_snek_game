import pygame as game_board

game_board.init()
display = game_board.display.set_mode((400, 300))
game_board.display.update()
game_board.display.set_caption("Py_Snek_Game")

game_running = True

while game_running:
    for event in game_board.event.get():
        if event.type == game_board.QUIT:
            game_running = False
        print(event)

game_board.quit()
quit()
