package day20

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"math"
)

func Part2() {
	file := helpers.OpenFile("./day20/input.txt")
	defer file.Close()

	var end Coords
	distanceToEnd = make(map[Coords]int)

	scanner := bufio.NewScanner(file)
	for r := 0; scanner.Scan(); r++ {
		line := scanner.Text()
		for c, ch := range line {
			if ch == '#' {
				continue
			}
			distanceToEnd[Coords{c, r}] = math.MaxInt
			if ch == 'E' {
				end = Coords{c, r}
			}
		}
	}

	bfs(end, 0)

	maxManhattanRange := 20
	type node struct {
		coords     Coords
		travelTime int
	}
	var aoe []node
	for i := -maxManhattanRange; i < maxManhattanRange+1; i++ {
		for j := -maxManhattanRange; j < maxManhattanRange+1; j++ {
			dist := abs(i) + abs(j)
			if dist < 2 {
				continue
			}
			if maxManhattanRange < dist {
				continue
			}
			aoe = append(aoe, node{Coords{i, j}, dist})
		}
	}

	result := 0
	for coordsFrom, distFrom := range distanceToEnd {
		// Some nodes are not reached in the bfs and still have maxint
		if distFrom == math.MaxInt {
			continue
		}
		for _, movement := range aoe {
			coordsTo := coordsFrom.Add(movement.coords)
			distTo, exists := distanceToEnd[coordsTo]
			if !exists {
				continue
			}
			if distTo > distFrom {
				continue
			}
			if distFrom-(distTo+movement.travelTime) < 100 {
				continue
			}
			if distFrom-distTo <= movement.travelTime {
				continue
			}
			result++
		}
	}
	println(result)
}
