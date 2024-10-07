from .settings import *
import pandas

def save_data(value: list, file_type: list, path_to_save: str):
    data_frame = pandas.DataFrame(value[1:], columns = value[0])
    if 'csv' in file_type:
        data_frame.to_csv(f'{path_to_save}/file.csv', index = False)
    elif 'excel' in file_type:
        data_frame.to_excel(f'{path_to_save}/file.excel', index = True)
    elif 'html' in file_type:
        data_frame.to_html(f'{path_to_save}/file.html', index = True)
    