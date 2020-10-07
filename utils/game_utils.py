import random


def snake_is_out_of_bounds(snake_position: (int, int), display_size: (int, int)):
    if (0 < snake_position[0] < display_size[0]) and (
        0 < snake_position[1] < display_size[1]
    ):
        return False
    return True


def generate_random_square(display_size: (int, int), square_size: (int, int)):
    return (
        round(random.randrange(0, display_size[0] - square_size) / square_size)
        * square_size,
        round(random.randrange(0, display_size[1] - square_size) / square_size)
        * square_size,
    )
