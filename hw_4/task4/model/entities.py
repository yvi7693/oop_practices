from __future__ import annotations
from hw_4.task4.model.constants import *
import random


class Spell:

    __name: str
    __effect: str
    __mana: int

    def __init__(self, name: str, effect: str, mana: int):
        self.__name = name
        self.__effect = effect
        self.__mana = mana

    def __str__(self):
        return (f"name: {self.__name}"
                f"effect: {self.__effect}"
                f"mana: {self.__mana}")

    def cast(self, target: HogwartsStudent, sender: HogwartsStudent) -> None:
        if self.__effect == DISARMAMENT:
            target.forget_spells()

        elif self.__effect == DEAD:
            target.set_mana(0)

        elif self.__effect == SHIELD:
            sender.apply_effect(SHIELD)

        elif self.__effect == STUN:
            target.apply_effect(STUN)

    def get_name(self) -> str:
        return self.__name

    def get_effect(self) -> str:
        return self.__effect

    def __get_mana(self) -> int:
        return self.__mana

    @staticmethod
    def record(original: Spell) -> Spell:
        return Spell(original.__name, original.__effect, original.__mana)

    mana = property(__get_mana)


class HogwartsStudent:

    __name: str
    __house: str
    __mana: int
    __effect: str
    __spells = list[Spell]

    def __init__(self, name: str, house: str, spells: list[Spell], effect = None):
        self.__name = name
        self.__house = house
        self.__mana = 100
        self.__spells = spells
        self.__effect = effect

    def __str__(self):
        return (f"name: {self.__name}"
                f"house: {self.__house}"
                f"mana: {self.__mana}"
                f"effect: {self.__effect}"
                f"spells: {self.__spells}")

    def get_name(self) -> str:
        return self.__name

    def get_house(self) -> str:
        return self.__house

    def __get_mana(self) -> int:
        return self.__mana

    def get_effect(self) -> str:
        return self.__effect

    def get_spells(self) -> list[Spell]:
        record_spells = []

        for spell in self.__spells:
            record_spells.append(Spell.record(spell))

        return record_spells

    def set_mana(self, new_mana: int) -> None:
        self.__mana = new_mana

    def apply_effect(self, effect: str|None) -> None:
        self.__effect = effect

    def learn_spell(self, spell: Spell) -> None:
        if spell in self.__spells: raise ValueError("This spell is in the spells")

        self.__spells.append(spell)

    def forget_spells(self) -> None:
        self.__spells = []

    def try_cast_spell(self, target: HogwartsStudent) -> bool:
        random_spell = random.randint(0, len(self.__spells) - 1)
        spell = self.__spells[random_spell]

        if self.__mana < spell.mana: return False

        spell.cast(target, self)
        self.__mana -= spell.mana

        return True

    mana = property(__get_mana)


class Hogwarts:

    __students: list[HogwartsStudent]
    __spells: list[Spell]

    def __init__(self, students: list[HogwartsStudent], spells: list[Spell]):
        self.__students = students
        self.__spells = spells

    def enroll_student(self, student: HogwartsStudent) -> None:
        self.__students.append(student)

    def teach_spell(self, spell: Spell) -> None:
        self.__spells.append(spell)

    def simulate_duel(self, attacker: HogwartsStudent, defender: HogwartsStudent) -> None:
        while attacker.mana > 0 and defender.mana > 0:
            if attacker.get_effect() != STUN or defender.get_effect() == SHIELD:
                print("Пропуск хода")
                attacker, defender = defender, attacker
                continue

            if attacker.try_cast_spell(defender):
                attacker, defender = defender, attacker

            else:
                print("Закончилась манна")








