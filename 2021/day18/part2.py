import re
import numpy as np

class node:
    def __init__(self,depth:int):
        self.left = None
        self.right = None
        self.parent = None
        self.depth = depth
        self.val = float("nan")

def create_node(s:str,depth:int):
    if s == None:
        return None
    n = node(depth)
    if '[' in s:
        left_branch, right_branch = find_branches_str(s)
        n.left = create_node(left_branch,depth+1)
        n.right = create_node(right_branch,depth+1)
        n.left.parent = n
        n.right.parent = n
    else:
        n.val = int(s)
    return n

def find_branches_str(s:str):
    s = s[::-1].replace(']', '', 1)
    s = s[::-1].replace('[', '', 1)

    if '[' not in s:
        foo = s.split(',')
        return foo[0],foo[1]

    idx_split = -1
    open_bracket_count = 0
    for c in s:
        idx_split += 1
        if c == '[':
            open_bracket_count += 1
            continue
        if c == ']':
            open_bracket_count -= 1
            continue
        if open_bracket_count == 0:
            break

    if s[0] != '[':
        idx_split = s.index(',')
    
    left_branch = s[:idx_split]
    right_branch = s[idx_split+1:]

    return left_branch,right_branch

def explode(n:node):
    if n == None:
        return False
    exploded = explode(n.left)
    if not exploded:
        exploded = explode(n.right)
    if n.depth >= 4 and n.left != None and n.right != None and not exploded:
        explode_add_to_left_neighbour(n.parent,n.left.val,[n], True)
        explode_add_to_right_neighbour(n.parent,n.right.val,[n], True)
        n.left = None
        n.right = None
        n.val = 0
        return True
    return exploded

def explode_add_to_left_neighbour(n:node, val:int, n_trace:list, ascending:bool):
    if n == None:
        return False
    found_neighbour = False
    n_trace.append(n)
    if not found_neighbour and n.right != None and n.right not in n_trace and not ascending:
        found_neighbour = explode_add_to_left_neighbour(n.right, val, n_trace, False)
    if not found_neighbour and n.left != None and n.left not in n_trace and ascending:
        found_neighbour = explode_add_to_left_neighbour(n.left, val, n_trace, False)
    if not found_neighbour and n.parent != None and ascending:
        found_neighbour = explode_add_to_left_neighbour(n.parent, val, n_trace, True)
    if n.left == None and not np.isnan(n.val):
        n.val += val
        return True

    return found_neighbour
    
def explode_add_to_right_neighbour(n:node, val:int, n_trace:list, ascending:bool):
    if n == None:
        return False
    found_neighbour = False
    n_trace.append(n)
    if not found_neighbour and n.left != None and n.left not in n_trace and not ascending:
        found_neighbour = explode_add_to_right_neighbour(n.left, val, n_trace, False)
    if not found_neighbour and n.right != None and n.right not in n_trace and ascending:
        found_neighbour = explode_add_to_right_neighbour(n.right, val, n_trace, False)
    if not found_neighbour and n.parent != None and ascending:
        found_neighbour = explode_add_to_right_neighbour(n.parent, val, n_trace, True)
    if n.right == None and not np.isnan(n.val):
        n.val += val
        return True

    return found_neighbour

def split(n:node):
    if n == None:
        return False
    has_split = split(n.left)
    if not has_split:
        has_split = split(n.right)
    if not has_split and not np.isnan(n.val) and n.val >= 10:
        n.left = node(n.depth + 1)
        n.left.val = int(np.floor(n.val / 2))
        n.left.parent = n
        n.right = node(n.depth + 1)
        n.right.val = int(np.ceil(n.val / 2))
        n.right.parent = n
        n.val = float("nan")
        return True
    return has_split

def increase_depth(n:node):
    if n == None:
        return
    n.depth += 1
    increase_depth(n.left)
    increase_depth(n.right)

def addition(n:node,m:node):
    result = node(0)
    increase_depth(n)
    increase_depth(m)
    result.left = n
    result.left.parent = result
    result.right = m
    result.right.parent = result
    return result

def perform_reduction(d:list):
    n = d[0]
    for i in range(len(d)):
        something_happened = True
        while something_happened:
            something_happened = explode(n)
            if something_happened:
                continue
            something_happened = split(n)
        if i < len(d)-1:
            n = addition(n,d[i+1])
            print(visualise_tree(n))
    return n
    
def calculate_magnitude(n:node):
    if n == None:
        return 0
    if np.isnan(n.val):
        return 3*calculate_magnitude(n.left) + 2*calculate_magnitude(n.right)
    else: 
        return n.val

def visualise_tree(n:node):
    if n == None:
        return ''
    s = visualise_tree(n.left)
    s += ','
    s += visualise_tree(n.right)

    if np.isnan(n.val):
        return '[' + s + ']'

    return str(n.val)

# Tests
with open("input.txt") as f:
    d = f.readlines()
    d = [x.strip() for x in d]
max_val = 0
max_combo = []
for i in range(len(d)):
    for j in range(len(d)):
        if i == j:
            continue
        n = create_node(d[i], 0)
        m = create_node(d[j], 0)
        n = addition(n, m)
        result = perform_reduction([n])
        max_val = max(max_val,calculate_magnitude(n))
        max_combo = [create_node(d[i], 0), create_node(d[j], 0)]
print(visualise_tree(max_combo[0]))
print(visualise_tree(max_combo[1]))
print(visualise_tree(perform_reduction([n,m])))
print(max_val)

