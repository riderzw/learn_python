# -*- coding: gbk -*-

print("hello,World")
print("hello,World lenth:	"+str(len("hello,World")))
#"hello %s��you have $%d" %("xxx",10000)

#list
print("--------------list---------------")
classmates = ["lily","tom","jim"]
print("ȡ��һ��ֵ")
print("first value:	"+classmates[0])
print("last value:	"+classmates[-1])
print("���ֵ")
classmates.append("adison")
print(classmates)
print("ɾ������һ��ֵ")
classmates.pop()
print(classmates)
print("ɾ��ָ��λ�õ�ֵ")
classmates.pop(1)
print(classmates)

#tuple
print("--------------tuple---------------")
print("tupleԪ��Ϊ���ɱ���� û�� append pop ����")

print("������ tuple")
classmatesTuple = ()
#����������Ϊ1��tupleʱ����ӡ�����
print("����������Ϊ1��tupleʱ����ӡ�����")
classmatesTuple = ("lily",)
print(classmatesTuple)

#�����ж�
print("--------------�����ж�---------------")
age =17
if age<18:
	print("������")
elif age>=18 and age>28:
	print("����")
else:
	print("����")
#ѭ��
print("--------------ѭ��---------------")
numberList = range(10)
print("for in ѭ��")
for x in numberList:
	print(x)
index = 0
print("while ѭ��")
while index<len(numberList):
	print(numberList[index])
	index = index+1
#�ֵ�
print("--------------dict and set---------------")	
print("����dict")
d = {"lily":95,"bob":93,"sandi":90}
#ȡֵ
print(d)
print("ȡֵ")
print("lily �ķ��� "+str(d.get("lily")))
print("��ֵ")
d["adison"] = 99
print(d)
#ɾ��
print("lily" in d.keys())
print("ɾ����lily")
d.pop("lily")
print(d)
print("����set")
s = set([1,2,3,4])
print(s)
print("setû���ظ�������")
print("���4")
s.add(4)
print(s)



