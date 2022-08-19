# DouDou_lunzi

## 所需环境

在运行远控之前需要在设备中安装一些第三方库

socket库（实现通讯）

os库（执行命令）

platform库（获取主机信息）

base64库（传输中进行加解密）

## 运行远控

实现两台客户端与服务端的通信，需要修改ip地址

server.py的ip修改为'0.0.0.0'

![image](https://user-images.githubusercontent.com/74801825/185522711-f6da667c-a1a6-430f-96f0-70c128779e87.png)

client.py的ip修改为'服务端的ip'

![image](https://user-images.githubusercontent.com/74801825/185523182-497e2a3e-f42f-4293-8834-bf182c545d78.png)

## 运行情况

![image](https://user-images.githubusercontent.com/74801825/185523778-656f42d7-b023-4447-86f6-2ad088a8a66b.png)

![image](https://user-images.githubusercontent.com/74801825/185523692-aaf327bb-5933-4454-810f-c0548918d787.png)

在连接成功时会回显系统的版本，以此判断是windows还是linux,来执行相应的命令,在现有的选项中只有对windows的命令，在查询linux可以手动去输入命令

## 小菜狗第一次写的远控，后期还会持续改进

![](https://ts3.cn.mm.bing.net/th?id=OIP-C.Cd-hqdbBwBAJTXoyR6deUwHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&dpr=1.25&pid=3.1&rm=2)
