def display_menu():
    """Функция для отображения меню."""
    print("\033[32m****************")
    print("Меню:")
    for item_key, price in menu.items():
        print(f"{item_key}: {price:} $")
    print("****************\033[0m")


def add_order(order, item_key, quantity):
    """Функция для добавления заказа."""
    if item_key in menu:
        if item_key in order:
            order[item_key] += quantity
        else:
            order[item_key] = quantity
    else:
        print(f"Извините, {item_key} нет в меню.")


def remove_order(order, item_key):
    """Функция для удаления заказа."""
    if item_key in order:
        del order[item_key]
        print(f"{item_key} удален.")
    else:
        print(f"{item_key} не найден в заказе.")


def calculate_total(order):
    """Функция для расчета общей стоимости заказа."""
    total = 0
    print("--------------------\nВаш заказ:\n", end="")
    for item_key, quantity in order.items():    # Вывод заказа.
        print(f"{item_key}: - {quantity:}")

    for item_key, quantity in order.items():    # Подсчет результата.
        total += menu[item_key] * quantity
    return total


# Меню обедов
menu = {
    "Бургер": 5,
    "Пицца": 4,
    "Салат": 3,
    "Суп": 2,
    "Сок": 1,
}
