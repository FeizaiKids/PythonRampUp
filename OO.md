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