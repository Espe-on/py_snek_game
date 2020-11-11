from game_types import Position, Tail


class Snake:
    def __init__(self, position: Position, pixel_size: int):
        self.orig_position: Position = position
        self.head_position: Position = position
        self.tail: Tail = []
        self.direction: Position = (0, 0)
        self._pixel = pixel_size
        self.direction_left: Position = (-self._pixel, 0)
        self.direction_right: Position = (+self._pixel, 0)
        self.direction_up: Position = (0, -self._pixel)
        self.direction_down: Position = (0, +self._pixel)

    def move_left(self):
        self.direction = self.direction_left

    def move_right(self):
        self.direction = self.direction_right

    def move_up(self):
        self.direction = self.direction_up

    def move_down(self):
        self.direction = self.direction_down

    def resolve_position(self, score: int):
        self.tail.append(self.head_position)
        if len(self.tail) > score:
            self.tail.pop(0)

        head_x, head_y = self.head_position
        direction_x, direction_y = self.direction

        self.head_position = (
            head_x + direction_x,
            head_y + direction_y,
        )

    def is_eating_itself(self):
        return self.head_position in self.tail

    def reset(self):
        self.head_position = self.orig_position
        self.direction = (0, 0)
        self.tail = []