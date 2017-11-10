#!/usr/bin/env python
# -*- coding: utf-8 -*-
#第1行和第2行是标准注释，
#第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，
#第2行注释表示.py文件本身使用标准UTF-8编码；  
## #coding=utf-8短一点，但Emacs不能用
##用来说明你的Python源程序文件用使用的编码。缺省情况下你的程序需要使用ascii码来写，
##但如果在其中写中文的话，python解释器一般会报错，但如果加上你所用的文件编码，python就会自动处理不再报错。

' a test module '
#模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
#
__author__ = 'YiJun Lee'
#使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

import sys

print 'test sys.args'

def test():
    args = sys.argv
    if len(args)==1:
        print 'Hello, world!'
    elif len(args)==2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__=='__main__':
    test()



#导入模块时，还可以使用别名，这样，可以在运行时根据当前环境选择最合适的模块
try:
    import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO

try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5

#由于Python是动态语言，函数签名一致接口就一样，因此，无论导入哪个模块后续代码都能正常工作。



#外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
#从编程习惯上不应该引用private函数或变量
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

print greeting('Lee');
print greeting('yiJun Lee');

print sys.path

#pip install PIL 这条命令安装不了
#Python Imaging Library
#代替库 ？？？ https://pypi.python.org/pypi/Pillow
#
#安装了Pillow需要 import前需要加from PIL
#不然会报错 import Version,Pillow_VERSION, —pligins ValueError：attempedrelative import in non-package
#import Image
from PIL import Image

im = Image.open('test.png')
print im.format, im.size, im.mode