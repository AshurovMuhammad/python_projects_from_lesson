from shape import rectangle, cylinder, circle
# from rectangle import Rectangle
# from circle import Circle


class Cylinder(rectangle.Rectangle, circle.Circle):
    def __init__(self, tomon1, radius):
        super().__init__(tomon1, radius)
        self.tomon1 = tomon1
        self.radius = radius

    def obyem(self):
        return 3.14 * self.radius ** 2 * self.tomon1

