### 类的定义和实例

```
class Cellphone:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def call(self):
        print(self.brand, "打电话")

# 创建手机对象
# 会调用__init__构造函数
iphone01 = Cellphone("苹果", 9999, "绿色")
huawei01 = Cellphone("华为", 6666, "白色")
iphone01.call()
huawei01.call()
```

### 对象具有的实例变量

```
print(ak.__dict__)
```

### 类变量和类方法(@classmethod)

```
class ICBC:
    """
        工商银行
    """
    # 类变量：大家的数据(总行的钱)
    total_money = 1000000

    @classmethod
    def print_total_money(cls):
        # print("总行的钱：",ICBC.total_money)
        print("总行的钱：",cls.total_money)

    def __init__(self, name="", money=0):
        self.name = name
        self.money = money
        # 总行的钱减少
        ICBC.total_money -= money


i01  = ICBC("陶然亭支行",100000)
ICBC.print_total_money()

i02  = ICBC("天坛支行",100000)
ICBC.print_total_money()
```

### 静态方法(@staticmethod)

```
class Vector2:
    """
        向量
    """
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    @staticmethod
    def get_left():
        return Vector2(0,-1)

    @staticmethod
    def get_right():
        return Vector2(0,1)

    @staticmethod
    def get_up():
        return Vector2(-1,0)

class DoubleListHelper:
    """
        二维列表助手类
    """
    @staticmethod
    def get_elements(list_target, vect_pos, vect_dir, count):
        list_result = []
        for __ in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            element = list_target[vect_pos.x][vect_pos.y]
            list_result.append(element)
        return list_result

list01 = [
    ["00","01","02","03","04"],
    ["10","11","12","13","14"],
    ["20","21","22","23","24"],
    ["30","31","32","33","34"],
]

print(DoubleListHelper.get_elements(list01,Vector2(3,0),Vector2.get_right(),3)

# 练习:32位置 向上获取3个元素
print(DoubleListHelper.get_elements(list01,Vector2(3,2),Vector2.get_up(),3))
# 练习:34位置 向左获取3个元素
print(DoubleListHelper.get_elements(list01,Vector2(3,4),Vector2.get_left(),3))
```

### 方法封装

```
"""
    __变量名  -->   _类名__变量名
"""
class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        # self.__age = age
        self.set_age(age)

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 20 <= value <= 50:
            self.__age = value
        else:
            raise Exception("我不要")

w01 = Wife("宁宁", 25)
print(w01.__age) # AttributeError: 'Wife' object has no attribute '__age'
print(w01._Wife__age) #25
w01._Wife__age = 100
print(w01._Wife__age) #100

w01.set_age(27)
print(w01.get_age())

w01.__age = 100
print(w01.__dict__)
```

### 属性封装

```
class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        # self.set_age(age)
        self.age = age #创建实例变量

    #提供两个公开的读写方法
    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 20 <= value <= 50:
            self.__age = value
        else:
            raise Exception("我不要")

    # 类变量
    # property 作用:拦截
    age = property(get_age, set_age) #创建类变量存储property对象


w01 = Wife("宁宁", 25)
w02 = Wife("铁锤", 26)
# w01.set_age(27)
w01.age = 27
print(w01.age)
print(w01.__dict__)
```

### 标准属性封装

```
class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age #创建实例变量

    @property# 创建property对象,自动绑定下面方法（读取）
    def age(self): # 与属性名一致
        return self.__age

    @age.setter# 自动绑定下面方法（写入）
    def age(self, value): # 与属性名一致
        if 20 <= value <= 50:
            self.__age = value
        else:
            raise Exception("我不要")

w01 = Wife("宁宁", 25)
w01.age = 27
print(w01.age)
print(w01.__dict__)
```

### 只读属性

```
class Wife02:
    def __init__(self):
        self.__age = 26

    @property
    def age(self):  # 秘书
        return self.__age  # 老板

w01 = Wife02()
print(w01.age)

# w01.age = 100# 不能写入
```

### 只写属性

```
class Wife01:
    def __init__(self, age=0):
        self.age = age

    def __set_age(self, v):
        self.__age = v

    age = property(None, __set_age) #因为没有属性绑定

w01 = Wife01(25)
w01.age = 26
# print(w01.age)
print(w01.__dict__) 
```

