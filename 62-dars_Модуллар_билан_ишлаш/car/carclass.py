class CarClass:
    def __init__(self, brand, model, year, probeg):
        self.brand = brand
        self.model = model
        self.year = year
        self.probeg = probeg

    def show_car(self):
        print(f"{self.brand}, {self.brand}, {self.year}-yil, {self.probeg} km")


if __name__ == "__main__":
    e = CarClass("Tesla", "Y-500", 2018, 2100)
    e.show_car()
