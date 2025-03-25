class Armour:
    def __init__(self, part: str, protection: int):
        self.part = part
        self.protection = protection

    def __getitem__(self, key):
        if hasattr(self, key):
            return getattr(self, key)
        raise KeyError(f"Attribute '{key}' not found")

    def __setitem__(self, key, value):
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            raise KeyError(f"Cannot set unknown attribute '{key}'")

class Weapon:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    def __getitem__(self, key):
        if hasattr(self, key):
            return getattr(self, key)
        raise KeyError(f"Attribute '{key}' not found")

    def __setitem__(self, key, value):
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            raise KeyError(f"Cannot set unknown attribute '{key}'")


class Potion:
    def __init__(self, name: str, effect: dict[str, int]):
        self.name = name
        self.effect = effect


class Knight:
    protection = 0

    def __init__(self, name: str, power: int, hp: int, armour: list[Armour], weapon: Weapon, potion: Potion | None):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self):
        """Применить броню к персонажу."""
        self.protection = sum(a.protection for a in self.armour)

    def apply_weapon(self):
        """Применить оружие к персонажу."""
        self.power += self.weapon.power

    def apply_potion(self):
        """Применить зелье к персонажу (если оно есть)."""
        if self.potion:
            for key, value in self.potion.effect.items():
                if hasattr(self, key):
                    setattr(self, key, getattr(self, key) + value)

    def __getitem__(self, key):
        if hasattr(self, key):
            return getattr(self, key)
        raise KeyError(f"Attribute '{key}' not found")

    def __setitem__(self, key, value):
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            raise KeyError(f"Cannot set unknown attribute '{key}'")

    def __str__(self):
        armour_names = ', '.join(a.part for a in self.armour) if self.armour else "None"
        potion_name = self.potion.name if self.potion else "None"
        return (f"Name: {self.name}, Power: {self.power}, HP: {self.hp}, "
                f"armour: {armour_names}, Weapon: {self.weapon.name}, Potion: {potion_name}, Protection: {self.protection}")

