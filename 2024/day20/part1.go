package day20

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"math"
)

type Coords struct {
	x, y int
}

func (c1 Coords) Add(c2 Coords) Coords {
	return Coords{c1.x + c2.x, c1.y + c2.y}
}

var distanceToEnd map[Coords]int

var directionMap = [4]Coords{
	{0, -1},
	{0, 1},
	{-1, 0},
	{1, 0},
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func Part1() {
	file := helpers.OpenFile("./day20/input.txt")
	defer file.Close()

	// var start Coords
	var end Coords
	distanceToEnd = make(map[Coords]int)
	walls := make(map[Coords]int)

	scanner := bufio.NewScanner(file)
	for r := 0; scanner.Scan(); r++ {
		line := scanner.Text()
		for c, ch := range line {
			if ch == '#' {
				walls[Coords{c, r}] = math.MaxInt
				continue
			}
			distanceToEnd[Coords{c, r}] = math.MaxInt
			// if ch == 'S' {
			// 	start = Coords{c,r}
			// }
			if ch == 'E' {
				end = Coords{c, r}
			}
		}
	}

	bfs(end, 0)

	// count := make(map[int]int)
	result := 0
	for wall := range walls {
		var adjacentCells []Coords
		for _, direction := range directionMap {
			testCoords := wall.Add(direction)
			if testCoords.x < 0 || testCoords.x >= 141 || testCoords.y < 0 || testCoords.y >= 141 {
				continue
			}
			if _, exists := distanceToEnd[testCoords]; !exists {
				continue
			}
			adjacentCells = append(adjacentCells, testCoords)
		}
		if len(adjacentCells) < 2 {
			continue
		}
		for i := 0; i < len(adjacentCells); i++ {
			for j := i; j < len(adjacentCells); j++ {
				if i == j {
					continue
				}
				timeSave := abs(distanceToEnd[adjacentCells[i]]-distanceToEnd[adjacentCells[j]]) - 2
				// count[timeSave]++
				if timeSave >= 100 {
					result++
				}
			}
		}
	}
	// fmt.Println(count)
	println(result)
}

func bfs(node Coords, distance int) {
	if distanceToEnd[node] <= distance {
		return
	}
	distanceToEnd[node] = distance
	for _, direction := range directionMap {
		nextCoords := node.Add(direction)
		if nextCoords.x < 0 || nextCoords.x >= 141 || nextCoords.y < 0 || nextCoords.y >= 141 {
			continue
		}
		if _, exists := distanceToEnd[nextCoords]; !exists {
			continue
		}
		bfs(nextCoords, distance+1)
	}
}
