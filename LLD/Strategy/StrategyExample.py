from abc import ABC, abstractmethod

# Strategy Pattern Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        """Process the payment of the given amount."""
        pass

# Concrete Strategy for Credit Card payment
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        """Process the payment using a credit card."""
        print(f"Paid {amount} using Credit Card.")

# Concrete Strategy for PayPal payment
class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        """Process the payment using PayPal."""
        print(f"Paid {amount} using PayPal.")

# Context that uses a PaymentStrategy
class ShoppingCart:
    def __init__(self, strategy: PaymentStrategy):
        """Initialize the shopping cart with a payment strategy."""
        self.strategy = strategy

    def checkout(self, amount: float):
        """Checkout and pay the given amount using the selected strategy."""
        self.strategy.pay(amount)

# Usage example
if __name__ == "__main__":
    cart = ShoppingCart(CreditCardPayment())
    cart.checkout(100)  # Paid 100 using Credit Card.
    cart.strategy = PayPalPayment()
    cart.checkout(200)  # Paid 200 using PayPal.