package day18

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"math"
	"strings"
	"sync"
	"sync/atomic"
)

type Coords struct {
	x, y int
}

type Node struct {
	f, g   int
	coords Coords
	parent *Node
}

func (c1 Coords) Add(c2 Coords) Coords {
	return Coords{c1.x + c2.x, c1.y + c2.y}
}

var directions = []Coords{
	{-1, 0},
	{1, 0},
	{0, -1},
	{0, 1},
}

func Part1() {
	file := helpers.OpenFile("./day18/input.txt")

	xMax := 70
	yMax := 70

	end := Coords{20, 35}

	corruptedCoords := make(map[Coords]struct{})
	scanner := bufio.NewScanner(file)
	for i := 0; scanner.Scan() && i < 1024; i++ {
		line := strings.Split(scanner.Text(), ",")
		x := helpers.Atoi(line[0])
		y := helpers.Atoi(line[1])

		corruptedCoords[Coords{x, y}] = struct{}{}
	}

	var wg sync.WaitGroup
	var result int32

	for _, start := range []Coords{{0, 0}, {70, 70}} {
		wg.Add(1)
		go func(start Coords) {
			defer wg.Done()
			atomic.AddInt32(&result, int32(doAStar(start, end, xMax, yMax, corruptedCoords)))
		}(start)
	}

	wg.Wait()
	println(result)
}

func doAStar(start, end Coords, xMax, yMax int, corruptedCoords map[Coords]struct{}) int {
	openList := []Node{{
		f:      0,
		g:      0,
		coords: start,
	}}
	var closedList []Node
	for len(openList) > 0 {
		q := findLeastF(&openList)
		for _, direction := range directions {
			coords := q.coords.Add(direction)
			if coords.x < 0 || coords.x > xMax || coords.y < 0 || coords.y > yMax {
				continue
			}
			if _, exists := corruptedCoords[coords]; exists {
				continue
			}
			g := q.g + 1
			h := abs(end.x-coords.x) + abs(end.y-coords.y)
			f := g + h
			successor := Node{f, g, coords, &q}
			// printGrid(xMax, yMax, corruptedCoords, successor)
			// println()
			if coords == end {
				// fmt.Println(successor)
				return successor.g - 1
			}
			shouldContinue := false
			for _, node := range openList {
				if node.coords == coords && node.f < f {
					shouldContinue = true
				}
			}
			if shouldContinue {
				continue
			}
			for _, node := range closedList {
				if node.coords == coords && node.f < f {
					shouldContinue = true
				}
			}
			if shouldContinue {
				continue
			}
			openList = append(openList, successor)
		}
		closedList = append(closedList, q)
	}
	return 0
}

func findLeastF(list *[]Node) Node {
	index := 0
	lowestF := math.MaxInt
	for i, node := range *list {
		if node.f < lowestF {
			index = i
			lowestF = node.f
		}
	}
	result := (*list)[index]
	*list = append((*list)[:index], (*list)[index+1:]...)
	return result
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func printGrid(xMax, yMax int, corruptedCoords map[Coords]struct{}, node Node) {
	path := make(map[Coords]struct{})
	for {
		path[node.coords] = struct{}{}
		if node.parent == nil {
			break
		}
		node = *node.parent
	}
	for y := 0; y <= yMax; y++ {
		for x := 0; x <= xMax; x++ {
			if _, exists := corruptedCoords[Coords{x, y}]; exists {
				print("#")
			} else if _, exists := path[Coords{x, y}]; exists {
				print("O")
			} else {
				print(".")
			}
		}
		println()
	}
}
