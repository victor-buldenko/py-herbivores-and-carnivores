from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.hidden = False
        self.health = health
        Animal.add_alive(self)

    @classmethod
    def isdead(cls, inst: Animal) -> None:
        if inst.health <= 0:
            cls.alive = [animal for animal in cls.alive if animal != inst]

    @classmethod
    def add_alive(cls, inst: Animal) -> None:
        if inst.health > 0:
            cls.alive.append(inst)

    def __repr__(self) -> str:
        return (f"{{"
                f"Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, victim: Herbivore) -> None:
        if not victim.hidden and isinstance(victim, Herbivore):
            victim.health -= 50

        Animal.isdead(victim)
