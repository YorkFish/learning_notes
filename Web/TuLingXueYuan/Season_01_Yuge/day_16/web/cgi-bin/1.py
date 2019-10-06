import cgi, cgitb, json, time
cgitb.enable()

# 给浏览器看的一个 HTTP 的响应报文，告诉浏览器，给它返回的是一个 HTML 文件，此为固定格式
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers  

fs = cgi.FieldStorage()             # 接收用户提交过来的数据
inputs = {}                         # 数据重组
for key in fs.keys():
    inputs[key] = fs[key].value

# print(inputs)						# 给用户返回数据
# 会返回这样的数据："GET /01_ajax.html HTTP/1.1" 200 -
# 释义：请求方式 GET，请求对象 01_ajax.html，HTTP 版本号 HTTP/1.1，状态码 200

# print('1')							# 若不发送 inputs，可以这样表示接收到请求

# time.sleep(3);						# 设置时间，模拟 ajax 请求数据超时，进入 error 函数

# 转换成 json 格式的数据
print(json.dumps(inputs))
# print(json.dumps([1,2,3]))
# print(inputs);
# print(fs,inputs);
# print('sucess')
