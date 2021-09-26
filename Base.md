### 数据类型

```
"""
    核心数据类型
        变量没有类型，关联的对象才有类型.

"""
# 1. None 空
# -- 占位：只希望有一个变量，但指向的对象还不能确定.
skill = None
# ...
skill = "乾坤大挪移"

# -- 解除与对象的绑定关系
name = None

# 2. 整形(整数)  int
# 字面值
# -- 十进制：0 1 2 3 ...9 10
number01 = -1
number01 = 1
number01 = 0

# -- 二进制：0 1 10  11  100  101 ..
number02 = 0b10
print(number02)

# -- 八进制：0 1 2 3 ... 7  10
number03 = 0o10
print(number03)

# -- 十六进制：0 --9  a(10) -- f(15)  10   11
number04 = 0x11
print(number04)

# 3. 浮点型(小数) float
# 字面值
number05 = 1.0
# 科学计数法
number06 = 5e3
print(number06)

number07 = 0.00000000000000000005
number07 = 500000000000000000000.0
print(number07)
```

### python交换变量

```
variable01, variable02 = variable02, variable01
```

### 物理行逻辑行

```
"""
    行
"""
# 三个物理行  三个逻辑行
a = 1
b = a + 1
c = a + b

# 一个物理行  三个逻辑行
a = 1;b = a + 1;c = a + b

# 三个物理行  一个逻辑行
a = 1+2+\
    3+\
    4+5+6

a = (1+2+
     3+4+5+6)
```

### 取各位数

```
number = int(input("请输入4位整数："))
# 个位 number % 10
result = number % 10
# 十位 number // 10% 10
result += number // 10% 10
# 百位 number // 100 % 10
result += number // 100 % 10
# 千位 number // 1000
result += number // 1000
print(result)
```

### 随机数库random

```
import random
random_number = random.randint(1, 100)
```

### 整数生成器range()

```
for item in range(3,10,2):
    print(item)
```

### 字符串编码

```
# 字 --> 数
number = ord("a")
print(number)

# 数 --> 字
str01 = chr(3498573945793475)
print(str01)
```

### 列表list

```
"""
    列表 list
    练习:exercise11
"""
# 1. 创建列表
list01 = []
list02 = list()

list01 = [90,"唐僧",True]
# 根据其他可迭代对象
list02 = list("我是齐天大圣")

# 2. 添加
# -- 追加
list01.append("悟空")
# -- 插入
list01.insert(2,"八戒")

# 3. 获取
# 索引：单个
print(list01[-1])
# 切片：多个
# 创建新列表
print(list01[:3])
# 循环：所有
for item in list01:
    print(item)
# 倒序
# 因为切片会产生新列表，浪费内存，所以不建议下面的方式
# for item in list01[::-1]:
#     print(item)
for i in range(len(list01)-1,-1,-1):
    print(list01[i])

# 4. 修改
# 索引
# 将右侧的数据地址赋值给左侧定位的元素
list01[-1] = "end"

# 切片
# 遍历右侧的可迭代对象，将每个元素赋值给左侧定位的元素
# list01[:2] = [1,2]
print(list01)
# list01[:2] = [1,2,3,4,5,6,7,8,9,10]
# list01[:3] = []
list01[1:1] = [1,2,3,4]
# 循环
for i in range(len(list01)):
    list01[i] = None
print(list01)

# 5. 删除
# 根据元素移除
list02.remove("我")

# 根据索引、切片移除
del list02[-1]
del list02[:2]
print(list02)
```

### 浅拷贝深拷贝

```
import copy

list01 = [10, [20, 30]]
list02 = list01[:]  # 浅拷贝
list03 = list01  # 赋值
list04 = copy.deepcopy(list01)  # 深拷贝

# 深拷贝
# 优点:互不影响
# 缺点：往往占用内存过多
```

### 元组tuple

```
"""
    元组tuple
"""
# 1. 创建
tuple01 = ()
tuple02 = tuple()

tuple01 = (12, 33, 4)
list01 = ["a", "b", "c"]
tuple02 = tuple(list01)
print(tuple02)
list03 = list(tuple01)

tuple02 = (1,)  # 元组中只有一个元素
tuple02 = 1, 2, 3  #
print(tuple02)

# 2. 查询
tuple03 = ("a", "b", "c")
a, b, c = tuple03

# 索引
print(tuple02[-1])

# 切片
print(tuple02[:2])

# 循环
for item in tuple02:
    print(item)
```

