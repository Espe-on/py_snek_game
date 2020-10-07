class GameColors:
    def __init__(
        self,
        main: tuple = (255, 0, 0),
        background: tuple = (0, 0, 0),
        highlight: tuple = (255, 0, 255),
    ):

        self.main = main
        self.background = background
        self.highlight = highlight


class GameSettings:
    def __init__(
        self,
        display_width: int = 300,
        display_height: int = 300,
        pixel_size: int = 10,
        colors: GameColors = GameColors(),
    ):
        self.display_size = (display_width, display_height)
        self.starting_position = (int(display_width / 2), int(display_height / 2))
        self.pixel_size = pixel_size
        self.colours = colors
