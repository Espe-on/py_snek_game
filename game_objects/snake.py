class Snake:
    def __init__(self, position: (int, int), pixel):
        self.head_position = position
        self.tail = []
        self.direction = (0, 0)
        self._pixel = pixel

    def move_left(self):
        self.direction = (-self._pixel, 0)

    def move_right(self):
        self.direction = (+self._pixel, 0)

    def move_up(self):
        self.direction = (0, -self._pixel)

    def move_down(self):
        self.direction = (0, +self._pixel)

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

