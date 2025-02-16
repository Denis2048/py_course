"""
Задача: Создать программу "Студенты", которая может добавлять, удалять,
выводить список студентов, добавлять оценки, считать средний балл.
Автор: Denis
Описание: программа 'Студенты' создает словарь, содержащий данные
о студентах: имя, оценка. Имеет возможность добавлять, удалять,
выводить список студентов, добавлять оценки, считать средний балл.
"""

def add_new_student():
    """Функция добавления студента."""

    name = input("Введите имя: ")
    if name not in school_class:
        school_class[name] = ()
        print(f"Студент {name} успешно создан")
    else:
        print("Уже был создан")


def add_grade():
    """Функция добавления оценок."""

    name = input("Введите имя: ")
    if name in school_class:
        grade = int(input("Оценки (1-10):"))
        school_class[name] += (grade,)
        print("Оценка добавлена")
    else:
        print("Студента еще не существует")


def avg():
    """Функция расчета среднего балла."""

    if len(school_class) == 0:
        print("Оценок не содержится")
    elif len(school_class) > 0:
        for name in school_class.keys():
            grades = school_class[name]
            if len(grades) > 0:
                print("--------------------------")
                print(f"Студент - {name} \nВсе оценки - {school_class[name]}")
                print(f"Средний балл: {sum(grades) / len(grades)}")
                print("--------------------------")
            else:
                print(f"У {name} нет оценок")


def del_student():
    """Функция удаления студентов."""

    name = input("Введите имя: ")
    if name in school_class:
        print(school_class.pop(name))
        print(f"Студент {name} удален")
    else:
        print(f"Студента {name} не существует")


def student_list():
    """Функция вывода списка студентов."""

    number = 1
    if len(school_class) != 0:
        for name_of_student in school_class.keys():
            print(f"№ {number} - {name_of_student}")
            number += 1
    else:
        print("Список студентов пуст")


def main():
    """Основная логика"""

    menu = """
1 - Добавить нового студента.
2 - Добавить оценку.
3 - Посчитать средний бал.
4 - Удалить студента.
5 - Вывести список студентов.
-1 - Выход\n-------------------\n"""

    oper = int(input(menu))
    while oper != -1:
        if oper == 1:
            add_new_student()
        elif oper == 2:
            add_grade()
        elif oper == 3:
            avg()
        elif oper == 4:
            del_student()
        elif oper == 5:
            student_list()
        oper = int(input(menu))


school_class = {}
main()
