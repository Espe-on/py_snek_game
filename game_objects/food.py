from random import randint
from utils.game_utils import generate_random_square

class Food:
    def __init__(self, display_size, square_size):
        self.position = generate_random_square(display_size, square_size)

    def move_food(self, display_size, square_size):
        self.position = generate_random_square(display_size, square_size)
