import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

ws.append(["文本", "数字"])
ws["A2"] = "520"
ws["B2"] = 520

wb.save(r"D:\05_demo.xlsx")

