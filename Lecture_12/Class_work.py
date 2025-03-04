# print()
# print(1,2,3)
#
# def Pront(*values):
#     print(type(values))
#     for val in values:
#         print(val, end=" ")
#     print()
#
#
# Pront([1,2,3,4])
# Pront("sdfdsfsdf")
# Pront(1,2,3,4)
# Pront(1,2,3,4, [1, 2, 3], "sdgfdfgdfgdfg")


# def Pront(*args, sep=" ", end="\n"):
#     for val in args:
#         print(val, end=sep)
#     print(end=end)
#
#
# Pront(1, 2, 3, 4, 5, [1,2,3,4], "sdfdsfsdfsdf")


# def balances(**balance):
#     print(balance)
#     print(type(balance))
#     for k, w in balance.items():
#         print("\t", k, ":", w)
#     print()
#
#
# balances(name="Vasia", cash=1232)


# def numbers(name="Joe", *args, **kwargs):
#     print(name)
#     print(args)
#     print(kwargs)
#
#
# numbers()   # Joe, (), {}.
# numbers("Vasia", 1, 2, 3, 4, 5, 6, "dsfdsfdsfsf", age=100, apples=99)


# def num_sum(*args):
#     s = 0
#     for i in args:
#         s += i
#     print(s)
#
#
# def numbers(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     num_sum(args)
#
#
# #numbers(1, 2, 3, 4, 5, 6)   # Err.


# def num_sum(*args):
#     print(args)
#     s = 0
#     for i in args:
#         s += i
#     print(s)
#
#
# def numbers(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     num_sum(*args)
#
#
# numbers(1, 2, 3, 4, 5, 6)


# li1, li2 = [1, 2, 3], [4, 5, 6]
# li3 = li1 + li2
# li3 = li1, li2
# li3 = [*li1, *li2]
# print(li3)
# st = "dfsdfsdfs"
# li = [*st]
# print(li)
# di = {"1":2, "2":3}
# di1 = {"11":22, "22":33}
# di3 = {**di, **di1}
# print(di3)


# def D(b, a, c):
#     return b**2-4*a*c
#
#
# lambda: 2   # def retTwo():
#             #    return 2
# (lambda: 2 )()
# lambda a, b, c: a*b-c
# (lambda a, b, c: a*b-c)(2, 3, 4)
#
# def coud(z, x, y, b, a, c):
#     return z+x+y + (lambda b,a,c: b**2-4*a*c)(b,a,c)
#
#
# print(coud(1, 2, 3, 4, 3, 5))


# li = [2, 3, 4, 5, 6]
# for i in li:
#     print(i)
#
# li_iter = iter(li)
# print(li_iter)
# print(next(li_iter))
# print(next(li_iter))
# print(next(li_iter))
# print(next(li_iter))
# print(next(li_iter))
# print(next(li_iter)) # Err stop.


# class PowFive:
#     def __init__(self, maxn):
#         self.maxn = maxn
#     def __iter__(self):
#         self.counter = 1
#         return  self
#     def __next__(self):
#         if self.counter <= self.maxn:
#             res = 5 ** self.counter
#             self.counter += 1
#             return res
#         raise StopIteration
#
#
# p = PowFive(15)
# p_iter = iter(p)
# print(next(p_iter))
# print(next(p_iter))
# print(next(p_iter))
# print(next(p_iter))
#
# p = PowFive(4)
# for i in p:
#     print(i)


# li = [i**2 for i in range(10)]
# print(li)
#
# gen = (i**2 for i in range(10))
# #print(gen)
# for val in gen:
#     print(val, end=" ")


# def retNumbers(n):
#     for i in range(n):
#         return i
#
#
# print(retNumbers(5))


# def retNumbers(n):
#     for i in range(n):
#         yield i**2
#
#
# r = retNumbers(5)
# print(r)
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))


# def mulFive(n):
#     return n*5
#
#
# li = [1, 2, 3, 4]
# res_li = list(map(mulFive, li))
# print(res_li)


# def a():
#     x = 10
#     def inner(number):
#         return number**x
#     return inner
#
#
# res = a()
# print(res)
# print(res(6))


# def numPowTwo():
#     num = 2
#     def inner():
#         nonlocal num
#         num **= 2
#         return num
#     return inner
#
#
# res = numPowTwo()
# print(res)
# print(res())
# print(res())
# print(res())
# print(res())
# print(res())


# class Nunber:
#     Num = 99
#     def get_number(self):
#         return 55
#
#
# n = Nunber()
# print(n.Num)
# print(n.get_number())
#
# def get_number(self):
#     return 55
#
#
# NumberFromType = type("NumberFromType", (object,), {"get_number":get_number, "Num":99, "name":"JOJO"})
# print(NumberFromType)
# nn = NumberFromType
# print(type(nn))
# print(nn.Num)
# print(nn.get_number)
