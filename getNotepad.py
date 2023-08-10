from jsonToList import*
from printNotepad import*
from sortedData import*

def getNotepad():
   data = getListFromJson()
   if(data==[]):
      print("Я тысячекратно извиняюсь, но заметок нет!))")
   else:
      sortedData(data)
      printNotepad(data)