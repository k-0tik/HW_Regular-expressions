import re

from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
new_contacts_list = []

phone_pattern = r"(\+7|8)?\s*\((\d{3,5})\)\s*(\d{1,3})[-\s]?(\d{2})[-\s]?(\d{2})(\s\(?"'доб'"\.\s\d{3,5}\)?)?"
replacement_phone_pattern = r"8-\2-\3-\4-\5\6"


for row in contacts_list:
    lastname = row[0]
    firstname = row[1]
    surname = row[2]
    if lastname:
        new_lastname = lastname.split(" ")[0]
    if firstname:
        new_firstname = firstname.split(" ")[0]
    elif len(lastname.split(" ")) > 1:
        new_firstname = lastname.split(" ")[1]
    else:
        new_firstname = ''
    if surname:
        new_surname = surname.split(" ")[0]
    elif len(firstname.split(" ")) > 1:
        new_surname = firstname.split(" ")[1]
    elif len(lastname.split(" ")) > 2:
        new_surname = lastname.split(" ")[2]
    else:
        new_surname = ''
    organization = row[3]
    position = row[4]
    phone = row[5]
    cleaned_phones = re.sub(phone_pattern, replacement_phone_pattern, phone)
    email = row[6]
    data = [new_lastname, new_firstname, new_surname, organization, position, cleaned_phones, email]
    new_contacts_list.append(data)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_contacts_list)