class Character:
    def __init__(self):
        self.hp = 100
        self.attack = 5
        self.est_mort = False

    def get_hp(self):
        return self.hp

    def attack(self, enemy):
        if not self.est_mort:
            enemy.received_damage(self.attack)

    def received_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.est_mort = True