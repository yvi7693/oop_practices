from __future__ import annotations

# task 3

BORDER_X = 1920
BORDER_Y = 1080

class Coord:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return (f"x: {self.x}"
                f"y: {self.y}")


class ModelWindow:
    heading: str
    upper_left_corner: Coord
    horizontal_size: int
    vertical_size: int
    color: str
    is_visible: bool
    has_frame: bool

    def __init__(self, heading: str, upper_left_corner: Coord, horizontal_size: int, vertical_size: int, color: str, is_visible: bool, has_frame:  bool):
        self.heading = heading
        self.upper_left_corner = upper_left_corner
        self.vertical_size = vertical_size
        self.horizontal_size = horizontal_size
        self.color = color
        self.is_visible = is_visible
        self.has_frame = has_frame

    def __str__(self):
        return (f"heading: {self.heading}"
                f"upper left corner: {self.upper_left_corner}"
                f"horizontal: {self.horizontal_size}"
                f"vertical: {self.vertical_size}"
                f"color: {self.color}"
                f"is visible: {self.is_visible}"
                f"has frame: {self.has_frame}")

    def move_x(self, shift: int) -> None:
        new_x = self.upper_left_corner.x + shift

        if new_x > (self.upper_left_corner.x + self.horizontal_size):
            raise ValueError

        self.upper_left_corner.x += shift

    def move_y(self, shift: int) -> None:
        new_y = self.upper_left_corner.y + shift

        if new_y > (self.upper_left_corner.y + self.vertical_size):
            raise ValueError

        self.upper_left_corner.y += shift


    def set_vertical(self, new_vertical_size: int) -> None:
        if (new_vertical_size + self.upper_left_corner.y) > BORDER_Y:
            raise ValueError

        self.vertical_size = new_vertical_size

    def set_horizontal(self, new_horizontal_size) -> None:
        if (new_horizontal_size + self.upper_left_corner.y) > BORDER_X:
            raise ValueError

        self.horizontal_size = new_horizontal_size

    def set_color(self, new_color) -> None:
        self.color = new_color

    def set_is_visible(self, new_condition: bool) -> None:
        self.is_visible = new_condition

    def set_has_frame(self, new_condition: bool) -> None:
        self.has_frame = new_condition


    def get_heading(self) -> str:
        return self.heading

    def get_upper_left_corner(self) -> Coord:
        return self.upper_left_corner

    def get_horizon_size(self) -> int:
        return self.horizontal_size

    def get_vertical_size(self) -> int:
        return self.vertical_size

    def get_is_visible(self) -> bool:
        return self.is_visible

    def get_has_frame(self) -> bool:
        return self.has_frame


# task 5

class Vector:
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, right: Vector):
        x = self.x + right.x
        y = self.y + right.y
        z = self.z + right.z

        return Vector(x,y,z)

    def __sub__(self, right: Vector):
        x = self.x + right.x
        y = self.y + right.y
        z = self.z + right.z

        return Vector(x,y,z)

    def __mul__(self, right: Vector):
        x = self.x * right.x
        y = self.y * right.y
        z = self.z * right.z

        return Vector(x,y,z)










