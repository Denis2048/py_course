# Lab bmi
def bmi(weight, height):
    """Расчет индекса массы тела."""

    return weight / (height/100)**2


def bmi_interpretation(res_of_bmi):
    """Интерпретация показателей ИМТ."""

    if res_of_bmi < 18.5:
        return "Дефицит массы тела"
    elif res_of_bmi >= 18.5 and res_of_bmi <= 24.99:
        return "Норма"
    elif res_of_bmi >= 25 and res_of_bmi <= 29.99:
        return "Избыточная масса тела (предожирение)"
    elif res_of_bmi >= 30 and res_of_bmi <= 34.99:
        return "Ожирение первой степени"
    elif res_of_bmi >= 35 and res_of_bmi <= 39.99:
        return "Ожирение второй степени"
    elif res_of_bmi >= 40:
        return "Ожирение третьей степени (морбидное)"


print("************************************\n\
Программа расчета индекса массы тела. \n\
Для корректной работы введите \n\
вес в килограммах и рост в сантиметрах.\n\
Для выхода введите '-1'\n\
******************************************")
while True:
    weight, height = float(input("Вес -> ")), float(input("Рост -> "))
    if (weight == -1) or (height == -1):
        print("Выход")
        break
    elif (weight <= 0) or (height <= 0):
        print("Неверные данные\n------------------")
    else:
        res_of_bmi = bmi(weight, height)
        print(f"Ваш ИМТ = {"%.2f" % res_of_bmi} \
({bmi_interpretation(res_of_bmi)}) \n------------------")
