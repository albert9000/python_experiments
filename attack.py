import random

class Enemy:
    hp = 200

    def __init__(self, low, high):
        self.low = low
        self.high = high

    def get_attack(self):
        print(self.low)

    def get_hp(self):
        print(self.hp)

enemy1 = Enemy(60, 80)
enemy1.get_attack()
enemy1.get_hp()

enemy2 = Enemy(40, 60)
enemy2.get_attack()
enemy2.get_hp()
'''

playerhp = 260
low = 60
high = 80

while playerhp > 0:
    dmg = random.randrange(low, high)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("Attack for ", dmg, "points. Current health", playerhp)

    if playerhp > 30:
        continue

    print("you've taken too much damage, take a break")
    break;
'''
