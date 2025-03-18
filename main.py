from src import Character
import time
player1 = Character.Character("john")
player2 = Character.Character("karen")

while not player1.is_dead and not player2.is_dead:
    player1.attack(player2)
    if not player2.is_dead:
        player2.attack(player1)
    time.sleep(1)

if player1.is_dead:
    print(player2.name + "won !")
else:
    print(player1.name + "won !")