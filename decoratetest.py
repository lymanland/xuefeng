#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test 高级编程 decorate '

__author__ = 'YiJun Lee'


'''
def decorate(func):
    print('running decorate', func)
    def decorate_inner():
        print('running decorate_inner function')
        return func()
    return decorate_inner
 
@decorate
def func_1():
    print('running func_1')
 
if __name__ == '__main__':
	print(func_1)

#运行结果
#running decorate <function func_1 at 0x7f29f644d268>
#<function decorate.<locals>.decorate_inner at 0x7f29f641cb70>
'''

'''
#叠放装饰器执行顺序
def outer(func):
    print('enter outer', func)
    def wrapper():
        print('running outer')
        func()
    return wrapper
 
def inner(func):
    print('enter inner', func)
    def wrapper():
        print('running inner')
        func()
    return wrapper
 
@outer
@inner
def main():
    print('running main')

#在python中，任何具有相同缩进量的代码会被识别为一个代码块，当下一行语句与上一行的缩进量不同时，它就自动退出了上一行语句所属的代码块
if __name__ == '__main__':
    main()

'''