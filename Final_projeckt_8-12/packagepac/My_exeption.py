class InvalidProductError(Exception):
    """Исключение для неверного продукта."""
    def __init__(self, message="Некорректные данные продукта."):
        self.message = message
        super().__init__(self.message)


class InvalidPriceError(Exception):
    """Исключение для неверной цены."""
    def __init__(self, message="Некорректная цена продукта."):
        self.message = message
        super().__init__(self.message)


class ProductNotFoundError(Exception):
    """Исключение для отсутствующего продукта."""
    def __init__(self, name, message=f"Продукт не найден."):
        self.name = name
        self.message = message
        super().__init__(self.message)
