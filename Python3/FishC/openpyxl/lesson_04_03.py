import openpyxl
from openpyxl.styles import GradientFill

wb = openpyxl.load_workbook(r"D:\04_demo.xlsx")
ws = wb["Sheet"]
c2 = ws["C2"]

red2green_fill = GradientFill(type="linear", stop=("FF0000", "0000FF")) # fill_type="linear" 线性 （fill_type 改成了 type）
                                                        # type='linear', degree=0, left=0, right=0, top=0, bottom=0, stop=()
c2.fill = red2green_fill

wb.save(r"D:\04_demo.xlsx")

