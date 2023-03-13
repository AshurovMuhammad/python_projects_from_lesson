import os.path
import pickle


class Auto:
    def __init__(self, brand, name, engine, color):
        self.brand = brand
        self.name = name
        self.engine = engine
        self.color = color

    def __str__(self):
        return f"{self.brand} ({self.name})"


class AutoModel:
    def __init__(self):
        self.db_name = "db_autos.txt"
        self.autos = self.load_data()

    def add_auto(self, dict_auto):
        auto = Auto(*dict_auto.values())
        self.autos[auto.brand] = auto

    def get_all_autos(self):
        return self.autos.values()

    def get_single_auto(self, user_request):
        auto = self.autos[user_request]
        dict_auto = {
            "brand": auto.brand,
            "nomi": auto.name,
            "dvigatel kuchi": auto.engine,
            "rangi": auto.color
        }
        return dict_auto

    def remove_auto(self, user_request):
        return self.autos.pop(user_request)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.autos, f)


