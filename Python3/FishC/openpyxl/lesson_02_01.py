import openpyxl

wb = openpyxl.load_workbook(r"D:\02_demo.xlsx")     # 传入路径，实例化一个工作簿
print(type(wb))                                     # <class 'openpyxl.workbook.workbook.Workbook'>

# print(wb.get_sheet_names())                         # ['Sheet1', 'Sheet2', 'Sheet3'] 目前还能使用，但相当于是废弃
print(wb.sheetnames)                                # ['Sheet1', 'Sheet2', 'Sheet3'] 官方推荐这种方法

# ws = wb.get_sheet_by_name('Sheet1')                 # 已经废弃
# error = wb.get_sheet_by_name("YorkFish")            # 已经废弃
ws = wb["Sheet1"]
# error = wb["YorkFish"]                              # KeyError: ...

wb.save(r"D:\02_demo.xlsx")

