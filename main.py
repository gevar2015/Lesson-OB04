from abc import ABC, abstractmethod

# Абстрактный класс оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        """Метод для выполнения атаки, специфичный для каждого оружия."""
        pass
