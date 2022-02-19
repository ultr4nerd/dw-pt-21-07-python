"""
Vector

<2, 3> + <4, 5> = <6, 8>
3 * <2, 4> = <6, 12>
"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __rmul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        return Vector(x, y)

    def __str__(self):
        return f"<{self.x}, {self.y}>"
