from openpyxl import Workbook
from openpyxl.styles import Font

wb = Workbook()
ws = wb.active

b2 = ws["B2"]
b2.value = "York"
bold_red_font = Font(bold=True, color="FF0000")
b2.font = bold_red_font

b3 = ws["B3"]
b3.value = "Fish"
italic_strike_blue_16font = Font(size=16, italic=True, strike=True, color="0000FF")
b3.font = italic_strike_blue_16font

wb.save(r"D:\04_demo.xlsx")

