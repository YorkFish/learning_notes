from openpyxl import load_workbook

wb = load_workbook(r"D:\06_demo.xlsx")
ws = wb["Sheet"]

#                  (待查询的值，查询范围，结果出现范围)
ws["J3"] = "=LOOKUP(I3, C3:C6, A3:A6)"

wb.save(r"D:\06_demo.xlsx")

