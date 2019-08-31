import openpyxl

wb = openpyxl.load_workbook(r"D:\02_demo.xlsx")     # 传入路径，实例化一个工作簿

nws = wb.create_sheet(index=0, title="YorkFish")
print(wb.sheetnames)                                # ['YorkFish', 'Sheet1', 'Sheet2', 'Sheet3']

wb.save(r"D:\02_demo.xlsx")

