import json
def outInJsonData(useDate):
        with open('notepad.json', 'w', encoding='utf-8') as out:
          json.dump(useDate, out, ensure_ascii=False, indent=2)