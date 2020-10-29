from random import randrange
from game_types import Position, Size


def snake_is_out_of_bounds(snake_position: Position, display_size: Size):
    (x, y) = snake_position
    (width, height) = display_size
    if (0 <= x < width) and (0 <= y < height):
        return False
    return True


def generate_random_square(display_size: Size, square_size: int) -> Position:
    return (
        randrange(0, int(display_size[0] / square_size)) * square_size,
        randrange(0, int(display_size[1] / square_size)) * square_size,
    )