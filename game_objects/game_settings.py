from pygame import Color
from game_types import Size


class GameColors:
    def __init__(
        self,
        main: Color = Color(255, 0, 0),
        background: Color = Color(0, 0, 0),
        highlight: Color = Color(255, 0, 255),
    ):

        self.main = main
        self.background = background
        self.highlight = highlight


class GameSettings:
    def __init__(
        self,
        display_size: Size = (300, 300),
        pixel_size: int = 10,
        colors: GameColors = GameColors(),
    ):
        width, height = display_size
        self.display_size = display_size
        self.starting_position = (int(width / 2), int(height / 2))
        self.pixel_size = pixel_size
        self.colours = colors
