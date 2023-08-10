import json
import datetime
from getId import *
def addNote():
    while(True):
        title = input("Введите, пожалуйста, заголовок Вашей заметки: ")
        if (title.replace(" ","") == ""):
            print("Пустой заголовок")
        else: break
    while(True):
        msg = input("Введите, пожалуйста, содержание Вашей заметки: ")
        if (msg.replace(" ","") == ""):
            print("Пустое содержание заметки!")
        else: break 
    id = getId()
    date = str (datetime.datetime.today().replace(microsecond=0))
    new_data = {'id': id, 'title': title, 'msg': msg, 'date': date}
    with open('notepad.json', encoding='utf-8') as w:
        data = json.load(w)
        data.append(new_data)
        with open('notepad.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)
    print(f'Поздравляю, Ваша заметка, с id-{id}, успешно добавлена в блокнот!')
    