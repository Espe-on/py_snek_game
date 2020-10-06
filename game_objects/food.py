from utils.game_utils import generate_random_square


class Food:
    def __init__(self, display_size, square_size):
        self.position = generate_random_square(display_size, square_size)
        self._display_size = display_size
        self._square_size = square_size

    def move_food(self):
        self.position = generate_random_square(self._display_size, self._square_size)
