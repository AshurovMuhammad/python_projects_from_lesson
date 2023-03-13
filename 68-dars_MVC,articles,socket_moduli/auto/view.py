def add_title(title):
    def wrapper(class_func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = class_func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap
    return wrapper


class View:
    @add_title("Foydalanuvchi sahifasi")
    def wait_user_answer(self):
        print("Avtomobillar bilan ishlash:")
        print("1 - avtomobil qo'shish\n"
              "2 - avtomobillarni ko'rish\n"
              "3 - kerakli avtomobilni ko'rish\n"
              "4 - avtomobilni o'chirish\n"
              "q - dasturni to'xtatish")
        user_answer = input("Menyuni tanlang: ")
        return user_answer

    @add_title("Avtomobil qo'shish")
    def add_user_auto(self):
        dict_autos = {
            "brend": None,
            "nomi": None,
            "dvigatel kuchi": None,
            "rangi": None
        }
        for key in dict_autos:
            dict_autos[key] = input(f"Avtomobil {key}ni kiriting: ")
        return dict_autos

    @add_title("Avtomobillar ro'yxati")
    def show_all_autos(self, autos):
        for ind, auto in enumerate(autos, 1):
            print(f"{ind}. {auto}")

    @add_title("Avtomobil brendni kiritish")
    def get_user_auto(self):
        user_auto = input("Avtomobil brendni kiitng: ")
        return user_auto

    @add_title("Avtomobil haqida ma'lumot")
    def show_single_auto(self, auto):
        for k, v in auto.items():
            print(f"{k} - {v}")

    @add_title("Ma'lumot kiritishda xatolik")
    def show_incorrect_user_request(self, user_request):
        print(f"{user_request.title()} bunday brendegi avtomobil mavjud emas")

    @add_title("Bazadan ma'lumotni o'chirish")
    def remove_single_auto(self, brand_name):
        print(f"{brand_name} avtomobil bazadan o'chirildi!")

    @add_title("Hatolik haqida habar")
    def show_incorrect_answer_error(self, answer):
        print(f"{answer} bunday menyu mavjud emas!")