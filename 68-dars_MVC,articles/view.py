def add_title(title):
    def wrapper(class_func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = class_func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_title("Foydalanuvchi haqida ma'lumot")
    def wait_user_answer(self):
        print("Maqolalar bilan ishlash:")
        print("1 - maqola qo'shish"
              "\n2 - maqolalarni ko'rish"
              "\n3 - maqolani alohida holda ko'rish"
              "\n4 - maqolani o'chirish"
              "\nq - dasturdan chiqish uchun")
        user_answer = input("Menu ni tanlang: ")
        return user_answer

    @add_title("Maqola qo'shish")
    def add_user_articles(self):
        dict_article = {
            "sarlavhasi": None,
            "muallif": None,
            "sahifalar soni": None,
            "description": None
        }
        for key in dict_article:
            dict_article[key] = input(f"Maqola {key}ni kiriting: ")
        return dict_article

    @add_title("Maqolalar ro'yxati")
    def show_all_articles(self, articles):
        for ind, article in enumerate(articles, 1):
            print(f"{ind}. {article}")

    @add_title("Maqola nomini kiritish")
    def get_user_article(self):
        user_article = input("Maqola nomini kiriting: ")
        return user_article

    @add_title("Maqolani ko'rish")
    def show_single_article(self, article):
        for key in article:
            print(f"Maqola {key} - {article[key]}")

    @add_title("Kiritilgan ma'lumotda hatolik")
    def show_incorrect_title_error(self, article_title):
        print(f"{article_title} bunday maqola bazada mavjud emas!")

    @add_title("Maqolani o'chirish")
    def remove_single_article(self, article):
        print(f"{article} maqola o'chirildi")

    @add_title("Malumot kiritishda xatolik")
    def show_incorrect_answer_error(self, answer):
        print(f"{answer} ushbu raqam orqali malumot mavjud emas!")
