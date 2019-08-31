import openpyxl

wb = openpyxl.load_workbook(r"D:\02_demo.xlsx")     # 传入路径，实例化一个工作簿

# wb.remove_sheet("YorkFish")                         # 已经废弃 官方推荐 wb.remove(worksheet) or del wb[sheetname]
wb.remove(wb["YorkFish"])
del wb["Sheet1"]
print(wb.sheetnames)                                # ['Sheet2', 'Sheet3']

wb.save(r"D:\02_demo.xlsx")

