import openpyxl

wb = openpyxl.load_workbook(r"D:\03_demo.xlsx")     # 载入一个工作簿

ws1 = wb["YorkFish1"]
ws1.row_dimensions[2].height = 100
ws1.column_dimensions['C'].width = 50

wb.save(r"D:\03_demo.xlsx")                         # 保存文件，此步需在文件关闭时操作

