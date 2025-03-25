from app.models import Knight, Armour, Potion
from app.weapons import METAL_SWORD, TWO_HANDED_SWORD, POISONED_SWORD, SWORD

LANCELOT = Knight(
    name="Lancelot",
    power=35,
    hp=100,
    armour=list(),
    weapon=METAL_SWORD,
    potion=None
)

ARTHUR = Knight(
    name="Arthur",
    power=45,
    hp=75,
    armour=[Armour(part="helmet", protection=15), Armour(part="breastplate", protection=20), Armour(part="boots", protection=10)],
    weapon=TWO_HANDED_SWORD,
    potion=None
)

MORDRED = Knight(
    name="Mordred",
    power=30,
    hp=90,
    armour=[Armour(part="breastplate", protection=15), Armour(part="boots", protection=10)],
    weapon=POISONED_SWORD,
    potion=Potion(name="Berserk", effect={"power": +15, "hp": -5, "protection": +10})
)

RED_KNIGHT = Knight(
    name="Red Knight",
    power=40,
    hp=70,
    armour=[Armour(part="breastplate", protection=25)],
    weapon=SWORD,
    potion=Potion(name="Blessing", effect={"power": +5, "hp": +10})
)