"""
--- Day 18: Snailfish ---
You descend into the ocean trench and encounter some snailfish. They say they saw the sleigh keys! They'll even tell you which direction the keys went if you help one of the smaller snailfish with his math homework.

Snailfish numbers aren't like regular numbers. Instead, every snailfish number is a pair - an ordered list of two elements. Each element of the pair can be either a regular number or another pair.

Pairs are written as [x,y], where x and y are the elements within the pair. Here are some example snailfish numbers, one snailfish number per line:

[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]
This snailfish homework is about addition. To add two snailfish numbers, form a pair from the left and right parameters of the addition operator. For example, [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]].

There's only one problem: snailfish numbers must always be reduced, and the process of adding two snailfish numbers can result in snailfish numbers that need to be reduced.

To reduce a snailfish number, you must repeatedly do the first action in this list that applies to the snailfish number:

If any pair is nested inside four pairs, the leftmost such pair explodes.
If any regular number is 10 or greater, the leftmost such regular number splits.
Once no action in the above list applies, the snailfish number is reduced.

During reduction, at most one action applies, after which the process returns to the top of the list of actions. For example, if split produces a pair that meets the explode criteria, that pair explodes before other splits occur.

To explode a pair, the pair's left value is added to the first regular number to the left of the exploding pair (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any). Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the regular number 0.

Here are some examples of a single explode action:

[[[[[9,8],1],2],3],4] becomes [[[[0,9],2],3],4] (the 9 has no regular number to its left, so it is not added to any regular number).
[7,[6,[5,[4,[3,2]]]]] becomes [7,[6,[5,[7,0]]]] (the 2 has no regular number to its right, and so it is not added to any regular number).
[[6,[5,[4,[3,2]]]],1] becomes [[6,[5,[7,0]]],3].
[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]] becomes [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] (the pair [3,2] is unaffected because the pair [7,3] is further to the left; [3,2] would explode on the next action).
[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] becomes [[3,[2,[8,0]]],[9,[5,[7,0]]]].
To split a regular number, replace it with a pair; the left element of the pair should be the regular number divided by two and rounded down, while the right element of the pair should be the regular number divided by two and rounded up. For example, 10 becomes [5,5], 11 becomes [5,6], 12 becomes [6,6], and so on.

Here is the process of finding the reduced result of [[[[4,3],4],4],[7,[[8,4],9]]] + [1,1]:

after addition: [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
after explode:  [[[[0,7],4],[7,[[8,4],9]]],[1,1]]
after explode:  [[[[0,7],4],[15,[0,13]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
after split:    [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
Once no reduce actions apply, the snailfish number that remains is the actual result of the addition operation: [[[[0,7],4],[[7,8],[6,0]]],[8,1]].

The homework assignment involves adding up a list of snailfish numbers (your puzzle input). The snailfish numbers are each listed on a separate line. Add the first snailfish number and the second, then add that result and the third, then add that result and the fourth, and so on until all numbers in the list have been used once.

For example, the final sum of this list is [[[[1,1],[2,2]],[3,3]],[4,4]]:

[1,1]
[2,2]
[3,3]
[4,4]
The final sum of this list is [[[[3,0],[5,3]],[4,4]],[5,5]]:

[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
The final sum of this list is [[[[5,0],[7,4]],[5,5]],[6,6]]:

[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]
Here's a slightly larger example:

[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
The final sum [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]] is found after adding up the above snailfish numbers:

  [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
+ [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
= [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]

  [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
+ [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
= [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]

  [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]
+ [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
= [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]

  [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
+ [7,[5,[[3,8],[1,4]]]]
= [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]

  [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
+ [[2,[2,2]],[8,[8,1]]]
= [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]

  [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
+ [2,9]
= [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]

  [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
+ [1,[[[9,3],9],[[9,0],[0,7]]]]
= [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]

  [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
+ [[[5,[7,4]],7],1]
= [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]

  [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
+ [[[[4,2],2],6],[8,7]]
= [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
To check whether it's the right answer, the snailfish teacher only checks the magnitude of the final sum. The magnitude of a pair is 3 times the magnitude of its left element plus 2 times the magnitude of its right element. The magnitude of a regular number is just that number.

For example, the magnitude of [9,1] is 3*9 + 2*1 = 29; the magnitude of [1,9] is 3*1 + 2*9 = 21. Magnitude calculations are recursive: the magnitude of [[9,1],[1,9]] is 3*29 + 2*21 = 129.

Here are a few more magnitude examples:

[[1,2],[[3,4],5]] becomes 143.
[[[[0,7],4],[[7,8],[6,0]]],[8,1]] becomes 1384.
[[[[1,1],[2,2]],[3,3]],[4,4]] becomes 445.
[[[[3,0],[5,3]],[4,4]],[5,5]] becomes 791.
[[[[5,0],[7,4]],[5,5]],[6,6]] becomes 1137.
[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]] becomes 3488.
So, given this example homework assignment:

[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
The final sum is:

[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]
The magnitude of this final sum is 4140.

Add up all of the snailfish numbers from the homework assignment in the order they appear. What is the magnitude of the final sum?

Your puzzle answer was 4235.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
You notice a second question on the back of the homework assignment:

What is the largest magnitude you can get from adding only two of the snailfish numbers?

Note that snailfish addition is not commutative - that is, x + y and y + x can produce different results.

Again considering the last example homework assignment above:

[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
The largest magnitude of the sum of any two snailfish numbers in this list is 3993. This is the magnitude of [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]] + [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]], which reduces to [[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]].

What is the largest magnitude of any sum of two different snailfish numbers from the homework assignment?
"""