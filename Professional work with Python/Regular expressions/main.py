import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
new_list = [contacts_list[0]]
phone_pattern = r"(\+7|8)?\s*\(?(\d{3})\)?(-|\s*|)(\d{3})(-|\s*|)(\d{2})(-|\s*|)(\d{2})\s*\(?(\w+\.)?\s*(\d+)?\)?"
substitution = r"+7(\2)\4-\6-\8 \9\10"

# Исправление данных
for a in contacts_list[1:]:
    # Разделение ФИО
    fio = list(" ".join(a[:3]).strip().split(" "))
    person_info = ['', '', '']
    for i in range(3):
        try:
            person_info[i] = fio[i]
        except IndexError:
            pass

    # Перенос информации
    person_info.append(a[3])
    person_info.append(a[4])

    # Телефон
    person_info.append(re.sub(phone_pattern, substitution, a[5]).strip())

    # Перенос информации
    person_info.append(a[6])

    new_list.append(person_info)

# объединение дубликатов по последней записи
for i in range(1, len(new_list) - 1):
    for j in range(i + 1, len(new_list) - 1):
        if new_list[i][0] == new_list[j][0] and new_list[i][1] == new_list[j][1]:
            if new_list[i][2] != new_list[j][2] and new_list[i][2] != '' and new_list[j][2] != '':
                break
            elif new_list[i][2] == '': new_list[i][2] = new_list[j][2]
            if new_list[j][3] != '':
                new_list[i][3] = new_list[j][3]
            if new_list[j][4] != '':
                new_list[i][4] = new_list[j][4]
            if new_list[j][5] != '':
                new_list[i][5] = new_list[j][5]
            if new_list[j][6] != '':
                new_list[i][6] = new_list[j][6]
            new_list.pop(j)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(new_list)