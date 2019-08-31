import openpyxl
from openpyxl.styles.colors import RED, GREEN, BLUE, YELLOW

wb = openpyxl.load_workbook(r"D:\05_demo.xlsx")
ws = wb["Sheet"]

ws["A7"].number_format = "[RED]+#,###.00;[GREEN]-#,###.00"
ws["A7"] = 99

ws["A8"].number_format = "[RED]+#,###.00;[GREEN]-#,###.00"
ws["A8"] = -99

ws["A9"].number_format = "[RED];[GREEN];[BLUE];[YELLOW]"
ws["A9"] = 0

ws["A10"].number_format = "[RED];[GREEN];[BLUE];[YELLOW]"
ws["A10"] = "YorkFish"

ws["A11"].number_format = "[=1]男;[=0]女"
ws["A11"] = 0

ws["A12"].number_format = "[=1]男;[=0]女"
ws["A12"] = 1

ws["A13"].number_format = "[=1]男;[=0]女"
ws["A13"] = 2   # 规则改了，之前是返回 ###...；现在非零即为真

ws["A14"].number_format = "[<60][RED]不及格;[>=60][GREEN]及格" # 显示文字，编辑时显示数字
ws["A14"] = 59

ws["A15"].number_format = "[<60][RED]不及格;[>=60][GREEN]及格"
ws["A15"] = 60

wb.save(r"D:\05_demo.xlsx")

