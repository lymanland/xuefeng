#!/usr/bin/env python
# -*- coding: utf-8 -*-

#导入socket库:
import socket
import time, threading

#创建一个基于IPv4和TCP协议的Socket：
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'create socket'

#请注意，小于1024的端口号必须要有管理员权限才能绑定：
# 监听端口:
s.bind(('127.0.0.1', 1025))
print 'bind'

#开始监听端口，传入的参数指定等待连接的最大数量：
s.listen(5)
print 'Waiting for connection...'

def tcplink(sock, addr):
 	#print 'Accept new connection from %s:%s...' %addr
 	#
    sock.send('-------------')
    print addr
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr

#通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

