# -*- coding:gbk -*-
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