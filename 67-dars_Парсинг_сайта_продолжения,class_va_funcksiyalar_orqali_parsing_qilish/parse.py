import re
import requests
from bs4 import BeautifulSoup


# class Parser:
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
#         news = self.html.find_all("div", class_="caption")
#         for item in news:
#             title = item.find("h3").text
#             href = item.find("a").get("href")
#             author = item.find("a", class_="topic-info-author-link").text.strip()
#             self.res.append({
#                 "title": title,
#                 "href": href,
#                 "author": author
#             })
#
#     def save_data(self):
#         with open(self.path, "w", encoding="utf-8") as f:
#             i = 1
#             for item in self.res:
#                 f.write(f"Yangilik №-{i}\n\nNomi: {item['title']}\nLink: {item['href']}\nMuallif: {item['author']}"
#                         f"\n\n{'*' * 20}\n")
#                 i += 1
#
#     def run(self):
#         self.get_html()
#         self.parsing()
#         self.save_data()


# Home work


# Olx dan malumotlarni olib text lista yozib beradi
# class ParserCamera:
#     html = ""
#     res = []
#
#     def __init__(self, url, file_name):
#         self.url = url
#         self.file_name = file_name
#
#     def get_html(self):
#         req = requests.get(self.url).text
#         self.html = BeautifulSoup(req, "lxml")
#
#     def parsing(self):
#         news = self.html.find_all("div", class_="css-1apmciz")
#         for item in news:
#             name = item.find("h6").text
#             price = item.find("p").text.strip()
#             self.res.append({
#                 "name": name,
#                 "price": price
#             })
#
#     def save_data(self):
#         with open(self.file_name, "w", encoding="utf-8") as f:
#             i = 1
#             for item in self.res:
#                 f.write(f"Product number №-{i}\n\nProduct name: {item['name']}\nProduct price: {item['price']}"
#                         f"\n\n{'*' * 20}\n")
#                 i += 1
#
#     def run(self):
#         self.get_html()
#         self.parsing()
#         self.save_data()
