from openpyxl import Workbook
from openpyxl.styles import Font
from data_temp import load_data

temp = load_data()

wb = Workbook()
ws = wb.active

for t in temp:
    ws.append(t)