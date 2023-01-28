from openpyxl import Workbook
import os

def data_to_excel_convert(data: list, output_path: str) -> None:
    wb = Workbook()
    ws = wb.active

    i = 1
    j = 1
    for entry in data:
        if entry.is_negative == True:
            i += entry.print(ws, 65, i)
            
        else:
            j += entry.print(ws, 75, j)

    file_path = f'{output_path}/Resumen_Contable.xlsx'
    wb.save(file_path)
    os.system(file_path)

