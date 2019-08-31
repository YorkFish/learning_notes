import openpyxl
from openpyxl.styles import PatternFill

wb = openpyxl.load_workbook(r"D:\04_demo.xlsx")
ws = wb["Sheet"]
b2 = ws["B2"]

yellow_fill = PatternFill(fill_type="solid", fgColor="FFFF00") # fgColor: 背景颜色；bgColor: 图案颜色
b2.fill = yellow_fill

wb.save(r"D:\04_demo.xlsx")

