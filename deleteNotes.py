from jsonToList import*
from outInJsonData import*
from printNotepad import*

def deleteNotes(useDataDelete):
    idDeleteElement = set([(i['id']) for i in useDataDelete])
    data = getListFromJson()
    minimal = 0
    dataForWrite = data.copy()
    for i in data:
           if i['id'] in idDeleteElement:
               dataForWrite.pop(minimal)
           else:
              minimal +=1 
    outInJsonData(dataForWrite)            
    print("Заметка(заметки) успешно удалена!")
    