from openpyxl import load_workbook
from openpyxl.styles import Alignment

wb = load_workbook(r"D:\06_demo.xlsx")
ws = wb["Sheet"]

center_alignment = Alignment(horizontal="center")
for row in ws.iter_rows(min_col=3, min_row=3, max_col=8, max_row=6):        # 注意坐标
    # ws[row[4].coordinate] = "=IF(%s>250, 'A', 'B')" % (row[4].coordinate)   # excel 不认单引号
    ws[row[4].coordinate] = '=IF(%s>250, "A", "B")' % (row[3].coordinate)   # 条件表达式
    ws[row[4].coordinate].alignment = center_alignment                      # 单元格居中

wb.save(r"D:\06_demo.xlsx")

