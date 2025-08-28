from abc import ABC, abstractmethod

# Product Interface
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# Concrete Products
class ProductA(Product):
    def operation(self) -> str:
        return "ProductA operation"

class ProductB(Product):
    def operation(self) -> str:
        return "ProductB operation"

# Factory Class
class Factory:
    def create_product(self, type_: str) -> Product:
        if type_ == "A":
            return ProductA()
        elif type_ == "B":
            return ProductB()
        else:
            raise ValueError("Unknown product type")

# Usage
factory = Factory()
product = factory.create_product("A")
print(product.operation())  # Output: ProductA operation
product = factory.create_product("B")
print(product.operation())  # Output: ProductB operation