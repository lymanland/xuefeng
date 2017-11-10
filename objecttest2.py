#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test 高级编程 chapter '

__author__ = 'YiJun Lee'

class Student(object):
    __slots__ = ('name', 'age')

    def set_age(self, age):
    	self.age = age;

   	#pass
   	#

s = Student()
s.name = 'Michale'
s.age = 25
s.set_age(25)
#s.score = 99


#__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：
class GraduateStudent(Student):
	#子类允许定义的属性就是自身的__slots__加上父类的__slots__
	#__slots__ = () # gs.score Error
	#__slots__ = ('score') #包含'name', 'age'
	pass

gs = GraduateStudent()
gs.age = 100	#ok
gs.score = 100 