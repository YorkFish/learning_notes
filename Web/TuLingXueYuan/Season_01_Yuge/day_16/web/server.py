from http.server import HTTPServer, CGIHTTPRequestHandler  

port = 8080 # 端口号
httpd = HTTPServer(('', port), CGIHTTPRequestHandler) # (('默认是本机的 IP 地址 LocalHost/127.0.0.1', 端口号), CGI 响应初识程序的包)
print("Starting simple_httpd on port: " + str(httpd.server_port)) # 输出所使用的端口号
httpd.serve_forever()
