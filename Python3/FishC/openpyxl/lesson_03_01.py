import openpyxl

wb = openpyxl.Workbook()                    # 实例化一个工作簿
ws1 = wb.create_sheet(title="YorkFish1")    # 创建工作表
ws2 = wb.create_sheet(title="YorkFish2")    # 创建工作表
ws3 = wb.create_sheet(title="YorkFish3")    # 创建工作表

ws1.sheet_properties.tabColor = "FF0000"    # red
ws2.sheet_properties.tabColor = "00FF00"    # green
ws3.sheet_properties.tabColor = "0000FF"    # blue

wb.save(r"D:\03_demo.xlsx")                 # 保存文件，此步需在文件关闭时操作

