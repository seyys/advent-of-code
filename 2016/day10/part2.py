class bot:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.chips = []

    def receive_chip(self, chip):
        self.chips.append(chip)
        if self.can_act():
            min_chip = min(self.chips)
            max_chip = max(self.chips)
            self.chips = []
            return self.low, min_chip, self.high, max_chip
        else:
            return None, None, None, None

    def can_act(self):
        return len(self.chips) == 2

def receive_chip(b, val):
    low_bot, low_chip, high_bot, high_chip = bot_instr[b].receive_chip(val)
    if low_bot:
        if low_bot < 0:
            bot_instr[low_bot] = low_chip
        else:
            receive_chip(low_bot, low_chip)
    if high_bot:
        if high_bot < 0:
            bot_instr[high_bot] = high_chip
        else:
            receive_chip(high_bot, high_chip)

with open("input.txt") as f:
    d = f.readlines()
d = [x.strip() for x in d]
d_instr = [x for x in d if "gives" in x]
d_input = [x for x in d if "goes" in x]

bot_instr = dict()

for instr in d_instr:
    b, b_low, b_high = instr.replace(" gives low to ", '|').replace(" and high to ", '|').split('|')
    b = int(b.replace("bot ", ''))
    if "output" in b_low:
        b_low = -int(b_low.replace("output ", '')) - 1
    else:
        b_low = int(b_low.replace("bot ", ''))
    if "output" in b_high:
        b_high = -int(b_high.replace("output ", '')) - 1
    else:
        b_high = int(b_high.replace("bot ", ''))
    bot_instr[b] = bot(b_low, b_high)

for inp in d_input:
    val, b = inp.replace("value ", '').split(" goes to bot ")
    val = int(val)
    b = int(b)
    receive_chip(b, val)

print(bot_instr[-1] * bot_instr[-2] * bot_instr[-3])