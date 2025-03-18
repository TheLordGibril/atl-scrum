from typing import Self

class Character:
    def __init__(self, name: str = "Character"):
        self.name: str = name
        self.hp: int = 100
        self.damage: int = 5
        self.critical_chance: int = 5
        self.is_dead: bool = False

    def attack(self, enemy: Self):
        if not self.is_dead:
            enemy.receive_damage(self.damage)
            print(f"{self.name} attacks {enemy.name} for {self.damage} damage points")
        else:
            print(f"{self.name} cannot attack because they are dead")


    def receive_damage(self, damage: int):
        self.hp -= damage
        remaining_hp = max(0, self.hp)
        print(f"{self.name} received {damage} damage points ({remaining_hp} HP remaining)")
        if self.hp <= 0:
            self.is_dead = True
            print(f"{self.name} is dead")