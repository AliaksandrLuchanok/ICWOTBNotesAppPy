from printNotepad import*
from jsonToList import*


# функция поиска заметок
def searchNotes():
    notepad = getListFromJson()
    useDate = input("введите дату заметки в формате 'год-месяц-день час:минута:секунда', например:\n" 
                    "2023-08-08 18:16:56\n"                       
                    )   
    listNotepad = list(filter(lambda i: useDate in i["date"], notepad))
    if len(listNotepad) == 0:
        useCommand = input(f'Заметок с датой "{useDate}" не найдено\n'
                           f'осуществить новый поиск, введите цифру --->> 1\n'
                           f'вернуться в главное меню, нажмите      --->> Enter\n').replace(" ","")
        if useCommand == "1":
           return searchNotes()
        else: None
    else:
        printNotepad(listNotepad)
        useCommand = input(f'желаете уточнить поиск заметок, введите цифру --->> 1\n'
                           f'если нашли необходимые заметки, нажмите       --->> Enter\n').replace(" ","")
        if useCommand == "1":
            return searchNotes()
        else: None 
    return listNotepad       
