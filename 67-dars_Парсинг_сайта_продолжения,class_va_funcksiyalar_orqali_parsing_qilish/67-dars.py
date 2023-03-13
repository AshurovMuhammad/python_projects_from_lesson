# Парсинг сайтов. Продолжения. Протокол HTTP/HTTPS  42  //  67

from bs4 import BeautifulSoup
import re
import requests
import csv

# Bazaviy shablon
# def get_html(url):
#     res = requests.get(url)  # binar element qaytadi
#     return res.text  # sahifa kodi qanday bo'lsa shu ko'rinishda consolga chiqarib beradi
#
#
# def get_page_data(html):
#     soup = BeautifulSoup(html, "lxml")  # html.parser
#
#
# def main():
#     url = "https://example.com"
#     get_page_data(get_html(url))
#
#
# if __name__ == "__main__":
#     main()


# def get_html(url):
#     res = requests.get(url)  # binar element qaytadi
#     return res.text  # sahifa kodi qanday bo'lsa shu ko'rinishda consolga chiqarib beradi
#
#
# def write_csv(data):
#     with open("plugin1.csv", "a", encoding="utf-8") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((
#             data["name"],
#             data["url"],
#             data["snippet"],
#             data["active"],
#             data["cy"]
#         ))
#
#
# def refine_cy(s):
#     return s.split(" ")[-1]
#
#
# def get_page_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     elements = soup.find_all("article", class_="plugin-card")
#     for el in elements:
#         try:
#             name = el.find("h3").text
#         except ValueError:
#             name = ""
#
#         try:
#             url = el.find("h3").find("a").get("href")
#         except ValueError:
#             url = ""
#
#         try:
#             snippet = el.find("div", class_="entry-excerpt").text.strip()
#         except ValueError:
#             snippet = ""
#
#         try:
#             active = el.find("span", class_="active-installs").text.strip()
#         except ValueError:
#             active = ""
#
#         try:
#             version = el.find("span", class_="tested-with").text.strip()
#             cy = refine_cy(version)
#         except ValueError:
#             cy = ""
#
#         data = {
#             "name": name,
#             "url": url,
#             "snippet": snippet,
#             "active": active,
#             "cy": cy
#         }
#
#         write_csv(data)
#
#         # print(f"Title: {name}\nURL: {url}\nSnippet: {snippet}\nActive: {active}\nVersion: {cy}\n")
#
#
# def main():
#     for i in range(22, 26):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_page_data(get_html(url))
#
#
# if __name__ == "__main__":
#     main()
#
# # https://ru.wordpress.org/plugins/browse/blocks/page/1/
# # https://ru.wordpress.org/plugins/browse/blocks/page/2/
# # https://ru.wordpress.org/plugins/browse/blocks/page/3/


# from parse import Parser
# Quyidegi saytdan ma'lumotlarni olamiz
# https://www.ixbt.com/live/index/news/
# def main():
#     pars = Parser(f"https://www.ixbt.com/live/index/news/", "news_ixbt.txt")
#     pars.run()
#
#
# if __name__ == "__main__":
#     main()


# Home Work
# from parse import ParserCamera
#
#
# # Olxdan yangiliklarni olamiz
# def main():
#     pars = ParserCamera("https://www.olx.uz/d/oz/elektronika/foto-video/", "olx_news.txt")
#     pars.get_html()
#     pars.parsing()
#
#
# if __name__ == "__main__":
#     main()


# Olx dan malumotlarni olib text lista yozib beradi
# from parse import ParserCamera
#
#
# def main():
#     pars = ParserCamera("https://www.olx.uz/d/oz/elektronika/foto-video/", "olx_news.txt")
#     pars.run()
#
#
# if __name__ == "__main__":
#     main()


# Parser qilish uchun shablon
# class ExampleParser:
#     html = ""
#     res = []
#
#     def __init__(self, url, path):
#         self.url = url
#         self.path = path
#
#     def get_html(self):
#         req = requests.get(self.url).text
#         self.html = BeautifulSoup(req, "lxml")
#
#     def parsing(self):
#         pass
#
#     def run(self):
#         self.get_html()
#
#
# def main():
#     pass
#
#
# if __name__ == "__main__":
#     main()


