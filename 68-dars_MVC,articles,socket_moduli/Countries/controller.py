from view import View
from model import CountryModel


class Controller:
    def __init__(self):
        self.model = CountryModel()
        self.view = View()

    def run(self):
        answer = None
        while answer != "q":
            answer = self.view.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            country = self.view.add_country()
            self.model.save_country(country)
        elif answer == "2":
            countries = self.model.get_all_countries()
            self.view.show_all_countries(countries)
        elif answer == "3":
            country_name = self.view.get_user_request()
            try:
                dict_country = self.model.get_single_country(country_name)
            except KeyError:
                self.view.show_incorrect_user_request(country_name)
            else:
                self.view.show_single_country(dict_country)
        elif answer == "4":
            country_name = self.view.get_user_request()
            try:
                name = self.model.remove_country(country_name)
            except KeyError:
                self.view.show_incorrect_user_request(country_name)
            else:
                self.view.show_remove_country(name)
        elif answer == "q":
            self.model.save_data()
        else:
            self.view.show_incorrect_answer_error(answer)
