from abc import ABC, abstractmethod

# Base Component
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass

# Concrete Component
class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Email: {message}")

# Base Decorator
class NotifierDecorator(Notifier):
    def __init__(self, notifier: Notifier):
        self._notifier = notifier
    def send(self, message: str) -> None:
        self._notifier.send(message)

# Concrete Decorator A
class SMSNotifier(NotifierDecorator):
    def send(self, message: str) -> None:
        super().send(message)
        print(f"SMS: {message}")

# Concrete Decorator B
class SlackNotifier(NotifierDecorator):
    def send(self, message: str) -> None:
        super().send(message)
        print(f"Slack: {message}")

# Usage
notifier = EmailNotifier()
notifier = SMSNotifier(notifier)
notifier = SlackNotifier(notifier)
notifier.send("Decorator works!")