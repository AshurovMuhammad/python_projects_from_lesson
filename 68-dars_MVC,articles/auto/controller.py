from view import View
from model import AutoModel


class Controller:
    def __init__(self):
        self.model = AutoModel()
        self.view = View()

    def run(self):
        answer = None
        while answer != "q":
            answer = self.view.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            auto = self.view.add_user_auto()
            self.model.add_auto(auto)
        elif answer == "2":
            autos = self.model.get_all_autos()
            self.view.show_all_autos(autos)
        elif answer == "3":
            auto_name = self.view.get_user_auto()
            try:
                auto = self.model.get_single_auto(auto_name)
            except KeyError:
                self.view.show_incorrect_user_request(auto_name)
            else:
                self.view.show_single_auto(auto)
        elif answer == "4":
            auto_name = self.view.get_user_auto()
            try:
                brand = self.model.remove_auto(auto_name)
            except KeyError:
                self.view.show_incorrect_user_request(auto_name)
            else:
                self.view.remove_single_auto(brand)
        elif answer == "q":
            self.model.save_data()
        else:
            self.view.show_incorrect_answer_error(answer)

