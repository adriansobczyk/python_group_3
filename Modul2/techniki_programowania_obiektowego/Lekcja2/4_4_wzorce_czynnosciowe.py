'''
Wzorce czynnosciowe w Pythonie
'''

# POLECENIE
from abc import ABC, abstractmethod

# Interfejs komendy
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Konkretna implementacja komendy
class ConcreteCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.action()

# Odbiorca (obiekt, na którym wykonywane są akcje)
class Receiver:
    def action(self):
        print("Akcja wykonana przez odbiorcę")

# Wyzwalacz
class Invoker:
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def execute_command(self):
        self._command.execute()

# receiver = Receiver()
# command = ConcreteCommand(receiver)
# invoker = Invoker()
# invoker.set_command(command)
# invoker.execute_command()


# OBSERWATOR

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Observer:
    def update(self, subject):
        pass


# Konkretny Subject
class ConcreteSubject(Subject):
    def __init__(self, state=None):
        super().__init__()
        self._state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
        self.notify()


# Konkretny Observer
class ConcreteObserver(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, subject):
        print(f"{self._name} otrzymał aktualizację. Nowy stan: {subject.state}")


subject = ConcreteSubject()
observer1 = ConcreteObserver("Obserwator 1")
observer2 = ConcreteObserver("Obserwator 2")
subject.attach(observer1)
subject.attach(observer2)
subject.state = 123
subject.state = "Nowy stan"
