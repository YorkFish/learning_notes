import openpyxl
from openpyxl.styles import Border, Side

wb = openpyxl.load_workbook(r"D:\04_demo.xlsx")
ws = wb["Sheet"]
b4 = ws["B4"]
c4 = ws["C4"]

thin_side = Side(border_style="thin", color="000000")
double_side = Side(border_style="double", color="FF0000")

b4.border = Border(diagonal=thin_side, diagonalUp=True, diagonalDown=True)
c4.border = Border(left=double_side, top=double_side, right=double_side, bottom=double_side)

wb.save(r"D:\04_demo.xlsx")

