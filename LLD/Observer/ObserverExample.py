from abc import ABC, abstractmethod
from typing import List

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass

# Subject interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass
    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass
    @abstractmethod
    def notify(self, message: str) -> None:
        pass

# Concrete implementation of Subject
class ConcreteSubject(Subject):
    def __init__(self):
        self._observers: List[Observer] = []
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)

# Concrete implementation of Observer
class ConcreteObserver(Observer):
    def update(self, message: str) -> None:
        print(f"Observer received: {message}")

# Usage example
subject = ConcreteSubject()
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()
subject.attach(observer1)
subject.attach(observer2)
subject.notify("Event happened!")