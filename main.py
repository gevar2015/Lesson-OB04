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
# Класс монстра
class Monster:
    def __init__(self):
        """Инициализация монстра."""
        self.health = 10  # Здоровье монстра для простоты

    def take_damage(self, damage):
        """Монстр получает урон."""
        self.health -= damage
        if self.health <= 0:
            return "Монстр побежден!"
        else:
            return "Монстр все еще сражается."

# Функция для демонстрации боя
def battle(fighter, monster):
    print(f"Боец {fighter.attack()}.")
    print(monster.take_damage(10))
# Создание оружия
sword = Sword()
bow = Bow()

# Создание бойца с мечом
fighter = Fighter(sword)

# Создание монстра
monster = Monster()

# Бой мечом
battle(fighter, monster)

# Смена оружия на лук
fighter.change_weapon(bow)

# Новый монстр для следующего боя
monster = Monster()

# Бой луком
battle(fighter, monster)
