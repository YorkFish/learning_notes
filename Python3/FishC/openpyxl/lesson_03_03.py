import openpyxl

wb = openpyxl.load_workbook(r"D:\03_demo.xlsx")     # 载入一个工作簿

ws1 = wb["YorkFish1"]
ws1.merge_cells("A1:C3")
ws1["A1"] = "Now, They are integrated!"

# ws1.unmerge_cells("A1:C2")                  # 此时会报错
ws1.unmerge_cells("A1:C3")                  # 当初怎么拆的，现在就怎么恢复，那句话仍然在 A1

wb.save(r"D:\03_demo.xlsx")                 # 保存文件，此步需在文件关闭时操作

