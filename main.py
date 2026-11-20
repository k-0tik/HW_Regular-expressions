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

phone_pattern = r"(\+7|8)[-\s]*\(?(\d{3,5}?)\)?[-\s]*(\d{1,3})[-\s]*(\d{2})[-\s]*(\d{2})(?:([-\s])*\(?(доб\.)?\s*(\d{3,5})?)?\)?"
replacement_phone_pattern = r"+7(\2)\3-\4-\5\6\7\8"
# Попробовала сделать необязательные группы через ?(: ), так в конце ничего не добавляется


for row in contacts_list[1:]:
    fio = " ".join(row[:3]).split()
    lastname, firstname, surname = fio[0], fio[1], fio[2] if len(fio) > 2 else ''
# #  Расписала сокращенный вариант, чтобы понять что сокращается
#     for _ in fio:
#         if len(fio) > 2:
#             lastname = fio[0]
#             firstname = fio[1]
#             surname = fio[2]
#         else:
#             surname = ''
    organization = row[3]
    position = row[4]
    phone = row[5]
    cleaned_phones = re.sub(phone_pattern, replacement_phone_pattern, phone)
    email = row[6]
    data = [lastname, firstname, surname, organization, position, cleaned_phones, email]
    new_contacts_list.append(data)

# Тут нужно придумать как отфильтровать данные
    
contacts_dict = {}
    
for employee in new_contacts_list:
    if employee[0] != '' and employee[1] != '':
        full_name = (employee[0], employee[1])
    if full_name not in contacts_dict:
        contacts_dict[full_name] = employee
    else:
        old_employee = contacts_dict[full_name]
        for i in range(len(employee)):
            if old_employee[i] == '':
                old_employee[i] = employee[i]


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerow(contacts_list[0])
  datawriter.writerows(contacts_dict.values())