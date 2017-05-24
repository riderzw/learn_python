# -*- coding:utf-8 -*-
from io import StringIO
from io import BytesIO
import os
import stat
file = open("C:/Users/junova/Desktop/text.txt","r")
#// C:\Users\junova\Documents\GitHub\learn_python \会造成转义 推荐使用 /
print(file.read())
file.close()

#安全的文件操作
try:
	f = open("C:/Users/junova/Desktop/text.txt","r")
	print(f.read())
finally:
	if f:
		f.close()
#with语法自动调用close()

with open("C:/Users/junova/Desktop/text.txt","r") as f1:
	print(f1.read())
	
#逐行读取文件,读取指定编码
try:
	f2 = open("C:/Users/junova/Desktop/text.txt","r",encoding = "gbk")
	for line in f2.readlines():
		print(line.strip())
finally:
	if f2:
		f2.close()
#写文件
with open("C:/Users/junova/Desktop/text.txt","w") as f3:
	f3.write("hello python,i came")

	
sio = StringIO()
sio.write("hello xxxxx\n i came")
print(sio.getvalue())

while True:
	s= sio.readline()
	if s =="":
		break
	print(s.strip())
bio = BytesIO()
bio.write("你好".encode("UTF-8"))
print(bio.getvalue())

print(os.name)

print(os.path.abspath("."))
dir = os.path.join(os.path.abspath("."),"testdir")
filepath = os.path.join(dir,"test1.txt")
#创建文件
f4 = open(filepath,mode="w",encoding="utf-8")
f4.write("create new file")
f4.close()
print(os.path.splitext(filepath))
print(os.listdir())
print([x for x in os.listdir() if os.path.isfile(x) and os.path.splitext(x)[1]==".py"])

