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
# Класс бойца
class Fighter:
    def __init__(self, weapon: Weapon):
        """Инициализация бойца с начальным оружием."""
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        """Метод для смены оружия бойца."""
        self.weapon = weapon

    def attack(self):
        """Боец атакует, используя выбранное оружие."""
        return self.weapon.attack()
