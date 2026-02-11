from __future__ import annotations
import math

# task 3

BORDER_X = 1920
BORDER_Y = 1080

class Coord:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def __str__(self):
        return (f"({self.__x},{self.__y})")

    def get_x(self) -> int:
        return self.__x

    def set_x(self, new_x: int) -> None:
        self.__x = new_x

    def get_y(self) -> int:
        return self.__y

    def set_y(self, new_y: int) -> None:
        self.__y = new_y



class ModelWindow:
    heading: str
    upper_left_corner: Coord
    horizontal_size: int
    vertical_size: int
    color: str
    is_visible: bool
    has_frame: bool

    def __init__(self, heading: str, upper_left_corner: Coord, horizontal_size: int, vertical_size: int, color: str, is_visible: bool, has_frame:  bool):
        self.__heading = heading
        self.__upper_left_corner = upper_left_corner
        self.__vertical_size = vertical_size
        self.__horizontal_size = horizontal_size
        self.__color = color
        self.__is_visible = is_visible
        self.__has_frame = has_frame

    def __str__(self):
        return (f"heading: {self.__heading}\n"
                f"upper left corner: {self.__upper_left_corner}\n"
                f"horizontal: {self.__horizontal_size}\n"
                f"vertical: {self.__vertical_size}\n"
                f"color: {self.__color}\n"
                f"is visible: {self.__is_visible}\n"
                f"has : {self.__has_frame}\n")

    def move_x(self, shift: int) -> None:
        new_x = self.__upper_left_corner.get_x() + shift

        if new_x > (self.__upper_left_corner.get_x() + self.__horizontal_size):
            raise ValueError

        self.__upper_left_corner.set_x(shift + self.__upper_left_corner.get_x())

    def move_y(self, shift: int) -> None:
        new_x = self.__upper_left_corner.get_y() + shift

        if new_x > (self.__upper_left_corner.get_y() + self.__horizontal_size):
            raise ValueError

        self.__upper_left_corner.set_y(shift + self.__upper_left_corner.get_y())


    def set_vertical(self, new_vertical_size: int) -> None:
            if (new_vertical_size + self.get_upper_left_corner().y) > BORDER_Y:
                raise ValueError

            self.__vertical_size = new_vertical_size

    def set_horizontal(self, new_horizontal_size) -> None:
        if (new_horizontal_size + self.__upper_left_corner.get_y()) > BORDER_X:
            raise ValueError

        self.__horizontal_size = new_horizontal_size

    def set_color(self, new_color) -> None:
        self.__color = new_color

    def set_is_visible(self, new_condition: bool) -> None:
        self.__is_visible = new_condition

    def set_has_frame(self, new_condition: bool) -> None:
        self.__has_frame = new_condition


    def get_heading(self) -> str:
        return self.__heading

    def get_upper_left_corner(self) -> Coord:
        return self.__upper_left_corner

    def get_horizon_size(self) -> int:
        return self.__horizontal_size

    def get_vertical_size(self) -> int:
        return self.__vertical_size

    def get_is_visible(self) -> bool:
        return self.__is_visible

    def get_has_frame(self) -> bool:
        return self.__has_frame

game = ModelWindow("Игра", Coord(3,6), 800, 500, "red", True, True)

game.move_x(200)
game.move_y(200)
print(game)


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
        x = self.x - right.x
        y = self.y - right.y
        z = self.z - right.z

        return Vector(x,y,z)

    def __mul__(self, right: Vector | float):
        if type(right) == Vector:
            x = (self.y * right.z) - (self.z * right.y)
            y = (self.z * right.x) - (self.x * right.z)
            z = (self.x * right.y) - (self.y * right.x)

            return Vector(x,y,z)

        x = self.x * right
        y = self.y * right
        z = self.z * right

        return Vector(x,y,z)

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)


vector1 = Vector(3,1,6)
vector2 = Vector(4,3,8)

print(vector1 + vector2)
print(vector1 - vector2)
print(vector1 * vector2)
print(vector1 * 5)
print(vector1.length())
print(f"{vector1} {vector2}")
