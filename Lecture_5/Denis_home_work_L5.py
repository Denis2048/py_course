# # Home work 5.1 A leap year.
# def is_year_leap(year):
#     """Является ли год високосным"""
#
#     if year % 4 != 0:
#         return False       # Если не високосный.
#     elif year % 100 == 0:
#         if year % 400 == 0:
#             return True    # Если високосный.
#         else:
#             return False   # Если не високосный.#
#     return True
#
#
# test_data = [1500, 1900, 2000, 2016, 1987, 2024, 2025]
# test_results = [False, False, True, True, False, True, False]
# for year, result in zip(test_data, test_results):
#     if is_year_leap(year) == result:
#         print(year, "is lear ? -->", result)
#     else:
#         print(year, "from your func -->", is_year_leap(year))
#         print("but expected -->", result)


# # Home work 5.4 Fibonacci numbers.
# def fibonachi(num):
#     """Числа Фибоначи"""
#
#     if num < 1:
#         return None
#     if num < 3:
#         return 1
#     f1, f2 = 1, 1
#     for i in range(2, num):
#         f1, f2 = f2, f1+f2
#     return f2
#
#
# for i in range(-1, 25):
#     num = i
#     print(fibonachi(num))

## Поиск числа ряда Фибоначи
# def fibonachi_search(n):
#     """Поиск числа ряда Фибоначи"""
#
#     i = 0
#     fib1, fib2 = 1, 1
#     while i < n - 2:   # Начало с третьего
#         fib1, fib2 = fib2, fib1 + fib2
#         i += 1
#     return fib2
#
#
# n = int(input("Введите номер элемента Фибоначи:"))
# print("Значение элемента:", fibonachi_search(n))
