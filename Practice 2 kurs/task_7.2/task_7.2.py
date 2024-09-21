def main(path_to_file_read: str, path_to_file_write: str) -> None:
    import datetime
    import time
    import lxml
    import requests as req
    from bs4 import BeautifulSoup

    req = req.get("https://2ip.ru/")

    soup = BeautifulSoup(req.text, "lxml")

    city, county = soup.find("div", id="ip-info-country").text.split()[:2]

    provaider = soup.find("div", class_="value value-custom").text.strip()

    with open(path_to_file_read, "r", encoding="utf-8") as file_read, \
        open("file_log.txt", "w", encoding="utf-8") as file_log:

        list_rows = file_read.readlines()

        for i in range(len(list_rows)):
            if i % 2 == 1:
                list_rows[i] = list_rows[i].upper()

        with open(path_to_file_write, "w", encoding="utf-8") as file_write:
            for row in list_rows:
                file_write.write(row)
                file_log.write(f"""Записалась строка: "{row.strip()}". 
                Время: {datetime.datetime.now()}. 
                Город: {city}.
                Страна: {county}.
                Провайдер: {provaider}\n\n""")

main("file_input.txt", "file_output.txt")