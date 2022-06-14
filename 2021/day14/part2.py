from collections import Counter

def insert_pairs(pairs:Counter, pair_insertion:dict):
    result = Counter()
    for p in pairs:
        result[pair_insertion[p][0]] += pairs[p]
        result[pair_insertion[p][1]] += pairs[p]
    return result

def generate_pair_insertions(pair_insertion:dict):
    for p in pair_insertion:
        pair_insertion[p] = [p[0] + pair_insertion[p], pair_insertion[p] + p[1]]
    return pair_insertion

with open('input.txt') as f:
    d = [x.strip() for x in f.readlines()]
    polymer = d[0]
    pair_insertion = dict([x.split(" -> ") for x in d[2:]])
    monomers = pair_insertion.copy()
    pair_insertion = generate_pair_insertions(pair_insertion)

unique_monomers = []
for m in monomers:
    if monomers[m] not in unique_monomers:
        unique_monomers.append(monomers[m])

pairs = Counter()
for i in range(len(polymer)-1):
    pairs += Counter([polymer[i] + polymer[i+1]])

for time in range(40):
    pairs = insert_pairs(pairs,pair_insertion)

monomers_count = Counter()
monomers_count += Counter(polymer[-1])
for p in pairs.keys():
    for m in unique_monomers:
        if m == p[0]:
            monomers_count[m] += pairs[p]

count_most_common_monomer = monomers_count.most_common(1)[0][1]
count_least_common_monomer = monomers_count.most_common()[-1][1]

print(count_most_common_monomer-count_least_common_monomer)

"""
--- Day 14: Extended Polymerization ---
The incredible pressures at this depth are starting to put a strain on your submarine. The submarine has polymerization equipment that would produce suitable materials to reinforce the submarine, and the nearby volcanically-active caves should even have the necessary input elements in sufficient quantities.

The submarine manual contains instructions for finding the optimal polymer formula; specifically, it offers a polymer template and a list of pair insertion rules (your puzzle input). You just need to work out what polymer would result after repeating the pair insertion process a few times.

For example:

NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
The first line is the polymer template - this is the starting point of the process.

The following section defines the pair insertion rules. A rule like AB -> C means that when elements A and B are immediately adjacent, element C should be inserted between them. These insertions all happen simultaneously.

So, starting with the polymer template NNCB, the first step simultaneously considers all three pairs:

The first pair (NN) matches the rule NN -> C, so element C is inserted between the first N and the second N.
The second pair (NC) matches the rule NC -> B, so element B is inserted between the N and the C.
The third pair (CB) matches the rule CB -> H, so element H is inserted between the C and the B.
Note that these pairs overlap: the second element of one pair is the first element of the next pair. Also, because all pairs are considered simultaneously, inserted elements are not considered to be part of a pair until the next step.

After the first step of this process, the polymer becomes NCNBCHB.

Here are the results of a few steps using the above rules:

Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
This polymer grows quickly. After step 5, it has length 97; After step 10, it has length 3073. After step 10, B occurs 1749 times, C occurs 298 times, H occurs 161 times, and N occurs 865 times; taking the quantity of the most common element (B, 1749) and subtracting the quantity of the least common element (H, 161) produces 1749 - 161 = 1588.

Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?

Your puzzle answer was 3259.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair insertion process; a total of 40 steps should do it.

In the above example, the most common element is B (occurring 2192039569602 times) and the least common element is H (occurring 3849876073 times); subtracting these produces 2188189693529.

Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
"""