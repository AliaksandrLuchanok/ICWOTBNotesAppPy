from jsonToList import*
# функция, которая генерирует уникальные id заметкам блокнота
def getId(): 
   id = 0
   notepad = getListFromJson()
   if notepad!=[]:
          id = max([int(notepad[i]['id']) for i in range(len(notepad))]) + 1
   return id

