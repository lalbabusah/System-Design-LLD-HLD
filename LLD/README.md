# SOLID Principles

SOLID is a set of five design principles for writing maintainable and scalable software:

**S: Single Responsibility Principle (SRP)**
A class should have only one reason to change.
```python
class Message:
    def format(self):
        pass
```

**O: Open/Closed Principle (OCP)**
Software entities should be open for extension, but closed for modification.
```python
class Notifier:
    def send(self):
        pass
class SMSNotifier(Notifier):
    def send(self):
        print("SMS sent")
```

**L: Liskov Substitution Principle (LSP)**
Subtypes must be substitutable for their base types.
```python
class Shape:
    def draw(self):
        pass
class Square(Shape):
    def draw(self):
        print("Drawing square")
```

**I: Interface Segregation Principle (ISP)**
Clients should not be forced to depend on interfaces they do not use.
```python
class Drawable:
    def draw(self):
        pass
class Colorable:
    def color(self):
        pass
```

**D: Dependency Inversion Principle (DIP)**
Depend on abstractions, not on concretions.
```python
class Sender(ABC):
    def send(self):
        pass
class MessageService:
    def __init__(self, sender: Sender):
        self.sender = sender
```
