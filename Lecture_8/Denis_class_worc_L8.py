# print(1/0)          # Ошибки.
# s = "dfdfdf"
# print(s.capitalize())
# print(s.decapitalize())
# li = [1, 2, 3]
# print(li[0.5])

# try:
#     print(1 / 0)
# except:
#     print("Error")
# print(12)

# try:
#     li = [1, 2, 3]
#     print(li[0.5])
# except:
#     print("Error")
# print(12)

# try:
#     print(1 / 0)
# except ValueError:
#     print("ValueError")
# except:                    # Идет всегда последней.
#     print("Error")

# try:
#     print(1 / 0)
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except ValueError:
#     print("ValueError")
# except:
#     print("Error")

# try:
#     try:
#         print(1 / 0)
#     except ZeroDivisionError:
#         print("ZeroDivisionError")
#     except ValueError:
#         print("ValueError")
#     except:
#         print("Error")
# except:
#     print("Error")

# try:
#     raise  ZeroDivisionError("sfsdfsdfdsfsdf")       # Вызов ошибки.
# except ZeroDivisionError as zde:                     # Передача ошибки.
#     print("ZeroDivisionError", zde.args)
# except:
#     print("Error")

# try:
#     print(1 / 0)
# except (ZeroDivisionError, ValueError):
#     print("ZeroDivisionError or ValueErro")

# a = 6
# if a == 8:
#     try:
#         import time
#     except:
#         pass
# else:
#     print("Делай без модуля time")

# a = 8
# if a == 8:
#     try:
#         import time
#     except:
#         pass
# else:
#     print("Делай без модуля time")
# time.sleep(2)

# try:
#     raise ZeroDivisionError # 1/0
# except ArithmeticError:
#     print("ArithmeticError")
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except:
#     print("default")

# try:                                  # Сверху всегда конкретные исключения.
#     raise ZeroDivisionError # 1/0
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except ArithmeticError:
#     print("ArithmeticError")
# except:
#     print("default")

# def a(x):
#     try:
#         res = int(x)
#     except:
#         print("123")
#         raise
#
#
# print(a(123))
# print(a("222"))

# assert 1
# assert 0  # Err
# assert [] # Err

# res = 10
# assert res == 10
# res = 11
# assert res == 10   # AssertionError
