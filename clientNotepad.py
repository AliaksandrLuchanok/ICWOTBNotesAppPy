from getNotepad import*
from addNote import*
from searchNotes import*
from deleteNotes import*
from editNotes import*

print("Выберете операцию, которую желаете выполнить, для чего введите --->>> команду:")
while(True):
  useCommand = input(
    "-посмотреть весь блокнот заметок --->>> get\n"
    "-добавить новую заметку          --->>> add\n" 
    "-найти заметку(заметки)\n"
    "   для удаления (редактирования) --->>> search\n"   
    "-завершить работу                --->>> exit\n"        
    ).replace(" ","").lower()
  match useCommand:
    case 'get':
      getNotepad()
    case 'add':
      addNote()
    case "search":
        useListSearch = searchNotes()
        if useListSearch != []:
          useCommand = input(f'удалить результаты поиска, введите команду --->> del\n'
                             f'редактировать, введите команду             --->> edit\n'
                             f'вернуться в главное меню, нажмите          --->> Enter\n').replace(" ","").lower()
          match useCommand:
             case "del": deleteNotes(useListSearch)
             case "edit": editNotes(useListSearch)
        else:
           None
    case "exit":
        break
    case _:
        print("Вы ввели некорректную команду, пожалуйста, повторите!")


  
  

