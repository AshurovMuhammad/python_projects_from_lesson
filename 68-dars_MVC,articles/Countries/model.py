import os.path
import pickle


class Country:
    def __init__(self, name, capital, population, language):
        self.name = name
        self.capital = capital
        self.population = population
        self.language = language

    def __str__(self):
        return f"{self.name} - ({self.capital})"


class CountryModel:
    def __init__(self):
        self.db_name = "db_countries.txt"
        self.countries = self.load_data()

    def save_country(self, dict_country):
        country = Country(*dict_country.values())
        self.countries[country.name] = country

    def get_all_countries(self):
        return self.countries.values()

    def get_single_country(self, user_request):
        country = self.countries[user_request]
        dict_country = {
            "name": country.name,
            "capital": country.capital,
            "population": country.population,
            "language": country.language
        }
        return dict_country

    def remove_country(self, user_request):
        return self.countries.pop(user_request)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.countries, f)
