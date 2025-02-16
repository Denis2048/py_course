school_class = {}
# name = input("name:")
# #{name:grades, name:grades}
#
# grade = int(input("grade:"))
# school_class[name] = (grade, )
# #school_class[name] = (grade, ) += (grade, )
# #sum(school_class[name]/len(school_class[name]))
menu = """
1 - Добавить нового студента
2 - Добавить оценку
3 - Посчитать средний бал
-1 - Выход"""

oper = int(input(menu))
while oper != -1:
    if oper == 1:
        name = input("name:")
        if name not in school_class:
            school_class[name] = ()
            print("Студент успешно создан")
        else:
            print("Уже был создан")
    elif oper == 2:
        name = input("name:")
        if name in school_class:
            grade = int(input("grade (1-10):"))
            school_class[name] += (grade,)
            print("Оценка добавлена")
        else:
            print("Студента еще не существует")
    elif oper == 3:
        if len(school_class) == 0:
            print("Оценок не содержится")
        elif len(school_class) > 0:
            for name in school_class.keys():
                grades = school_class[name]
                if len(grades) > 0:
                    print(name)
                    print(school_class[name])
                    print("avg:")
                    print(sum(grades)/len(grades))
                else:
                    print("У", name, "нет оценок")
    oper = int(input(menu))
