def printNotepad(list):
    for i in list:         
         print(f'id:{i["id"]}; ' 
               f'title:{i["title"]}; '
               f'msg:{i["msg"]}; '
               f'date:{i["date"]}; '
               )