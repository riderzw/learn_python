# 函数

## 参数

### 参数类型



* 必选参数

* 默认参数

  参数有默认值

* 可变参数

  传入的是list *args

* 关键字参数

  传入的是tuple **kw

* 命名关键字参数

  限制关键字参数的名字 

  ```python
  def person(name, age, *, city, job):
      print(name, age, city, job)
  ```

  ​

### 参数组合

​	按顺序排列 