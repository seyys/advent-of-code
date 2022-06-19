import numpy as np

class a_star_node:
    def __init__(self,coords,parent_coords,travel_distance,end_coords):
        self.coords = coords
        self.parent_coords = parent_coords
        self.travel_distance = travel_distance
        self.est_distance_from_end = abs(coords[0] - end_coords[0]) + abs(coords[1] - end_coords[1])
        self.est_cost = travel_distance + self.est_distance_from_end

def a_star(graph:list):
    end_coords = (len(graph)-1,len(graph[0])-1)
    open_list = [a_star_node((0,0),(0,0),0,end_coords)]
    closed_list = list()
    while len(open_list) > 0:
        open_list.sort(key=lambda x:(x.est_cost))
        current_node = open_list.pop(0)
        current_node_children = list()
        for direction in [(0,-1), (0,1), (-1,0), (1,0)]:
            proposed_node_coords = (current_node.coords[0] + direction[0], current_node.coords[1] + direction[1])

            if proposed_node_coords == end_coords:
                total_distance = graph[proposed_node_coords[0]][proposed_node_coords[1]] + current_node.travel_distance
                end_node = a_star_node(proposed_node_coords,current_node.coords,total_distance,end_coords)
                open_list = []
                break

            if proposed_node_coords[0] < 0:
                continue
            if proposed_node_coords[1] < 0:
                continue
            if proposed_node_coords[0] > end_coords[0]:
                continue
            if proposed_node_coords[1] > end_coords[1]:
                continue

            total_distance = graph[proposed_node_coords[0]][proposed_node_coords[1]] + current_node.travel_distance
            proposed_node = a_star_node(proposed_node_coords,current_node.coords,total_distance,end_coords)

            node_in_open_list = [x for x in open_list if x.coords == proposed_node.coords]
            if len(node_in_open_list) > 1:
                raise Exception("Too many proposed nodes in open list")
            if len(node_in_open_list) == 1:
                if node_in_open_list[0].est_cost > proposed_node.est_cost:
                    open_list.pop(open_list.index(node_in_open_list[0]))
                else: 
                    continue

            node_in_closed_list = [x for x in closed_list if x.coords == proposed_node.coords]
            if len(node_in_closed_list) > 1:
                raise Exception("Too many proposed nodes in closed list")
            if len(node_in_closed_list) == 1:
                if node_in_closed_list[0].est_cost > proposed_node.est_cost:
                    closed_list.pop(node_in_closed_list[0])
                    closed_list.append(current_node)
                continue

            open_list.append(proposed_node)
        
        closed_list.append(current_node)
    
    closed_list.append(end_node)
    return closed_list[-1].travel_distance


with open('input.txt') as f:
    d = f.readlines()
    d = [list(x.strip()) for x in d]
    d = [[int(x) for x in y] for y in d]

shortest_route = a_star(d)

print(shortest_route)

"""
--- Day 15: Chiton ---
You've almost reached the exit of the cave, but the walls are getting closer together. Your submarine can barely still fit, though; the main problem is that the walls of the cave are covered in chitons, and it would be best not to bump any of them.

The cavern is large, but has a very low ceiling, restricting your motion to two dimensions. The shape of the cavern resembles a square; a quick scan of chiton density produces a map of risk level throughout the cave (your puzzle input). For example:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
You start in the top left position, your destination is the bottom right position, and you cannot move diagonally. The number at each position is its risk level; to determine the total risk of an entire path, add up the risk levels of each position you enter (that is, don't count the risk level of your starting position unless you enter it; leaving it adds no risk to your total).

Your goal is to find a path with the lowest total risk. In this example, a path with the lowest total risk is highlighted here:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
The total risk of this path is 40 (the starting position is never entered, so its risk is not counted).

What is the lowest total risk of any path from the top left to the bottom right?
"""