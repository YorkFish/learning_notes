import datetime, os, openpyxl

os.chdir("D:\\")
wb = openpyxl.Workbook()            # 实例化一个工作簿
ws = wb.active                      # 获取工作表
print(ws.title)                     # 输出：Sheet；此为工作表的 title

ws["A1"] = 520                      # 将 520 赋值给 A1
ws.append([1, 2, 3])                # 将 [1, 2, 3] 添加至下一行
ws["A3"] = datetime.datetime.now()  # 获取当前时间，并赋值
wb.save("demo.xlsx")                # 将文件保存为 demo.xlsx

