from game_types import Size, Tail
from utils.game_utils import generate_random_square


class Food:
    def __init__(self, display_size: Size, square_size: int):
        self.position = generate_random_square(display_size, square_size)
        self._display_size = display_size
        self._square_size = square_size

    def move_food(self, tail: Tail):
        self.position = generate_random_square(self._display_size, self._square_size)
        while self.position in tail:
            self.position = generate_random_square(
                self._display_size, self._square_size
            )
