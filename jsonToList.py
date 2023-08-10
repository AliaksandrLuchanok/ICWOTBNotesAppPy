import json
def getListFromJson():
      with open('notepad.json', 'r', encoding='utf-8') as f:
              data = json.load(f)
      return data