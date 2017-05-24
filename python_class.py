# -*- coding: utf-8 -*-
from types import MethodType
from enum import Enum



class Student(object):
	__slots__ = ("name","score","age","set_name","__msex")
	def __init__(self,name,score):
		self.name = name
		self.score =score
		self.__msex = None
	
	@property
	def msex(self):
		return self.__msex
	
	@msex.setter
	def msex(self,value):
		self.__msex = value	
		
		
	def get_name(self):
		return self.name
	def get_score(self):
		return self.score
	def printInfo(self):
		print("name : %s score : %d"%(self.name,self.score))

	
		
lily = Student("lily",99)
lily.printInfo()
lily.msex = "girl"

print(type(lily))
print(dir(lily))
lily.age = "15"

print(lily.age)


def set_name(self,name):
    self.name = name
lily.set_name = MethodType(set_name,lily)
lily.set_name("bob")
lily.printInfo()



Month  =  Enum("Month",("Jan","Feb","Mar"))

for name ,member in Month.__members__.items():
	 print(name, '=>', member, ',', member.value)