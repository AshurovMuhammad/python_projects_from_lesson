class Circle:
    def __init__(self, radius):
        self.radius = radius

    def dlina_okrujnosti(self):
        return 2 * 3.14 * self.radius

    def ploshad_kroga(self):
        return 3.14 * (self.radius) ** 2

    def __str__(self):
        return f"{self.radius}"