### 字典dict

```
"""
    字典dict
"""
# 1. 创建
dict01 = {}
dict02 = dict()

dict01 = {101: "a", 102: "b", 103: "c"}
dict02 = dict([(101,"a"),(102,"b")])

# 2. 添加
dict01[104] = "d"

# 3. 修改
dict01[104] = "e"

# 4. 查找
# key
print(dict01[102])
if 106 in dict01:
    print(dict01[106])

# 循环
for key in dict01:
    print(key)

for value in dict01.values():
    print(value)

for item in dict01.items():
    print(item)

for k,v in dict01.items():
    print(k)
    print(v)
```

### 集合set

```
"""
    集合set
        价值：去重复
             数学运算
"""
# 1. 创建
set01 = set()

set02 = {"唐僧", "悟空", "八戒"}

list01 = ["A", "b", "c", "A"]
set03 = set(list01)
print(set03)

print(set("abcacdb"))

# 2. 添加
set01.add("A")
set01.add("A")
print(set01)

# 3. 删除
set02.remove("唐僧")
if "唐三藏" in set02: set02.remove("唐三藏")
print(set02)

# 4. 循环
for item in set02:
    print(item)

# 5. 数学计算
set04 = {1, 2, 3}
set05 = {2, 3, 4}
# -- 交集
print(set04 & set05)# {2, 3}
# -- 并集
print(set04 | set05)# {1, 2, 3, 4}
# -- 补集
print(set04 ^ set05)# {1, 4}
print(set04 - set05)# {1}
print(set05 - set04)# {4}
# -- 子集
set06 = {2,3}
print(set06 < set04)
# -- 超集
print(set04 > set06)
```

### 容器推导式
```
dict_result = {item: item ** 2 for item in range(1, 10) if item % 2 ==0}
```

```
list01 = ["香蕉","苹果","哈密瓜"]
list02 = ["咖啡","牛奶","雪碧","可乐"]
# list03 = []
# for r in list01:
#     for c in list02:
#         list03.append(r +c)
list03 = [r +c for r in list01 for c in list02]

print(list03)
```

### 容器运算

```
max(list_height)
min(list_height)
```

```
#join
message = "How are you"
list_temp = message.split(" ")
result = " ".join(list_temp[::-1])
print(result)
```

```
#sum
month = int(input("请输入月份："))
day = int(input("请输入天数："))
day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# total_day = 0
# for item in day_of_month[:month - 1]:
#     total_day += item
total_day = sum(day_of_month[:month - 1])
total_day += day
print(total_day)
```

```
dict_persons = {
    "经理":{"曹操","刘备","孙权"},
    "技术":{"曹操","刘备","张飞","关羽"}
}
print(dict_persons["经理"]  &  dict_persons["技术"])#{'曹操', '刘备'}
print(dict_persons["经理"]  -  dict_persons["技术"])#{'孙权'}
print(dict_persons["技术"]  -  dict_persons["经理"])#{'张飞', '关羽'}  
print(dict_persons["技术"]  ^  dict_persons["经理"])#{'关羽', '张飞', '孙权'}
print(len(dict_persons["技术"]  |  dict_persons["经理"]))#5
```

### 函数内存分配

```
def fun02(p1,p2):
    p1 = 20
    p2[0] = 20

# 结论1：传入不可变对象，函数体内部不可能修改数据
a = 10
# 结论2：传入可变对象，函数体内部可能修改数据
b = [10]
fun02(a,b)
print(a)#?10
print(b)#?[20]
```

### 计算多位整数每位相加和

```
def each_unit_sum(number):
    """
        计算整数的每位相加和
    :param number:需要操作的数据，int类型
    :return:相加的结果，int类型
    """
    sum_value = 0
    for item in str(number):
        sum_value += int(item)
    return sum_value

re = each_unit_sum(12345)
print(re)
```

### 判断列表中是否存在相同元素

```
def is_repeating(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] == list_target[c]:
                return True
    return False

list01 = [3,4,6,8,8,7]
print(is_repeating(list01))
```
### 方阵转置

