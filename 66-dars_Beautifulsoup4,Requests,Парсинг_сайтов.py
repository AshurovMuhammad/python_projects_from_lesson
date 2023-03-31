# Параллельное и многопаточное программирование. Парсинг сайтов  // 41 // 69
# Parsing bu biror-bir saytdan malumot olish.
# pip install beautifulsoup4 or bs4

# Beautifulsoupda 2ta parser mavjud
# 1) html.parser
# 2) lxml -> ushbu parserdan foydalanish uchun uni o'rnatib olishimiz kerek (pip install lxml)

from bs4 import BeautifulSoup
import re
import requests
import csv


# f = open('index.html').read()  # Agar rus tilida yozilgan shriftlarni o'qimasa encoding="utf-8" atributini qo'llemz
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find("div", class_="name")  # find-birinchi topgan elementni qaytaradi
# row = soup.find_all("div", class_="name")  # find_all-topgan barcha elementni qaytaradi
# row = soup.find_all("div", class_="row")[1].find("div", class_="links")
# row = soup.find("div", {"data-set": "salary"})
# print(row)

# alena = soup.find("div", text="Alena").parent.parent
# alena = soup.find("div", text="Alena").find_parent(class_="row")
# print(alena)

# with_id = soup.find("div", id="whois3")  # id orqali topadi
# with_id = soup.find("div", id="whois3").find_next_sibling()  # qidirilayotgan divdan bitta kegingi divni topadi
# with_id = soup.find("div", id="whois3").find_previous_sibling()  # qidirilayotgan divdan bitta oldingi divni topadi
# print(with_id)


# def get_copywriter(tag):
#     whois = tag.find("div", class_="whois")
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# copywriter = []
# row = soup.find_all("div", class_="row")
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)


# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find_all("div", {"data-set": "salary"})
# for i in row:
#     get_salary(i.text)


# requests bilan ishlash

# r = requests.get("https://ru.wordpress.org/")
# print(r.status_code)
# print(r.headers)
# print(r.headers["Content-Type"])


# r = requests.get("https://ru.wordpress.org/")
# # print(r.content)
# print(r.text)


# worldPress saytidan ma'lumot olish
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "html.parser")
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))
#
#
# if __name__ == "__main__":
#     main()


# 531 775
# worldPress saytidan ma'lumot olib csv faylga yozib beradi
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(rtng):
#     res = re.sub(r"\D+", "", rtng)
#     return res
#
#
# def write_csv(data):
#     with open("plugins.csv", "a") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((data["name"], data["url"], data["rating"]))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "html.parser")
#     s = soup.find_all("section", class_="plugin-section")[1]
#     plugins = s.find_all("article")
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         url = plugin.find("h3").find("a").get("href")
#         rating = plugin.find("span", class_="rating-count").find("a").text
#         r = refined(rating)
#
#         data = {"name": name, "url": url, "rating": r}
#         write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == "__main__":
#     main()


# Home Work
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def write_csv(data):
#     with open("news.csv", "a") as f:  # encoding="utf-8"
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((data["title"], data["time"], data["url"]))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "html.parser")
#     start = soup.find("div", class_="top-news__small-items")
#     plugins = start.find_all("div", class_="col-md-6")
#     for plugin in plugins:
#         title = plugin.find("a", class_="small-news__title").text
#         link = 'https://kun.uz/' + plugin.find("a", class_="small-news__img").get("href")
#         time = plugin.find("span").text
#         # print(f"{title} - {time}. Link: {link}")
#         data = {"title": title, "time": time, "url": link}
#         write_csv(data)
#
#
# def main():
#     url = "https://kun.uz/uz/"
#     get_data(get_html(url))
#
#
# if __name__ == "__main__":
#     main()

print("Hello")