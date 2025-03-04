# class User:
#     __counter = 0
#     def __init__(self, name):
#         self.name = name
#         User.__counter += 1
#     @classmethod
#     def get_counter(cls):
#         return cls.__counter
#     def __str__(self):
#         return f"User name: {self.name}"
#
#
# print(User.get_counter())
# k = User("Kate")
# print(k)
# print(k.get_counter())
# print(User.get_counter())


# class User:
#     __counter = 0
#     def __init__(self, name):
#         self.name = name
#         User.__counter += 1
#     @classmethod
#     def get_counter(cls):
#         return cls.__counter
#     def set_counter(cls, value):
#         cls.__counter = value
#     def __str__(self):
#         return f"User name: {self.name}"
#
#
# k = User("Kate")
# print(k)
# print(User.get_counter())
# User.set_counter(88)
# print(User.set_counter())


# class User:
#     __counter = 0
#     def __init__(self, name):
#         self.name = name
#         User.__counter += 1
#     def __str__(self):
#         return f"User name: {self.name}"
#     @classmethod
#     def get_counter(cls):
#         return cls.__counter
#     @classmethod
#     def set_counter(cls, value):
#         cls.__counter = value
#     @staticmethod
#     def check_name(name):
#         return False if len(name) < 2 else True
#
#
# user1 = "Kate"
# if User.check_name(user1):
#     inst1 = User(user1)
# else:
#     print("Имя слишком короткое")
# print(inst1)


# class User:
#     __counter = 0
#     def __init__(self, name):
#         print("__init__")
#         self.name = name
#         User.__counter += 1
#     @classmethod
#     def init_age_including(cls, name, age):
#         print("__alt_init__")
#         user = cls(name)
#         user.age = age
#         return  user
#     def __str__(self):
#         return f"User name: {self.name}"
#     @classmethod
#     def get_counter(cls):
#         return cls.__counter
#     @classmethod
#     def set_counter(cls, value):
#         cls.__counter = value
#
#
# u1 = User("Vova")
# u2 = User.init_age_including("Vova", 19)
# User.get_counter()
# print(u1.name)
# print(u2.age)


## txt csv json xml
## prep export status
# from abc import ABC, abstractmethod
#
# class Export(ABC):
#     @abstractmethod
#     def export(self):
#         pass
#
#     @abstractmethod
#     def prep(self):
#         pass
#
#     @abstractmethod
#     def status(self):
#         pass
#
#
# class ExportToTXT(Export):
#     def __init__(self, file_name):
#         self.file_name = file_name
#     def export(self):
#         print("export to txt", self.file_name)
#     def prep(self):
#         print("prep")
#     def status(self):
#         print("status")
#
#
# class ExportToJSON(Export):
#     def __init__(self, file_name):
#         self.file_name = file_name
#     def export(self):
#         print("export to json", self.file_name)
#     def prep(self):
#         print("prep")
#     def status(self):
#         print("status")
#
#
# inst = ExportToTXT("1.txt")
# inst.status()
# inst.prep()
# inst.export()
# inst2 = ExportToJSON("2.json")
# inst2.status()
# inst2.prep()
# inst2.export()
#
# li = [ExportToTXT("1.txt"), ExportToTXT("3.txt"), ExportToJSON("2.json")]
# for inst in li:
#     inst.export()


# # MRO
# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# class C(B):
#     pass
#
#
# print(C.__mro__)
# print(C.mro)


# class A:
#     a = 10
#
# class B(A):
#     b = 100
#
# class C(B):
#     c = 1000
#
#
# c = C()
# c1 = C()
# print(c1.c)
# print(c1.b)
# print(c1.a)
# # print(c1.d) # Err.


# class A:
#     a = 10
#     def __init__(self):
#         self.aaa = 11
#
#
# class B(A):
#     b = 100
#     def __init__(self):
#         self.bbb = 111
#
#
# class C(B):
#     c = 1000
#     def __init__(self):
#         self.ccc = 1111
#         super().__init__()
#
#
# c1 = C()
# print(c1.c)
# print(c1.ccc)
# print(c1.b)
# print(c1.bbb)
# print(c1.a)
# #print(c1.aaa) # Err.


# try:
#     raise AttributeError
# except:
#     print("Err")
# else:
#     print("OK")
# finally:
#     print("fin")

# try:
#     1 + 1
# except:
#     print("Err")
# else:
#     print("OK")
# finally:
#     print("fin")


# def a(number):
#     try:
#         return number
#     except:
#         return number + 1
#     else:
#         return number + 2
#     finally:
#         return number ** 10
#
#
# print(a(10))


# class User:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"User name: {self.name}"
#     def call(self, number):
#         if len(number) < 8:
#             pass
#         return f"Звоню {number}"
#
#
# class NumberError(Exception):
#     def __init__(self, number, message):
#         self.number = number
#         self.message = message
#
# raise  NumberError(1231231, "Короткий номер")
