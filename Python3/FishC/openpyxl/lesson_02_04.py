import openpyxl

wb = openpyxl.load_workbook(r"D:\02_demo.xlsx")             # 传入路径，实例化一个工作簿

ws = wb["Sheet1"]

c = ws["A2"]
print(c.row)                                                # 2
print(c.column)                                             # A
print(c.coordinate)                                         # A2

print(ws["A2"].value)                                       # 若对应的各自内有信息，则返回那个信息，否则，返回 None
print(c.value)                                              # 同上

print(openpyxl.cell.cell.get_column_letter(496))            # SB
print(openpyxl.cell.cell.column_index_from_string("JB"))    # 262

wb.save(r"D:\02_demo.xlsx")

