from abc import ABC, abstractmethod

# Абстрактный класс оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        """Метод для выполнения атаки, специфичный для каждого оружия."""
        pass
# Класс меча
class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

# Класс лука
class Bow(Weapon):
    def attack(self):
        return "наносит удар из лука"
