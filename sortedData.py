from datetime import datetime, date
def sortedData(list):
    list.sort(key = lambda x: datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'))
