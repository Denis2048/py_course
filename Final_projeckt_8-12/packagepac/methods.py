from packagepac import My_exeption as Ex
from packagepac import abstract_class as Ab


class Shop(Ab.Store):
    products = {}

    # Метод для добавления продукта.
    @classmethod
    def add_product(cls, name, price):
        # Проверка вводимого имени продукта.
        if not isinstance(name, str) or len(name) == 0:
            raise Ex.InvalidProductError("Название продукта не может быть пустым.")
        if not name.replace(" ", "").isalnum():
            raise Ex.InvalidProductError("Название продукта содержит недопустимые символы.")

        # Проверка вводимой цены.
        if isinstance(price, str):
            try:
                price = float(price)
            except ValueError:
                raise Ex.InvalidPriceError("Цена продукта должна быть числом.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise Ex.InvalidPriceError("Цена продукта должна быть положительным числом.")

        cls.products[name] = price
        return f"Продукт '{name}' добавлен в магазин."

    # Метод для удаления продукта.
    @classmethod
    def remove_product(cls, name):
        if name not in cls.products:
            raise Ex.ProductNotFoundError(name)
        del cls.products[name]
        return f"Продукт '{name}' удален из магазина."

    # Метод для поиска продукта.
    @classmethod
    def get_product(cls, name):
        if name not in cls.products:
            raise Ex.ProductNotFoundError(name)
        return f"Продукт: {name}, Цена: {cls.products[name]} by."

    # Метод для отображения списка продуктов.
    @classmethod
    def list_products(cls):
        if not cls.products:
            return "В магазине нет продуктов."
        return "\n".join([f"{name}: {price} buy." for name, price in cls.products.items()])
