#coding=utf-8

''''
#不加前面的coding，直接下面一行会报错： Non-ASCII character '\xe5' in file
#函数式编程 装饰器
'''
import functools  
import types  


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


########装饰器

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
  
#current3() 



''''' 
请装饰器范例 
定义一个能打印日志的decorator 
''' 

def log22(func):
	def wrapper(*args, **kw):
		print 'before call'
		func(*args, **kw)
		print 'end call'
		#print func(*args, **kw)
	return wrapper
@log22
def now():
	print '2013-12-25'
#now();
#now = log(now)



''''' 
再思考一下能否写出一个@log的decorator，使它 
既支持： 
@log 
def f(): 
    pass 
 
又支持： 
@log('execute') 
def f(): 
    pass 
'''  
#这个就有点难为我了,我就在此沦陷啦  
#首先要使用默认值,这一点还是比较清楚的  
#以下代码为模仿别人的  
def log(text='execute'):  
    def logdecorate(func):  
        @functools.wraps(func)  
        def wrapper(*args,**kw):  
            ''''' 
            如果text有值,那就要打印出该值 
            如果没值,那就打印默认值,所以都是 
            text 
            '''  
            print '%s %s()' % (text,func.__name__)  
            return func(*args,**kw)  
        return wrapper  
    ''''' 
    如果text参数有传值过来的话, 
    说明用的是log('text'),即log('text')(now) 
    这个时候要将log('text')转成logdecorate才成 
    即函数原型,然后才能变为log('text')(now)==logdecorate(now) 
    所以有参数时直接返回logdecorate函数 
    '''  
    #判断text是否属于函数类型  
    if not isinstance(text,types.FunctionType):  
        #为log('text')  
        return logdecorate  
    ''''' 
    如果没有传值过来的话,说明用的是log,即log(now). 
    text==now,其实就是要调用logdecorate(now) 
    所以无参数时,直接返回调用logdecorate(now)的结果 
    '''  
    if isinstance(text,types.FunctionType):  
        #为log形式  
        return logdecorate(text)  
 
@log  
def func_one():  
    print 'log has no args'  
 
@log('diff')  
def func_two():  
    print 'log has args'  
  
#func_one()  


max2 = functools.partial(max, 10)
print max2(5, 6, 7)
'''
相当于：
args = (10, 5, 6, 7)
max(*args)
'''