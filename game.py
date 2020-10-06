from game_objects.game_settings import GameSettings
from game_objects.snake import Snake
from game_objects.food import Food
from utils.game_utils import snake_is_out_of_bounds


def game_loop(game_board, display, game_settings: GameSettings):
    display_size = game_settings.display_size
    pixel = game_settings.pixel_size
    colors = game_settings.colours;

    snake = Snake(game_settings.starting_position, pixel)
    food = Food(display_size, pixel)
    clock = game_board.time.Clock()
    game_running = True;

    while game_running:
        for event in game_board.event.get():
            if event.type == game_board.QUIT:
                game_running = False;
            if event.type == game_board.KEYDOWN:
                if event.key == game_board.K_LEFT:
                    snake.move_left();
                elif event.key == game_board.K_RIGHT:
                    snake.move_right();
                elif event.key == game_board.K_UP:
                    snake.move_up();
                elif event.key == game_board.K_DOWN:
                    snake.move_down();
        snake.resolve_position();

        print(f"Snake Position:\nx={snake.position[0]}\ny={snake.position[1]}")
        print(f"Food Position:\nx={food.position[0]}\ny={food.position[1]}")
        if food.position == snake.position:
            print("Snake is on food!")
        print(f"Snake out of bounds:{snake_is_out_of_bounds(snake.position, display_size)}")

        display.fill(colors.background);
        game_board.draw.rect(display, colors.highlight, [food.position[0], food.position[1], pixel, pixel])
        game_board.draw.rect(display, colors.main, [snake.position[0], snake.position[1], pixel, pixel]);
        game_board.display.update();

        clock.tick(1)


    game_board.quit();
    quit();
