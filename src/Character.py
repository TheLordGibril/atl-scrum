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
            # Determine if attack is a critical hit
            is_critical = random.randint(1, 100) <= self.critical_chance

            # Calculate damage
            damage_to_deal = self.damage * 2 if is_critical else self.damage

            # Deal damage
            enemy.receive_damage(damage_to_deal)

            # Print appropriate message
            if is_critical:
                print(f"{self.name} lands a CRITICAL HIT on {enemy.name} for {damage_to_deal} damage points!")
            else:
                print(f"{self.name} attacks {enemy.name} for {damage_to_deal} damage points")
        else:
            print(f"{self.name} cannot attack because they are dead")


    def receive_damage(self, damage: int):
        self.hp -= damage
        print(self.name + " received " + damage + " points of damage")
        if self.hp <= 0:
            self.is_dead = True
            print(self.name + " is dead")