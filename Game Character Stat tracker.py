class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        # Cap health between 0 and 100
        self._health = max(0, min(100, value))

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        # Cap mana between 0 and 50
        self._mana = max(0, min(50, value))

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1
        # Reset health and mana using the property setters
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Level: {self.level}\n"
                f"Health: {self.health}\n"
                f"Mana: {self.mana}")

# --- Example Usage ---
hero = GameCharacter('Kratos')
print(hero)

hero.health -= 30
hero.mana -= 10
print(f"\nStats after damage:\n{hero}")

hero.level_up()
print(f"\nStats after level up:\n{hero}")