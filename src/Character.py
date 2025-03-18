from typing import Self

class Character:
    def __init__(self):
        self.name: str = ""
        self.hp: int = 100
        self.damage: int = 5
        self.critical_chance: int = 5
        self.is_dead: bool = False

    def attack(self, enemy: Self):
        if not self.is_dead:
            enemy.receive_damage(self.damage)
            print(self.name + " attacks " + enemy.name + " for " + self.damage + " points of damage")
        else:
            print(self.name + " cannot attack because is dead")


    def receive_damage(self, damage: int):
        self.hp -= damage
        print(self.name + " received " + damage + " points of damage")
        if self.hp <= 0:
            self.is_dead = True
            print(self.name + " is dead")