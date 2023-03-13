class Rectangle:
    def __init__(self, tomon1, tomon2):
        self.tomon1 = tomon1
        self.tomon2 = tomon2

    def peimetr(self):
        return 2 * (self.tomon1 + self.tomon2)

    def ploshad(self):
        return self.tomon2 * self.tomon1

    def storoni(self):
        return self.tomon1, self.tomon2
