from openpyxl import load_workbook
from openpyxl.utils import FORMULAE

wb = load_workbook(r"D:\06_demo.xlsx")
ws = wb["Sheet"]

for row in ws.iter_rows(min_col=3, min_row=3, max_col=7, max_row=6):
    ws[row[4].coordinate] = "=SUM(%s:%s)" % (row[0].coordinate, row[2].coordinate)

# print("SUM" in FORMULAE)
# print("SAM" in FORMULAE)

wb.save(r"D:\06_demo.xlsx")

