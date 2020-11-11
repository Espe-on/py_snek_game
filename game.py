import pygame
from pygame import Color, Rect, Surface
from pygame.constants import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN
from pygame.font import Font

from game_objects.food import Food
from game_objects.game_settings import GameSettings
from game_objects.snake import Snake
from utils.game_utils import snake_is_out_of_bounds


def game_loop(display: Surface, game_settings: GameSettings):
    display_size = game_settings.display_size
    pixel_size = game_settings.pixel_size
    colors = game_settings.colours
    font_style_large = Font(None, 50)
    font_style_small = Font(None, 25)

    snake = Snake(game_settings.starting_position, pixel_size)
    food = Food(display_size, pixel_size)
    clock = pygame.time.Clock()
    game_running = True
    intro = True
    crashed = False
    playing = False
    score = 0

    def handle_event():
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT and not (
                    snake.direction == snake.direction_right
                ):
                    snake.move_left()

                elif event.key == K_RIGHT and not (
                    snake.direction == snake.direction_left
                ):
                    snake.move_right()

                elif event.key == K_UP and not (
                    snake.direction == snake.direction_down
                ):
                    snake.move_up()

                elif event.key == K_DOWN and not (
                    snake.direction == snake.direction_up
                ):
                    snake.move_down()

    def wait(ms: int):
        waiting = True
        while waiting:
            handle_event()

            ms -= clock.tick(120)
            if ms <= 0:
                waiting = False

    def message(msg: str, color: Color, font: Font):
        text = font.render(msg, False, color)
        text_rect = text.get_rect()
        text_rect.center = game_settings.starting_position

        return text, text_rect

    def display_message(msg: str, color: Color, font: Font):
        display.fill(colors.background)
        pygame.display.update()
        print(f"displaying {msg}")
        text, text_rect = message(msg, color, font)
        pygame.draw.rect(
            display,
            Color(128, 0, 128),
            text_rect,
        )
        display.blit(text, text_rect)
        wait(2000)

    def draw_score():
        score_text, score_text_rect = message(
            f"{score}", Color(40, 40, 40), font_style_large
        )
        display.blit(score_text, score_text_rect)

    # This section is the game intro screen
    while game_running:
        if intro:
            display_message("SNAKE!", colors.main, font_style_large)
            intro = False
            playing = True

        handle_event()

        if playing:
            if food.position == snake.head_position:
                score = score + 1
                food.move_food(snake.tail)

            snake.resolve_position(score)

            if snake_is_out_of_bounds(snake.head_position, display_size):
                crashed = True

            if snake.is_eating_itself():
                crashed = True

            # Logging
            print(
                f"Snake Position: x={snake.head_position[0]}, y={snake.head_position[1]}"
            )
            print(f"Food Position: x={food.position[0]}, y={food.position[1]}")
            print(f"Score: {score}")
            if food.position == snake.head_position:
                print("Snake is on food!")
            if snake_is_out_of_bounds(snake.head_position, display_size):
                print("Snake out of bounds:")

            # Rendering Game
            display.fill(colors.background)
            draw_score()

            pygame.draw.rect(
                display,
                colors.highlight,
                [food.position[0], food.position[1], pixel_size, pixel_size],
            )
            pygame.draw.rect(
                display,
                colors.main,
                Rect(
                    snake.head_position,
                    (pixel_size, pixel_size),
                ),
            )
            for tail_position in snake.tail:
                pygame.draw.rect(
                    display,
                    colors.main,
                    [tail_position[0], tail_position[1], pixel_size, pixel_size],
                )

            clock.tick(10)

        if crashed:
            # Rendering Lost Screen
            # print("LOST, rendering lost message")
            # display_message("You Lost", colors.highlight, font_style_large)

            # print("rendering score")
            playing = False
            display_message(f"FAIL", colors.highlight, font_style_large)
            display_message(f"Score: {score}", colors.highlight, font_style_small)
            snake.reset()
            score = 0
            crashed = False
            playing = True

        pygame.display.update()

    pygame.quit()
    quit()
