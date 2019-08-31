import openpyxl

wb = openpyxl.load_workbook(r"D:\03_demo.xlsx")     # 载入一个工作簿

ws = wb.active                                      # 获取工作表
# ws.freeze_panes = "A1"                              # 解冻，即以 A1 为参考点
ws.freeze_panes = None                              # 解冻的另一种方法

wb.save(r"D:\03_demo.xlsx")                         # 保存文件，此步需在文件关闭时操作

