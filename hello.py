#coding=utf-8

#print u'请输入你的姓名:'
#name = raw_input()
#print 'hello,', name

#print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
# 中文

"""
import os # 导入os模块，模块的概念后面讲到
print [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
#\xd0\xc2\xbd\xa8\xce\xc4\xb1\xbe\xce\xc4\xb5.txt
for dd in [d for d in os.listdir('.')]:
	#print dd.decode('utf-8')
	print dd#新建文本文档.txt
#x,y = (1,2)
#print x,y
"""

#str1 = 'hello, %s\n' % 'world'
#str2 = "Hi, %s, your score is:%d" % ("liyijun", 100)
#print str1, str2


"""
g = (x * x for x in range(10))
print g

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print b
        yield b
        a, b = b, a + b
        n = n + 1

 #print None
 #yield  <generator object fib at 0x104feaaa0>
value = fib(6); 
print 'value:', value

for n in value:
	print 'for in value:',n

for n in fib(6):
	print 'for in fib:',n
"""


"""
def f(x):
	return x * x
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
"""

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

#f1, f2, f3 = count() #[function f, function f, funciton f]
'''
f1 = count()
f2 = count()
print f1
print f2
'''


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
#print f()


########[函数式编程]装饰器
import functools  
import types  
''''' 
请编写一个decorator，能在函数调用的前后打印出 
'begin call'和'end call'的日志。 
'''  
def logt(text):  
    def log(func):  
        @functools.wraps(func)  
        def wrapper(*args,**kw):  
            print '%s %s():'% (text,func.__name__)  
            func(*args,**kw)  
            print 'finish %s():'% func.__name__  
        return wrapper  
    return log  
@logt('execute')  
def current3():  
    print 'nihaoa'  
  
current3() 


def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


@log   
def now():
	print '2013-12-25'
#now = log(now)