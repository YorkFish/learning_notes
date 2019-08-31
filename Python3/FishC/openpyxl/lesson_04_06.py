import openpyxl
from openpyxl.styles import Alignment, Font, NamedStyle

wb = openpyxl.load_workbook(r"D:\04_demo.xlsx")
ws = wb["Sheet"]

hightlight = NamedStyle(name="hightlight")
hightlight.font = Font(bold=True, size=20)
hightlight.alignment = Alignment(horizontal="center", vertical="center")

# wb.add_named_style(hightlight)  # 第一次使用，样式的名称存储在它们的本地化表单中，后面就不用重复添加了

ws["B7"].value = "YorkFish"
# ws["B7"].style = hightlight # 第一次使用
ws["B7"].style = "hightlight"   # 第二次及以后使用

wb.save(r"D:\04_demo.xlsx")

