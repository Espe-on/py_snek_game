from game_settings import GameSettings
from game_utils import snake_is_out_of_bounds


def game_loop(game_board, display, game_settings: GameSettings):
    display_width = game_settings.display_width;
    display_height = game_settings.display_height;
    pixel = game_settings.pixel_size
    colors = game_settings.colours;

    snake_position = game_settings.starting_position
    snake_position_change = [0, 0]

    clock = game_board.time.Clock()
    game_running = True;

    while game_running:
        for event in game_board.event.get():
            if event.type == game_board.QUIT:
                game_running = False;
            if event.type == game_board.KEYDOWN:
                if event.key == game_board.K_LEFT:
                    snake_position_change = [-pixel, 0]
                elif event.key == game_board.K_RIGHT:
                    snake_position_change = [pixel, 0]
                elif event.key == game_board.K_UP:
                    snake_position_change = [0, -pixel]
                elif event.key == game_board.K_DOWN:
                    snake_position_change = [0, pixel]
        snake_position= [x + y for x, y in zip(snake_position, snake_position_change)]

        display.fill(colors.background)

        game_board.draw.rect(display, colors.main, [snake_position[0], snake_position[1], pixel, pixel]);
        game_board.display.update();

        clock.tick(20)
        print(f"position:\nx={snake_position[0]}\ny={snake_position[1]}")
        print(f"Snake out of bounds:{snake_is_out_of_bounds(snake_position[0], snake_position[1], display_width, display_height)}")

    game_board.quit();
    quit();
