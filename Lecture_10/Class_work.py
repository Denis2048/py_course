# class Car:
#     def __init__(self, brand, vol):
#         self.brand = brand
#         self.volume = vol
#     def __str__(self):
#         return f"{self.brand}: {self.volume}"
#
#
# my_car = Car("VAZ", 1.8)
# print(my_car)


# class Car:
#     def __init__(kitty, brand, vol):
#         kitty.brand = brand
#         kitty.volume = vol
#     # def __str__(kitty):
#     #     return f"str - {kitty.brand}: {kitty.volume}"
#     def __repr__(kitty):
#         return f"repr - {kitty.brand}: {kitty.volume}"
#
#
# my_car = Car("VAZ", 1.8)
# print(my_car)
# #my_car
## my_car.volume = 12.5
## print(my_car)


# class Car:
#     counter = 0
#     def __init__(self, brand, vol):
#         self.brand = brand
#         self.volume = vol
#         Car.counter += 1
#     def __str__(self):
#         return f"{self.brand}: {self.volume}"
#     def __repr__(self):
#         return f"Inst of Car: \n\t{self.brand}.\n\tVolume: {self.volume}"
#

# print(Car.counter)
# my_car = Car("VAZ", 1.8)
# print(Car.counter)
# my_car = Car("VAZ", 1.8)
# print(Car.counter)
# print(my_car.counter)
# print(Car.__doc__)
# print(Car.__bases__)
# print(Car.__dict__)


# class Car:
#     counter = 0
#     def __init__(self, brand, vol):
#         self.brand = brand
#         self.volume = vol
#         Car.counter += 1
#     def drive(self, dist):
#         print(f"Я проехал {dist} километров")
#     def __str__(self):
#         return f"{self.brand}: {self.volume}"
#     def __repr__(self):
#         return f"Inst of Car: \n\t{self.brand}.\n\tVolume: {self.volume}"
#
#
# my_car = Car("VAZ", 1.8)
# my_car.drive(123)


## hasattr - Проверить есть ли атрибут.
## setattr
## getattr

# class Car:
#     counter = 0
#     def __init__(self, brand, vol):
#         self.brand = brand
#         self.volume = vol
#         Car.counter += 1
#     def drive(self, dist):
#         print(f"Я проехал {dist} километров")
#     def __str__(self):
#         return f"{self.brand}: {self.volume}"
#     def __repr__(self):
#         return f"Inst of Car: \n\t{self.brand}.\n\tVolume: {self.volume}"
#
#
# my_car = Car("VAZ", 1.8)
# print(my_car.brand)
# print(getattr(my_car, "brand"))
# print(getattr(my_car, "bra", False))
#
# if getattr(my_car, "brand") != False:
#     print(my_car.brand)
#
# print(hasattr(my_car, "brand"))
# print(hasattr(my_car, "brand"))
# if hasattr(my_car, "brand"):   # Синоним.
#     print(my_car.brand)
# else:
#     print(False)
#
# setattr(my_car, "bra", 1234)
# print(my_car.__dict__)
# setattr(my_car, "brand", "asdazsd")
# print(my_car.__dict__)
# my_car.hello = 333
# print(my_car.__dict__)


# class Animal:
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
#     def eat(self):
#         print(f"Животное {self.color} цвета кушает...")
#     def go(self):
#         print("Животное двигается...")
#     def sleep(self):
#         print("Zzzzzz...")
#
#
# class DomesticCat(Animal):
#     def __init__(self, name, color, age):
#         self.name = name
#         super().__init__(color, age)
#
#
# cat = DomesticCat("Dima", "black", 0)
# print(cat.color, cat.name, cat.age)
# cat.eat()
# cat.sleep()
# cat.go()


# class Animal:
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
#     def eat(self):
#         print(f"Животное {self.color} цвета кушает...")
#     def go(self):
#         print("Животное двигается...")
#     def sleep(self):
#         print("Zzzzzz...")
#
#
# class DomesticCat(Animal):
#     def __init__(self, name, color, age):
#         self.name = name
#         super().__init__(color, age)
#     def __repr__(self):
#         return f"Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"
#
#
# cat = DomesticCat("Dima", "black", 0)
# print(cat)


# class Animal:
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
#     def eat(self):
#         print(f"Животное {self.color} цвета кушает...")
#     def go(self):
#         print("Животное двигается...")
#     def sleep(self):
#         print("Zzzzzz...")
#
#
# class DomesticCat(Animal):
#     counter = 123
#     def __init__(self, name, color, age):
#         self.name = name
#         self.__id = DomesticCat.counter
#         DomesticCat.counter += 1
#         super().__init__(color, age)
#     def __repr__(self):
#         return f"Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"
#
#
# cat = DomesticCat("Dima", "black", 0)
# print(cat.__dict__)
# ##print(cat.__id)  # Err.
# print(cat._DomesticCat__id)


# class Animal:
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
#     def eat(self):
#         print(f"Животное {self.color} цвета кушает...")
#     def go(self):
#         print("Животное двигается...")
#     def sleep(self):
#         print("Zzzzzz...")
#
#
# class DomesticCat(Animal):
#     counter = 123
#     def __init__(self, name, color, age):
#         self.name = name
#         self.__id = DomesticCat.counter
#         DomesticCat.counter += 1
#         super().__init__(color, age)
#     def get_id(self):
#         print(f"cat id is: {self.__id}")
#     def __repr__(self):
#         return f"Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"
#
#
# cat = DomesticCat("Dima", "black", 0)
# cat.get_id()


# a = 10
# b = 11
# print(a+b)
# print(a.__add__(b))
# print(a.__sub__(b))
# print(a.__truediv__(b))
#
# s = "hdgfdc"
# s1 = ";kp;k;okl"
# print(s.__add__(s1))

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __add__(self, nextcat):
#         return self.age + nextcat.age
#     def __contains__(self, key):
#         return key in self.name
#     def __len__(self):
#         return self.age
#     def __lt__(self, nextcat):
#         return self.age < nextcat.age
#
#
# c = Cat("Cat", 5)
# c2 = Cat("Sany", 6)
# print(c + c2)
# print(len(c), len(c2))
# print(c < c2)
# print("d" in c)


# class Wallet:
#     def __init__(self, amount):
#         self.amount = amount
#     def __add__(self, int_value):
#         self.amount += int_value
#         return self.amount
#     def __sub__(self, int_value):
#         self.amount -= int_value
#         return self.amount - int_value
#     def __len__(self):
#         return self.amount
#
#
# my_wallet = Wallet(1000)
# my_wallet + 100
# print(len(my_wallet))
# my_wallet - 50
# print(len(my_wallet))
