from .settings import *

def search(service, name):
    query = f"name = '{name}'"
    file = service.files().list(q = query, spaces = 'drive', fields = 'files(id)').execute()
    return file['files'][0]['id']