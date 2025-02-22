# class Car:
#     pass
#
# class Dog:
#     pass

# class Dog:
#     pass
# d = Dog()
# print(type(d))

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# d = Dog("Bobik", 34)
# print(type(d))
# print(isinstance(d, Dog))


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# d = Dog("Bobik", 34)
# print(type(d))
# print(isinstance(d, Dog))
# print(d.name)
# print(d.age)


# class Dog:
#     dog_counter = 0      # Переменная класса.
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Dog.dog_counter += 1
#
#
# d = Dog("Bobik", 34)
# c = Dog("Sosiska", 22)
# print(d.name)
# print(c.age)
# # Dog.name  # Error
# print(Dog.dog_counter)
# v = Dog("Bo", 2)
# print(v.dog_counter)


# class Dog:
#     dog_counter = 0      # Переменная класса.
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Dog.dog_counter += 1
#
#
# d = Dog("Ssds", 11)
# c = Dog("hjhj", 55)
# d.dog_counter = 555           # Создание свойства на лету.
# print(d.dog_counter)


# class Wallet:
#     """Представляет структуру полей для описания кошелька"""
#     counter = 0
#     def __init__(self, owner, currency, amount, adrres="", color="silver"):
#         self.owner = owner
#         self.currency = currency
#         self.amount = amount
#         self.adrres = adrres
#         self.color = color
#         Wallet.counter += 1
#         self.wallet_id = Wallet.counter * 10
#
#
# print(Wallet.counter)
# fw = Wallet("S F", "BYN", 1000)
# print(fw.wallet_id)
# print(fw.adrres)
# print(fw.color)
# print(fw.amount)
#
# sw = Wallet("D F", "RUB", 100000 , color="GOLD")
# print(sw.wallet_id)
# print(sw.adrres)
# print(sw.color)
# print(sw.amount)
#
# # Wallet.__doc__
# # Wallet.__name__
# # Wallet.__module__
# # Wallet.__bases__
#
# print(fw.__dict__)
# print(sw.__dict__)
# for k, v in fw.__dict__.items():
#     print(k, ":", v)


## Методы.

# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#     def hello(self, message):
#         print(f"{self.name} says {message}!")
#     def bye(self):
#         print(f"{self.name} says bye bye!")
#     def __str__(self):                           # Новый метод для печати красиво.
#         return f"User: name - {self.name}, email - {self.email}"
#
# dl = User("Dima", "@")
# print(dl.name)
# print(dl.hello("hello there"))
# print(dl.bye())
#
# st = "hello"
# print(st)
# print(dl)   # <__main__.User object at 0x00000268B6A3DC10>
# kate = User("Kate", "kate@mail.com")
# kate.bye()
# print(kate)

# print(dir(int))


# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#     def hello(self, message):
#         print(f"{self.name} says {message}!")
#     def bye(self):
#         print(f"{self.name} says bye bye!")
#     def __str__(self):                           # Новый метод для печати красиво.
#         return f"User: name - {self.name}, email - {self.email}."
#
#
# class Storage:
#     counter_id = 0
#     def __init__(self):
#         self.storage = {}
#     def add_user(self, user):
#         Storage.counter_id += 1
#         self.storage.update({Storage.counter_id:user})
#     def show_all(self):
#         for user_id, user in self.storage.items():
#             print(f"User id:{user_id}")
#             print(f"      Name: {user.name}")
#             print(f"      Email: {user.email}")
#             print(f"__str__")
#             print(user)
#             user.bye()
#
#
# strg = Storage()
# dima = User("Dima", "dfdfdf")
# kate = User("Kate", "aaaaaa")
# vasy = User("Vasy", "vvvv")
# strg.add_user(dima)
# strg.add_user(kate)
# strg.add_user(vasy)
# strg.show_all()


## Наследование
# class Car:
#     def __init__(self, vin, volume, model_name):
#         self.vin = vin
#         self.volume = volume
#         self.model_name = model_name
#     def __str__(self):
#         return "привет из родительского класса"
#
#
# class Sedan:
#     pass
#
# class Wagon:
#     pass
#
# print(Sedan.__bases__)
#
# class Sedan(Car):
#     pass
#
# class Wagon(Car):
#     pass
# print(Sedan.__bases__)
# print(Wagon.__bases__)
#
# s = Sedan("21215454545", 1.7, "Megane")
# print(s)
#
# print(isinstance(s, Sedan))
# print(isinstance(s, Car))


