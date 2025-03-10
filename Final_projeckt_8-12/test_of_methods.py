import pytest
from packagepac import My_exeption as Ex
from packagepac import methods as Md


# Фикстура с предустановленными продуктами.
@pytest.fixture
def shop_with_products():
    Md.Shop.products = {"Apple": 100.0, "Banana": 50.0}
    return Md.Shop


# Фикстура для тестовых данных.
@pytest.fixture
def product_data():
    return {"name": "Orange", "price": 75.0}


def test_add_product(shop_with_products, product_data):
    """Проверка добавления продукта."""
    result = shop_with_products.add_product(product_data["name"], product_data["price"])
    assert result == f"Продукт '{product_data['name']}' добавлен в магазин."
    assert product_data["name"] in shop_with_products.products
    assert shop_with_products.products[product_data["name"]] == product_data["price"]


def test_add_product_invalid_name(shop_with_products):
    """Проверка добавления продукта с недопустимым именем."""
    with pytest.raises(Ex.InvalidProductError):
        shop_with_products.add_product("", 100)


def test_add_product_invalid_price(shop_with_products, product_data):
    """Проверка добавления продукта с недопустимой ценой."""
    with pytest.raises(Ex.InvalidPriceError):
        shop_with_products.add_product(product_data["name"], "abc")


def test_remove_product(shop_with_products):
    """Проверка удаления продукта."""
    result = shop_with_products.remove_product("Apple")
    assert result == "Продукт 'Apple' удален из магазина."
    assert "Apple" not in shop_with_products.products


def test_remove_product_not_found(shop_with_products):
    """Проверка удаления несуществующего продукта."""
    with pytest.raises(Ex.ProductNotFoundError):
        shop_with_products.remove_product("Unknown")


def test_get_product(shop_with_products):
    """Проверка поиска продукта."""
    result = shop_with_products.get_product("Banana")
    assert result == "Продукт: Banana, Цена: 50.0 by."


def test_list_products(shop_with_products):
    """Проверка списка продуктов."""
    result = shop_with_products.list_products()
    assert result == "Apple: 100.0 buy.\nBanana: 50.0 buy."
