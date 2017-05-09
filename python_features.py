# -*- coding: gbk -*-
#--------切片------------
numberList =list(range(15))
print (numberList)
print(numberList[0:10])
print(numberList[:5])
print(numberList[-10:])
print(numberList[0:10:2])
#--------迭代------------
for a in numberList:
	print(a)
person = {"name":"lily","age":"18"}
for key in person:
	print(key)
for value in person.values():
	print(value)
for k,v in person.items():
	print(k+":"+v)
	
setPerson = (["lily","bob","sandy"])

for x in setPerson:
	print(x)

#--------列表生成式-----------

simpleList = list(range(1,11))
print(simpleList)

complexList = [x*x for x in range(1,11)]
print(complexList)

moreComplexList1 = [x*x for x in range(1,11) if x%2 ==0]
print(moreComplexList1)

moreComplexList2 = [x+y for x in "ABC" for y in "DEF"]
print(moreComplexList2)

#-----------生成器-------------
g = (x*x for x in range(1,11))

for x in g:
	print(x)

def triangles():

	line = [1]
	yield line
	line = [1,1]
	while True:
		yield line
		line = [1]+[line[i] +line[i+1] for i in range(len(line)-1)]+[1]
	
g= triangles()
m = 0
while m<10:
	try:
		m = m+1
		print(next(g))
	except StopIteration as e:
		print(e.value)



