import re
import itertools

def hit(attacker, defender):
    defender["Hit Points"] -= max(attacker["Damage"] - defender["Armor"], 1)

def fight(player, boss):
    while(True):
        hit(player, boss)
        if boss["Hit Points"] <= 0:
            win = True
            break
        hit(boss, player)
        if player["Hit Points"] <= 0:
            win = False
            break
    return win

with open('shop.txt') as f:
    d_shop = f.readlines()
    d_shop = [x.strip() for x in d_shop]

shop = {}

for row in d_shop:
    if row == '':
        continue
    if "Weapons" in row or "Armor" in row or "Rings" in row:
        category = re.search(r"^.*(?=:)", row).group(0)
        shop[category] = {}
        continue
    item, cost, damage, armor = re.split(r"\W+(?=\s\s)", row) 
    cost = int(cost)
    damage = int(damage)
    armor = int(armor)
    shop[category][item] = {"cost": cost, "damage": damage, "armor": armor}

shop["Armor"]["None"] = {"cost": 0, "damage": 0, "armor": 0}
shop["Rings"]["None1"] = {"cost": 0, "damage": 0, "armor": 0}
shop["Rings"]["None2"] = {"cost": 0, "damage": 0, "armor": 0}

with open("boss.txt") as f:
    d_boss = f.readlines()
    d_boss = [x.strip() for x in d_boss]

boss = {}

for row in d_boss:
    stat, val = row.split(": ")
    boss[stat] = int(val)

max_cost = 0

for weapon in shop["Weapons"]:
    for armor in shop["Armor"]:
        for rings in itertools.combinations(shop["Rings"], 2):
            player = {"Hit Points": 100, "Damage":0, "Armor": 0}
            cost = shop["Weapons"][weapon]["cost"] + shop["Armor"][armor]["cost"] + shop["Rings"][rings[0]]["cost"] + shop["Rings"][rings[1]]["cost"]
            player["Damage"] += shop["Weapons"][weapon]["damage"] + shop["Armor"][armor]["damage"] + shop["Rings"][rings[0]]["damage"] + shop["Rings"][rings[1]]["damage"]
            player["Armor"] += shop["Weapons"][weapon]["armor"] + shop["Armor"][armor]["armor"] + shop["Rings"][rings[0]]["armor"] + shop["Rings"][rings[1]]["armor"]
            if not fight(player, boss.copy()):
                max_cost = max(max_cost, cost)

print(max_cost)