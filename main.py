from modules import *

if __name__ == "__main__":
    service_drive = connect('drive', 'v3')
    id = search(service_drive, FILE_NAME)
    service_sheets = connect('sheets', 'v4')
    value = read_table(service_sheets, id, RANGE)
    path_to_save = os.path.abspath(__file__ + '/../saves')
    save_data(value, ['csv'], path_to_save)