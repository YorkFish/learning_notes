import openpyxl
from openpyxl.styles import Alignment

wb = openpyxl.load_workbook(r"D:\04_demo.xlsx")

ws = wb["Sheet"]
ws.merge_cells("A4:D6")
center_alignment = Alignment(horizontal="center", vertical="center")
ws["A4"].value = "YorkFish"
ws["A4"].alignment = center_alignment

wb.save(r"D:\04_demo.xlsx")

