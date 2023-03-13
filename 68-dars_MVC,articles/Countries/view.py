def add_title(title):
    def wrapper(class_func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = class_func(*args, **kwargs)
            print(50 * "=")
            return output

        return wrap

    return wrapper


class View:
    @add_title("Enter information about countries")
    def wait_user_answer(self):
        print("Actions on countries:\n"
              "1 - Add country\n"
              "2 - View countries\n"
              "3 - View a specific country\n"
              "4 - Delete country\n"
              "q - Quit the program")
        user_answer = input("Choose one of the above: ")
        return user_answer

    @add_title("Add country")
    def add_country(self):
        dict_country = {
            "name": None,
            "capital": None,
            "population": None,
            "language": None
        }
        for key in dict_country:
            dict_country[key] = input(f"Enter the {key} of the country: ")
        return dict_country

    @add_title("List of countries")
    def show_all_countries(self, countries):
        for ind, country in enumerate(countries, 1):
            print(f"{ind}. {country}")

    @add_title("Enter the name of the country")
    def get_user_request(self):
        user_request = input("Enter the name of the country: ")
        return user_request

    @add_title("View the country")
    def show_single_country(self, dict_country):
        for key in dict_country:
            print(f"Country {key} - {dict_country[key]}")

    @add_title("Data entry error")
    def show_incorrect_user_request(self, user_request):
        print(f"{user_request} does not exist in such a state base")

    @add_title("Delete country")
    def show_remove_country(self, name):
        print(f"The country named {name} has been removed from the database")

    @add_title("Data entry error")
    def show_incorrect_answer_error(self, answer):
        print(f"Error in number entry, {answer}")
