from packagepac import My_exeption as Ex
from packagepac import methods as Md


class App:
    """Класс для взаимодействия с пользователем."""
    @staticmethod
    def run():
        while True:
            print("\n==== Меню магазина ====")
            print("1 - Добавить продукт")
            print("2 - Удалить продукт")
            print("3 - Найти продукт")
            print("4 - Список всех продуктов")
            print("5 - Выйти")
            print("=" * 23)
            choice = input("Выберите действие: ")

            if choice == '1':
                try:
                    name = input("Введите название продукта: ")
                    price = input("Введите цену продукта: ")
                    print(Md.Shop.add_product(name, price))
                except Ex.InvalidProductError as e:
                    print(f"Ошибка: {e}")
                except Ex.InvalidPriceError as e:
                    print(f"Ошибка: {e}")

            elif choice == '2':
                try:
                    name = input("Введите название продукта для удаления: ")
                    print(Md.Shop.remove_product(name))
                except Ex.ProductNotFoundError as e:
                    print(f"Ошибка: {e}")

            elif choice == '3':
                try:
                    name = input("Введите название продукта для поиска: ")
                    print(Md.Shop.get_product(name))
                except Ex.ProductNotFoundError as e:
                    print(f"Ошибка: {e}")

            elif choice == '4':
                print("\nСписок продуктов:")
                print(Md.Shop.list_products())

            elif choice == '5':
                print("Выход из программы.")
                break
            else:
                print("Некорректный выбор. Попробуйте снова.")
