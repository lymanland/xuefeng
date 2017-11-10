#coding=utf-8
# 导入socket库:
import socket

print 'create socket'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接:
print 'connect socket'
s.connect(('127.0.0.1', 1025))

# 接收欢迎消息:
print 'begin recv\n'
print s.recv(1024)
for data in ['Michael', 'Tracy', 'Sarah']:
    # 发送数据:
    s.send(data)
    print s.recv(1024)
s.send('exit')
s.close()