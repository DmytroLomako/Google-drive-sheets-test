from .settings import *

def read_table(service, id, range):
    sheet = service.spreadsheets()
    value = sheet.values().get(spreadsheetId = id, range = range).execute()
    return value['values']