# class Car:
#     def __init__(self, vin, volume, model_name):
#         self.vin = vin
#         self.volume = volume
#         self.model_name = model_name
#     def __str__(self):
#         return "привет из родительского класса"
#     def drive(self):
#         print("Врум Врум")
#
# class Sedan(Car):
#     pass
#
# class Wagon(Car):
#     pass
#
# w = Wagon(654596646, 1.9, "256345")
# print(w.__dict__)
# print(Sedan.__dict__)
# print(Car.__dict__)
# w.drive()
#
# class Sedan(Car):
#     def drive(self):               # Переопределенный метод
#         print("Седан делает ыыыы")
#
# s = Sedan(132134866, 3.3, "sdfsdfsdfsdf")
# s.drive()

# class Car:
#     def __init__(self, vin, volume, model_name):
#         self.vin = vin
#         self.volume = volume
#         self.model_name = model_name
#     def __str__(self):
#         return "привет из родительского класса"
#     def drive(self):
#         print("Врум Врум")
#
#
# class Wagon(Car):
#     pass
#
#
# class Sedan(Car):
#     def drive(self):
#         super().drive()
#         print("Седан делает ыыыы")
#
#
# w = Wagon(654596646, 1.9, "256345")
# s = Sedan(132134866, 3.3, "sdfsdfsdfsdf")
#
# w.drive()
# s.drive()


# class Car:
#     def __init__(self, vin, volume, model_name):
#         self.vin = vin
#         self.volume = volume
#         self.model_name = model_name
#     def __str__(self):
#         return "привет из родительского класса"
#     def drive(self):
#         print("Врум Врум")
#     def show_car(self):
#         print(self.vin, self.volume, self.model_name)
#
#
# class Sedan(Car):
#     def __init__(self):
#         self.body_type = "Sedan"
#     def drive(self):
#         super().drive()
#
# # s = Sedan(132134866, 3.3, "sdfsdfsdfsdf")   # Ошибка.
# s = Sedan()
# print(s)
# s.drive()
# # s.show_car()  # Ошибка.


# class Car:
#     def __init__(self, vin, volume, model_name):
#         self.vin = vin
#         self.volume = volume
#         self.model_name = model_name
#     def __str__(self):
#         return "привет из родительского класса"
#     def drive(self):
#         print("Врум Врум")
#     def show_car(self):
#         print(self.vin, self.volume, self.model_name)
#
#
# class Sedan(Car):
#     def __init__(self, vin, volume, model_name):
#         self.body_type = "Sedan"
#         super().__init__(vin, volume, model_name)
#     def drive(self):
#         super().drive()
#         print("Седан делает ыыыыыыы")
#
#
# s = Sedan(132134866, 3.3, "sdfsdfsdfsdf")
# print(s.body_type)
# print(s.vin)
# print(s.volume)
# print(s.model_name)
# s.show_car()


# # Инкапсуляция.

# money = 21321654634536
# money = -321321213
#
# class wallet:
#     def __init__(self, money):
#         self.money = money
#
#
# wall = wallet(36546546464)
# wall.money = -132154654
# print(wall.money)


# class wallet:
#     def __init__(self, money):
#         self.__money = money
#
#
# wall = wallet(36546546464)
# print(wall.money)
# wall.money = - 20346546           # Ошибка атрибута.


# class wallet:
#     def __init__(self, money):
#         self.__money = money
#     def read(self, secret):
#         if secret == 123:
#             return self.__money
#         return "unauthorised"
#     def add(self, amount, secret):
#         if secret != 123:
#             return "unauthorised"
#         if amount > 0:
#             self.__money += amount
#         return "unauthorised"
#
#
# my_wallet = wallet(100)
# #print(my_wallet.money)    # Ошибка.
# print(my_wallet.read(123))
# print(my_wallet.add(123, 123))
# print(my_wallet.read(123))
