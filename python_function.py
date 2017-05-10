# -*- coding:utf-8 -*-
from functools import reduce

print("------function---------")

def power(x):
	return x*x



def power(x,n=4):
	s=1;
	while n>0:
		n = n-1;
		s = s*x
	return s

print( str(power(2)))
print(str(power(2,5)))
def mSum(*number):
	sum = 0
	for x in number:
		sum  =sum +x
	return sum;
print(mSum(1,2,3,4,5))

def person(name,age,**ot):
	print(name+age)
	print(ot)
	
person("lily","23",city = "shanghai", job ="android")
#map

def addCharA(s):
	
	return s+"A"

personList = ["lily","sandy","bob","joker"]

personAList = map(addCharA,personList)
print(list(personAList))


def calSum(i,j):
	if(isinstance(i,int) and isinstance(j,int)):
		return i+j
	else:
		raise TypeError("类型错误")
numberList =[1,2,3,22,88,6,7,8,9,10,14,33,55,96]

print(str(reduce(lambda x,y:x+y,numberList)))


print(sorted(numberList,reverse =True))


#返回函数

def lazySum():
	return str(reduce(calSum,numberList))
f = lazySum
f