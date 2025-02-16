import random
import time
#import random as r
#from random import randint
#from random import randint as r

def main():
    """Основная логика"""

    menu = """
Игра 'Угадай число'. Выберите действие:
1 - Игра.
2 - Результаты.
2 - Выход '-1'
______________
"""

    oper = int(input(menu))
    while oper != -1:
        if oper == 1:
            game()
        elif oper == 2:
            print(f"Количество выигрышей - {list_of_res.count(1)}")
            print(f"Количество проигрышей - {list_of_res.count(2)}")
            print("------------------------")
        oper = int(input(menu))


def game():
    """Игра с записью результатов"""

    user_result = int(input("Введите целое число от 1 до 3\n"))
    while user_result != -1:
        comp_result = random.randint(1, 3)
        if user_result == comp_result:
            win_or_not = "Вы выйграли"
            list_of_res.append(1)
        else:
            win_or_not = "Вы проиграли"
            list_of_res.append(2)
        time.sleep(1)
        print(f"{win_or_not} \nКомпьютер загадал - {comp_result}")
        print("--------------------------")
        user_result = int(input("Введите целое число от 1 до 3\n"))


list_of_res = []
main()
