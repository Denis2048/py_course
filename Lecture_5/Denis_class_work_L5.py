## L5.
#import  this
import sys

# n = 10
# users = []
# user_a_pass = input("pass:")
# users_a_name = input("name:")
# users.append([users_a_name, user_a_pass])
# print(users)

# users = []
# def register():
#     users_a_name = input("name:")
#     user_a_pass = input("pass:")
#     users.append([users_a_name, user_a_pass])
#     #print("done:", users)
#
# for i in range(3):
#     register()
# print(users)

# def hello():
#     print("hello")
# hello()

# def hello():
#     user = input("name:")
#     print("hello", user)
#
# hello()

# def hello():
#     user = input("name:")
#     print("hello", user)
#     for i in range(3):
#         print(i, end = " ")
#     d = 88
#     if d == 88:
#         print("xxx")
#     print(354465464)
#
# hello()

# hello = 55
# hello()

# change_pass()

# def hi():
#     print("")
# hi(55)

# # Param
# def hello(user):
#     print("Hello", user)

# print(hello(123))

# def hello(a, b, c):
#     print("Hello", a, b, c)
#
# print(hello(1, 2,3))

# def hello(a, b, c):
#     print("Hello", a, b, c)
#
# print(hello(b = 1, c = 2, a = 3))
# print(hello(1, c = 2, b = 3))
# print(hello(1, c = 2, 3))    # Err

# def hello(name, age):
#     print("Hello", name, age)
#
# print(hello("Vasy", 28))
# print(hello(28, "Vasy"))  # Problem

# def hello(name, age = 22):
#     print("Hello", name, age)
#
# print(hello("Vasy"))

# def create_order(name, ph, age="", msg=""):
#     print("Order 32555:")
#     print("order dit:")
#     print(f"Name:{name}")
#     print(f"Phone:{ph}")
#     print(f"Age:{age}")
#     print(f"MS:{msg}")
#     print()
#
# create_order("Goose", 123, 18, "call me")
# create_order("Goose", 123)

# def a(name = "Dsd", age = 123):
#     print(name, age)

# a()
# a("Fggfg")

# name = input("-->")
# print(name)

# def hello():
#     pass
#
# res = hello()
# print(res)
#
# def hello():
#     print(1*44)
#
# res = hello()
# print(res)

# def create_order(name, ph, age="", msg=""):
#     """Функция которая делает что-то           # Строки документации.
#     имя - строка, обязательно
#     телефон - обязательно
#     возраст - необязательно
#     сообщение - необязательно"""
#     if len(name) < 2:
#         return False
#     if str(ph).isalnum() != True:
#         return False
#
#     print("Order 32555:")
#     print("order dit:")
#     print(f"Name:{name}")
#     print(f"Phone:{ph}")
#     print(f"Age:{age}")
#     print(f"MS:{msg}")
#     print()
#     return True
#
# res = create_order("", 1315)
# print(res)
# res = create_order("Yan", 1315)
# print(res)
# #res = create_order("Yan", 13 15)   # Err.
# #print(res)

# def Up(name):
#     print(name.upper())
#
# print(Up("sdsdd"))
#
#
# def Up(name):
#     return name.upper()
#
# upName = Up("dfdfdf")
# print(Up("sdsdd"))
# print(upName)

#help(print)

# def a():
#     print(1)
# def b():
#     print(2)
# def c():
#     print(3)
# del c
#
# print(b())
# print(id(a))
# #print(c())   # Err.

# def numbers(num):
#     if num % 2 == 0:
#         return True
#     return None
# print(numbers(2))

# def numbers(num):
#     if num % 2 == 0:
#         return True
#
# print(numbers(2))
# print(numbers(3))

# def numbers(num):   # Упрощение.
#     return num % 2 == 0
#
# print(numbers(2))
# print(numbers(3))

# a = 10
# s = "dsfsdfdsf"
#
# print(isinstance(a, int))
# print(isinstance(a, str))
#
# if isinstance(a, int):
#     print("INT")
#
# print(isinstance(a, (int, float, str)))   # Проверка а на экземпляр типа.

# total = 0         # Ошибка LGBT).
# def add_to_total(n):
#     total = total + n
#
# add_to_total(5)
# print(total)

# x = 5154
# def add(x):
#     print("In", x, id(x))
#     x += 8888
#     print("In", x, id(x))
#
# print(add(218))
#
# number = 5154
# def add(number):
#     print("In", number, id(number))
#     number += 8888
#     print("In", number, id(number))
#
# print(add(218))

# number = 5154
# def add():
#     global number
#     print("In", number, id(number))
#     number += 8888
#     print("In", number, id(number))
#
# add()

# def a():
#     print(1)
# def b():
#     print(2)
# def c():
#     print(3)
#
# li = [a(), b(), c()]
# print(li)

# def noname(number):      # Рекурсия.
#     if number > 20:
#         return True
#     return number + noname(number+4)

# print(noname(1))

# from math import factorial
# sys.getrecursionlimit()
# print(factorial(1000))

# f1 = f2 = 1    # Фибоначи.
# f1, f2 = f2, f1 + f2
# print(f1, f2)#
# f1, f2 = f2, f1 + f2
# print(f1, f2)
# f1, f2 = f2, f1 + f2
# print(f1, f2)
