import openpyxl

wb = openpyxl.load_workbook(r"D:\02_demo.xlsx")             # 传入路径，实例化一个工作簿

ws = wb["Sheet1"]

# 有数据的话，可以使用如下 code
# for each_movie in ws["A2":"B10"]:
#     for each_cell in each_movie:
#         print(each_cell.value, end=' ')

# for each_row in ws.rows:
#     print(each_row[0].value)

# for each_row in ws.iter_rows(min_row=2, min_col=1, max_row=4, max_col=2):
#     print(each_row[0].value)

wb.save(r"D:\02_demo.xlsx")

