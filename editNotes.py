from jsonToList import*
from printNotepad import*
from jsonToList import*
from outInJsonData import*
import datetime
def editNotes(useData):
    useActionTitle = useCommand("заголовок")
    if useActionTitle == "1":
        title = notEmpty("заголовок")
        for i in range(len(useData)):
            useData[i]['title'] = title
    printNotepad(useData)
    useActionMsg = useCommand("сообщение")    
    if useActionMsg == "1":
        msg = notEmpty("сообщение")
        for i in range(len(useData)):
            useData[i]['msg'] = msg
    printNotepad(useData)
    if(useActionTitle != "" or useActionMsg != ""):
        for i in range(len(useData)):
            useData[i]['date'] = str (datetime.datetime.today().replace(microsecond=0))
        notepad = getListFromJson()
        idEditElement = set([(i['id']) for i in useData])
        minimal = 0
        for i in range(len(notepad)):
           if notepad[i]['id'] in idEditElement:
               notepad[i] = useData[minimal]
               minimal += 1
           else:
              None
        outInJsonData(notepad)
        print("Ваши данные успешно изменены:")
        printNotepad(useData)
    else:
        print("Никаких изменений в искомые данные не внесено! ")


# осуществляет проверку на пустую строку
def notEmpty(nameField):
    data = input (f'Введите {nameField}\n')
    if data.replace(" ","") == "":
        print(f'Ваши данные пустые, повторите ввод данных в {nameField}!\n')
        return notEmpty(nameField)
    return data

# принимает на вход имя и выводит пользователю интерфейс взаимодействия
def useCommand(nameField):
    useCommand = input (f'внести изменение в {nameField}, введите цифру --->> 1\n'
                        f'оставить без изменений, нажмите            --->> Enter\n').replace(" ","")
    return useCommand

