class Snake:
    def __init__(self, position: (int, int), pixel):
        self.head_position = position
        self.tail = []
        self.direction = (0, 0)
        self._pixel = pixel
        self.direction_left = (-self._pixel, 0)
        self.direction_right = (+self._pixel, 0)
        self.direction_up = (0, -self._pixel)
        self.direction_down = (0, +self._pixel)

    def move_left(self):
        self.direction = self.direction_left
    def move_right(self):
        self.direction = self.direction_right

    def move_up(self):
        self.direction = self.direction_up

    def move_down(self):
        self.direction = self.direction_down

    def resolve_position(self, score):
        self.tail.append(self.head_position)
        if len(self.tail) > score:
            self.tail.pop(0)

        self.head_position = (
            self.head_position[0] + self.direction[0],
            self.head_position[1] + self.direction[1],
        )

    def is_eating_itself(self):
        return self.head_position in self.tail