```
def square_matrix_tranpose(matrix):
    for c in range(len(matrix) - 1):
        for r in range(c + 1, len(matrix)):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]

square_matrix_tranpose(list01)
print(list01)
```

### 全局变量

```
count = 0
def fun01():
    global count
    count += 1
fun01()
fun01()
print("执行次数是：" + str(count))
```

### 函数实参形参

```
def fun01(a, b, c):
    print(a)
    print(b)
    print(c)

#位置实参：根据位置，将实参传递给形参。
fun01(1, 2, 3)

#序列实参：使用星号将序列拆分后，与形参进行对应。
list01 = [4, 5, 6]
fun01(*list01)

#关键字:根据名称，将实参传递给形参。
fun01(a=1, c=3, b=2)

#字典实参：使用双星号将字典拆分后，与形参进行对应。
dict01 = {"c": 3, "b": 2, "a": 1}
fun01(**dict01)

```

```
#位置形参:约束实参必须提供  【必填】
def fun01(a, b, c):
    print(a)
    print(b)
    print(c)

#默认参数：实参可以不提供   【可选】
def fun02(a=0, b="", c=0.0):
    print(a)
    print(b)
    print(c)
fun02(1)
fun02(b="bb")

#星号元组形参：将位置实参合并为一个元组
#只能有一个,建议形参名称位args
def fun03(*args):
    print(args)
fun03(1, 2, 3)
# fun03(a = 1,b=2)

#命名关键字形参：星号元组形参，后面的位置形参，必须使用关键字实参传递。
def fun04(*args, a, b, c):
    print(args)
fun04(1, 2, 3, 4, 5, a=1, b=2, c=3)

def fun05(a, *, b=0, c=0):
    print(a)
    print(b)
    print(c)

fun05(1, c=3)

# print(*args, sep=' ', end='\n')
print(1, 2, 3, 4, end=" ")
print(1, 2, 3, 4, sep="-")
print(1, 2, 3, 4, end=" ", sep="-")

#双星号字典形参：将关键字实参合并为一个字典
#只能有一个,建议形参名称位args
def fun06(**kwargs):
    print(kwargs)

fun06(a = 1,b = 2)
```

```
#关键字传参
def get_total_second(hour=0, minute=0, second=0):
    return hour * 3600 + minute * 60 + second

print(get_total_second(1, 2, 3))
print(get_total_second(1, 2))
print(get_total_second(minute=2, second=3))
print(get_total_second(minute=2))
```

```
#列表传参
def sum(*args):
    sum_value = 0
    for item in args:
        sum_value += item
    return sum_value

print(sum(213,3,4,3,5,6,67))
print(sum())

list = [1,2,3,4]
print(sum(*list))
```

```
#列表和关键字传参
def fun01(*args, **kwargs):
    print(args)
    print(kwargs)

fun01()
fun01(12,2,a = 1,b=2)
# fun01(12,a = 1,2,b=2)

def fun02(a, *args, b, c="", **kwargs):
    print(a)
    print(args)
    print(b)
    print(c)
    print(kwargs)

fun02(1,2,3,b = 2,c="3",d = 4)
fun02(a = 1,b = 2)
```

### 字符串内置方法

```
message = "  自强不 息,  厚德 载物. "
print(message.count(" "))
print(message.replace(" ",""))
print(message.find("厚德"))
print(message.startswith("自强"))
```

```
"""
    str --> list
"""

message = "悟空-猪八戒-沙和尚"
list_result = message.split("-")
print(list_result)
```

```
"""
    list --> str
"""
# 根据xx逻辑，拼接一个字符串。
# range(10) --> "0123456789"

# str_result = ""# 不可变
# for item in range(10):
#     # str_result += str(item)
#     # 每次循环 每次拼接 都会创建新对象 产生一个垃圾
#     str_result = str_result + str(item)
# print(str_result)

list_temp = []#可变
for item in range(10):
    # 每次追加新对象 不会产生垃圾
    list_temp.append(str(item))

str_result = "-".join(list_temp)
print(str_result)
```

### 切片赋值

```
lista = [1,2,3,4]
listb = [0,0,0,0]
listb[::-1] = lista
print(listb)#[4, 3, 2, 1]
```