### 继承

```
# 内置函数
# isinstance   对象  是一种  类型
print(isinstance(p01, Person))  # True
print(isinstance(s01, Person))  # True
print(isinstance(t01, Student))  # False
print(isinstance(p01, Teacher))  # False

# issubclass   类型  是一种  类型
print(issubclass(Person, Person))  # True
print(issubclass(Student, Person))  # True
print(issubclass(Teacher, Student))  # False
print(issubclass(Person, Teacher))  # False

# type 对象  是  类型
print(type(p01) == Person)  # True
print(type(s01) == Person)  # False
print(type(t01) == Student)  # False
print(type(p01) == Teacher)  # False
```

### 继承 - 数据

```
class Person:
    def __init__(self, name=""):
        self.name = name


class Student(Person):
    def __init__(self, name="", score=0):
        super().__init__(name)
        self.score = score


# 如果子类没有构造函数,直接使用父类构造函数
s01 = Student("悟空", 100)
print(s01.name)
```

### 重写（覆盖）

```
class Wife(object):
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # 对象 --> 字符串(没有限制)
    def __str__(self):
        return "奴家%s今年%d岁啦" % (self.name, self.age)

    # 对象 --> 字符串(python语法)
    def __repr__(self):
        return "Wife('%s', %d)"% (self.name, self.age)


w01 = Wife("双儿", 22)
# print(w01)
content = w01.__str__()
print(content)

code = w01.__repr__()
print(code)

# eval：将字符串作为python代码执行
print(eval("1+2*3"))
# print(eval(input()))

# 克隆对象
w02 = eval(w01.__repr__())
w01.age = 26
print(w02.age)
```

### 运算符重载

```
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x的分量是%d,y的分量是%d" % (self.x, self.y)

    # +
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    # += 返回自身，没有新建对象
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    # <
    def __lt__(self, other):
        return self.x + self.y < other.x + other.y

    # ==
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


pos = Vector2(1, 2)
dir = Vector2(0, 1)
# print(pos + dir)  # pos.__add__(dir)

# pos.x += dir.x
# pos.y += dir.y
pos += dir
# print(pos)

"""
# 创建了新对象
list01 = [1]
print(id(list01))
list01 = list01 + [2]
print(id(list01))

# 累加(在原有对象基础上增加)
list02 = [1]
print(id(list02))
list02 += [2]
print(id(list02))
"""

list01 = [
    Vector2(1, 2),
    Vector2(7, 8),
    Vector2(5, 6),
    Vector2(3, 4)
]

# sorted升序：内部在循环调用每个元素的__lt__
for item in sorted(list01):  #
    print(item)

#in 的内部也在循环调用每个元素的__eq__方法
print(Vector2(1, 2) in list01)# ?

# list01.remove(Vector2(1, 2))
# list01.count(Vector2(1, 2))
```

### 设计思想

```
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, vehicle):
        print("走喽")
        # 1. 调用交通工具(父)
        if not isinstance(vehicle,Vehicle):
            raise Exception("传入的必须是交通工具")

        vehicle.transport()


class Vehicle:
    """
        交通工具:隔离人与具体交通工具的变化
    """

    def transport(self):
        pass


# -------------------------------------
class Car(Vehicle):
    # 3. 重写
    def transport(self):
        print("嘟嘟～")


class Airplane(Vehicle):

    def transport(self):
        print("嗖嗖~")


p01 = Person("老张")
c01 = Car()
a01 = Airplane()
# 2. 创建子类对象
p01.go_to(c01)

```

### 多继承

```
class A:
    def func(self):
        print("A")

class B(A):
    def func(self):
        print("B")

class C(A):
    def func(self):
        print("C")

class D(B, C):
    def func(self):
        print("D")
        super().func()# B
        C.func(self)# 调用指定名称的父类同名方法 C

d01 = D()
d01.func()
print(D.mro())
```

### 设计规则

#### 开-闭原则（目标、总的指导思想） 

#### 类的单一职责（一个类的定义）

#### 依赖倒置（依赖抽象）

#### 组合复用原则（复用的最佳实践）

#### 里氏替换（继承后的重写，指导继承的设计）

#### 迪米特法则（类与类交互的原则）

