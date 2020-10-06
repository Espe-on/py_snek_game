from game_settings import GameSettings
from game_utils import snake_is_out_of_bounds

def game_loop(game_board, display, game_settings:GameSettings):
    display_width = game_settings.display_width;
    display_height = game_settings.display_height;
    pixel = game_settings.pixel_size
    colors = game_settings.colours;

    snake_x = game_settings.starting_position[0]
    snake_y = game_settings.starting_position[1]
    snake_x_change = 0
    snake_y_change = 0

    clock = game_board.time.Clock()
    game_running = True;

    while game_running:
        for event in game_board.event.get():
            if event.type == game_board.QUIT:
                game_running = False;
            if event.type == game_board.KEYDOWN:
                if event.key == game_board.K_LEFT:
                    snake_x_change = -pixel;
                    snake_y_change = 0;
                elif event.key == game_board.K_RIGHT:
                    snake_x_change = pixel;
                    snake_y_change = 0;
                elif event.key == game_board.K_UP:
                    snake_x_change = 0;
                    snake_y_change = -pixel;
                elif event.key == game_board.K_DOWN:
                    snake_x_change = 0;
                    snake_y_change = pixel;
        snake_x += snake_x_change
        snake_y += snake_y_change
        if snake_x < 0:
            snake_x = display_width
        elif snake_x > display_width:
            snake_x = 0

        display.fill(colors.background)

        game_board.draw.rect(display, colors.main, [snake_x, snake_y, pixel, pixel]);
        game_board.display.update();

        clock.tick(20)
        print(f"position:\nx={snake_x}\ny={snake_y}")
        print(snake_is_out_of_bounds(snake_x, snake_y, display_width, display_height))

    game_board.quit();
    quit();