# -*- coding: utf-8 -*-
# @Time : 2023/7/19 10:16
# @Author : zhoufan
# @File : annotation_demo.py
# @Project : geektime_0-master
from typing import List, NewType, NoReturn, Callable, TypeVar, Dict, Union


# 类型提示功能--python3.5及以上版本新增
# 好处：
# 1、增加代码的可读性
# 2、ide中代码提示
# 3、静态代码检查 -第三方包来进行静态代码检查 mypy


# 变量注解
# age = 20


# age = '2'


def print_name(name):
    return name


print(print_name(11))


# 函数注解
# def say_hi(name: str) -> str:
#     return f'hi,{name}'
#
#
# print(say_hi('zhoufan'))
#
#
# # 自定义对象
class Person:
    def __init__(self, name: str):
        self.name = name


def hello(p: Person) -> str:
    return f'Hello, {p.name}'


def get_person(name: str) -> Person:
    return Person(name)


# 类型别名
Vector = List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


print(scale(2.2, [1.2, 22.1]))
# -----------------------------------
# NewType和类型别名类似,但是区别在于，NewType创建的是原始类型的子类
UserId = NewType('UserId', int)
user_id: UserId = UserId(123456)
print(user_id * 3)


# Vector3D = NewType('Vector3D', Tuple[int, int, int])
# vector: Vector3D = Vector3D((1, 2, 3))
# print(vector[0])


# more
# NoReturn 函数没有返回值
def hello1() -> NoReturn:
    raise RuntimeError('oh no')


# Union:函数的返回值是多种类型中的一种
def foo() -> Union[int, str, float]:
    ...


# Callable 只要求对象可调用

class C1:
    def __call__(self):
        print('I am foo')


def bar1():
    print('I am bar')


def hello2(a: Callable):
    a()


# 类型检查通过
hello2(C1())
# 同样通过
hello2(bar1)

K = TypeVar("K")
V = TypeVar("V")


def get_item(key: K, container: Dict[K, V]) -> V:
    return container[key]


dict_1 = {"age": 10}
dict_2 = {99: "dusai"}

print(get_item("age", dict_1))
# print(get_item("age", dict_2))
# # 例1
# # 类型检查通过，输出: 10
#
# print(get_item(99, dict_2))
# # 例2
# # 类型检查通过，输出: dusai
#
# print(get_item("name", dict_2))
# # 例3)
