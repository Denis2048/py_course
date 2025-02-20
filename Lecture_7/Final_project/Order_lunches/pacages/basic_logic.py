from pacages import function as fn

def main():
    """Основная логика."""
    order = {}
    choice = int(input("Что бы вы хотели сделать? \
             \n1 - Заказать\n2 - Удалить заказ\n3 - Итого\n4 - Выход\n"))
    while choice != 4:
        if choice == 1:
            fn.display_menu()
            item_key = input("Введите название блюда: ")
            quantity = int(input("Введите количество: "))
            fn.add_order(order, item_key, quantity)

        elif choice == 2:
            if not order:
                print("Вы еще ничего не заказали")
            else:
                fn.display_menu()
                item_key = input("Введите название блюда для удаления: ")
                fn.remove_order(order, item_key)

        elif choice == 3:
            total = fn.calculate_total(order)
            print(f"\nИтого: {total:} $")
            print("--------------------")

        choice = int(input("\nЧто бы вы хотели сделать? \
                \n1 - Заказать\n2 - Удалить заказ\n3 - Итого\n4 - Выход\n"))
    print("Спасибо за заказ!")
