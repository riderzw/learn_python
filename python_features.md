# python特性

## 切片

作用截取`list`或`tuple`的部分元素，语法为`[A:B:C]`其中A代表从某个位置开始，B代表结束位置，C代表取值间隔 如2就代表每两个取一个元素。

示例：

```python
numberList = list(range(100))
print(numberList[0:10])
```

输出为：

```python
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

要取最后10个元素则为：

```python
print(numverList[-10:])
```

输出为：

```python
[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
```

每两个取一个元素

```python
print(numberList[0:10:2])
```

输出为：

```python
[0, 2, 4, 6, 8]
```

## 迭代

遍历`list`、`tuple`等可迭代的对象，语法为`for...in...`

迭代list：

```python
for a in numberList:
	print(a)
```

迭代dict key：

```python
person = {"name":"lily","age":"18"}
for key in person:
	print(key)
```

迭代dict value：

```python
for value in person.values():
	print(value)
```

迭代dict key and value：

```python
for k,v in person.items():
	print(k+":"+v)
```

## 列表生成式

列表生成式即用来生成`list`的表达式,如生成`[1,2,3,4,5,6,7,8,9,10]`便可以用`list(range(1,11))`快速生成.这只是最简单的应用，如果要生成稍微复杂一点的`list`如`[1*1,2*2,3*3,4*4,...10*10]`便可以用到列表生成式。

```python
[x*x for x in range(1,11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

如果只生成偶数的平方则

```python
[x*x for x in range(1,11) if x%2 ==0]
[4, 16, 36, 64, 100]
```

如果要生成全排列

```python
[x+y for x in "ABC" for y in "DEF"]
['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']
```

## 生成器

生成器与列表生成式同样是同样是用来生成`list`，区别是列表生成式在生成时是将`list`所有的元素生成，而生成器保存的是算法,按需生成，比如只需要前十个元素，则只生成前十个,按需生成.可以将列表生成式很方便的改为生成器只需要将`[]`更改为`()`。如果函数中包含`yield`，那它就不是普通的函数，而是生成器。

杨辉三角

```
         1
        1   1
      1   2   1
    1   3   3   1
  1   4   6   4   1
1   5   10  10  5   1
```



对应的生成器

```python
def triangles():

	line = [1]
	yield line
	line = [1,1]
	while True:
		yield line
		line = [1]+[line[i] +line[i+1] for i in range(len(line)-1)]+[1]
```

调用

```python
while m<10:
	try:
		m = m+1
		print(next(g))
	except StopIteration as e:
		print(e.value)
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
[1, 7, 21, 35, 35, 21, 7, 1]
[1, 8, 28, 56, 70, 56, 28, 8, 1]
[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
 
```

## 迭代器

生成器都是迭代器