from openpyxl import load_workbook

wb = load_workbook(r"D:\06_demo.xlsx")
ws = wb["Sheet"]

#                   (待查对象，查询范围，基准列，FALSE 精准查找 TRUE 模糊查找)
ws["M3"] = "=VLOOKUP(L3, A:F, 6, FALSE)"

wb.save(r"D:\06_demo.xlsx")

