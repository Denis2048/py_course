from abc import ABC, abstractmethod

# Абстрактный класс.
class Store(ABC):
    @abstractmethod
    def add_product(self, name, price):
        pass

    @abstractmethod
    def remove_product(self, name):
        pass

    @abstractmethod
    def get_product(self, name):
        pass

    @abstractmethod
    def list_products(self):
        pass
