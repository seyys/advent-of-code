import copy
import numpy as np

class game_state:
    spells = {"Magic Missile": {"MP": 53, "Damage": 4, "Healing": 0, "Effects": None, "Duration": 0},
                   "Drain": {"MP": 73, "Damage": 2, "Healing": 2, "Effects": None, "Duration": 0},
                   "Shield": {"MP": 113, "Damage": 0, "Healing": 0, "Effects": "Shield", "Duration": 6},
                   "Poison": {"MP": 173, "Damage": 0, "Healing": 0, "Effects": "Poison", "Duration": 6},
                   "Recharge": {"MP": 229, "Damage": 0, "Healing": 0, "Effects": "Recharge", "Duration": 5}}

    def __init__(self, boss, player, mana_spent, effects):
        self.boss = boss
        self.player = player
        self.mana_spent = mana_spent
        self.effects = effects
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def tick(self, spell):
        if not self.player_turn(spell):
            return False, self
        if self.player["MP"] <= 0:
            return False, self
        if self.boss["Hit Points"] <= 0:
            return True, self
        self.boss_turn()
        if self.boss["Hit Points"] <= 0:
            return True, self
        if self.player["Hit Points"] <= 0:
            return False, self
        return None, self

    def player_turn(self, spell):
        self.tick_effects()
        self.player["MP"] -= self.spells[spell]["MP"]
        self.mana_spent += self.spells[spell]["MP"]
        self.boss["Hit Points"] -= self.spells[spell]["Damage"]
        self.player["Hit Points"] += self.spells[spell]["Healing"]
        if spell in self.effects:
            return False
        if self.spells[spell]["Effects"]:
            self.effects[spell] = self.spells[spell]["Duration"]
        return True

    def boss_turn(self):
        self.tick_effects()
        if self.boss["Hit Points"] <= 0:
            return
        armor = 7 if "Shield" in self.effects else 0
        self.player["Hit Points"] -= self.boss["Damage"] - armor

    def tick_effects(self):
        if "Poison" in self.effects.keys():
            self.boss["Hit Points"] -= 3
        if "Recharge" in self.effects.keys():
            self.player["MP"] += 101
        foo = {}
        for effect in self.effects:
            if self.effects[effect] > 1:
                foo[effect] = self.effects[effect] - 1
        self.effects = foo

with open("input.txt") as f:
    d_boss = f.readlines()
    d_boss = [x.strip() for x in d_boss]

boss = {}

for row in d_boss:
    stat, val = row.split(": ")
    boss[stat] = int(val)

boss["Armor"] = 0

player = {}
player["Hit Points"] = 50
player["MP"] = 500
player["Armor"] = 0

stack = [game_state(boss, player, 0, {})]
min_mp = np.inf

while(len(stack) > 0):
    stack.sort(key=lambda x: -x.mana_spent)
    current_state = stack.pop()
    for spell in game_state.spells:
        proposed_state = copy.deepcopy(current_state)
        win, proposed_state = proposed_state.tick(spell)
        if win == True:
            min_mp = min(min_mp, proposed_state.mana_spent)
        elif win == False:
            continue
        elif proposed_state not in stack:
            stack.append(proposed_state)
        
print(min_mp)