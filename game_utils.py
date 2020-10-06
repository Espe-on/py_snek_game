def snake_is_out_of_bounds(snake_x, snake_y, display_width, display_height):
    if (0 < snake_x < display_width) and (0 < snake_y < display_height):
        return False
    return True
