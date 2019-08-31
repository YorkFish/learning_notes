import openpyxl

wb = openpyxl.load_workbook(r"D:\02_demo.xlsx")     # 传入路径，实例化一个工作簿

ws = wb["Sheet1"]

new = wb.copy_worksheet(ws)
print(type(new))                                    # <class 'openpyxl.worksheet.worksheet.Worksheet'>

wb.save(r"D:\02_demo.xlsx")

