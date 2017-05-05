# -*- coding: gbk -*-

print("hello,World")
print("hello,World lenth:	"+str(len("hello,World")))
#"hello %s，you have $%d" %("xxx",10000)

#list
print("--------------list---------------")
classmates = ["lily","tom","jim"]
print("取第一个值")
print("first value:	"+classmates[0])
print("last value:	"+classmates[-1])
print("添加值")
classmates.append("adison")
print(classmates)
print("删除最后的一个值")
classmates.pop()
print(classmates)
print("删除指定位置的值")
classmates.pop(1)
print(classmates)

#tuple
print("--------------tuple---------------")
print("tuple元组为不可变对象 没有 append pop 方法")

print("创建空 tuple")
classmatesTuple = ()
#当创建长度为1的tuple时，需加“，”
print("当创建长度为1的tuple时，需加“，”")
classmatesTuple = ("lily",)
print(classmatesTuple)

#条件判断
print("--------------条件判断---------------")
age =17
if age<18:
	print("青少年")
elif age>=18 and age>28:
	print("青年")
else:
	print("中年")
#循环
print("--------------循环---------------")
numberList = range(10)
print("for in 循环")
for x in numberList:
	print(x)
index = 0
print("while 循环")
while index<len(numberList):
	print(numberList[index])
	index = index+1
#字典
print("--------------dict and set---------------")	
print("定义dict")
d = {"lily":95,"bob":93,"sandi":90}
#取值
print(d)
print("取值")
print("lily 的分数 "+str(d.get("lily")))
print("增值")
d["adison"] = 99
print(d)
#删除
print("lily" in d.keys())
print("删除了lily")
d.pop("lily")
print(d)
print("定义set")
s = set([1,2,3,4])
print(s)
print("set没有重复的内容")
print("添加4")
s.add(4)
print(s)



