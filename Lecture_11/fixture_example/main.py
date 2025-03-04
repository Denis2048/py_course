from mobile_phone import MobilePhone


def menu():
    """Пользовательское меню."""
    print("\nМеню:")
    print("1 - Включить телефон")
    print("2 - Выключить телефон")
    print("3 - Позвонить")
    print("4 - Выход")


def main():
    """Основная логика."""
    my_phone = MobilePhone("123-456-789")
    while True:
        menu()
        choice = input("Выберите команду: ")
        if choice == "1":
            print(my_phone.turn_on())
        elif choice == "2":
            print(my_phone.turn_off())
        elif choice == "3":
            print(my_phone.call("123-456-789"))
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверная команда.")


if __name__ == "__main__":
    main()
