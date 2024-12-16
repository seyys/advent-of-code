package day16

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"container/heap"
)

type Coords struct {
	x, y int
}

func (c1 Coords) Add(c2 Coords) Coords {
	return Coords{c1.x + c2.x, c1.y + c2.y}
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func Part1() {
	file := helpers.OpenFile("./day16/input.txt")

	walls := make(map[Coords]struct{})
	var start Coords
	var end Coords

	scanner := bufio.NewScanner(file)
	for r := 0; scanner.Scan(); r++ {
		line := scanner.Text()

		for c, ch := range line {
			switch ch {
			case '#':
				walls[Coords{c, r}] = struct{}{}
			case 'S':
				start = Coords{c, r}
			case 'E':
				end = Coords{c, r}
			}
		}
	}

	openList := &MinHeap{}
	openList.Push(Node{
		f:         0,
		g:         0,
		coords:    start,
		direction: Coords{1, 0},
	})
	heap.Init(openList)
	closedList := make(map[[2]Coords]Node)

	for openList.Len() > 0 {
		q := heap.Pop(openList).(Node)
		// printPath(start, end, q, walls)
		if q.coords == end {
			println(q.g)
			break
		}
		successors := []struct {
			coords    Coords
			direction Coords
			extra     int
		}{
			{q.coords.Add(q.direction), q.direction, 1},
			{q.coords, rotateAnticlockwise(q.direction), 1000},
			{q.coords, rotateClockwise(q.direction), 1000},
		}
		for _, successor := range successors {
			if _, exists := walls[successor.coords]; exists {
				continue
			}
			g := q.g + successor.extra
			if successor.coords == end {
				println(g)
				return
			}
			h := calcH(successor.coords, end)
			f := g + h

			if node, found := openList.GetNodeAtCoords(successor.coords); found && node.f < f {
				continue
			}
			if node, found := closedList[[2]Coords{successor.coords, successor.direction}]; found && node.f < f {
				continue
			}
			newNode := Node{
				f:         f,
				g:         g,
				coords:    successor.coords,
				direction: successor.direction,
				parent:    &q,
			}
			openList.Push(newNode)
		}

		closedList[[2]Coords{q.coords, q.direction}] = q
	}
}

func calcH(start Coords, end Coords) int {
	return abs(end.y-start.y) + abs(end.x-start.x)
}

func rotateClockwise(direction Coords) Coords {
	return Coords{-direction.y, direction.x}
}

func rotateAnticlockwise(direction Coords) Coords {
	return Coords{direction.y, -direction.x}
}

var directionMap = map[Coords]string{
	{0, -1}: "^",
	{0, 1}:  "v",
	{-1, 0}: "<",
	{1, 0}:  ">",
}

func printPath(start, end Coords, node Node, walls map[Coords]struct{}) {
	path := make(map[Coords]Coords)
	for {
		path[node.coords] = node.direction
		if node.parent == nil {
			break
		}
		node = *node.parent
	}

	for r := 0; r < 17; r++ {
		for c := 0; c < 17; c++ {
			coords := Coords{c, r}
			if direction, exists := path[coords]; exists {
				print(directionMap[direction])
			} else if coords == start {
				print("S")
			} else if coords == end {
				print("E")
			} else if _, exists := walls[coords]; exists {
				print("#")
			} else {
				print(".")
			}
		}
		println()
	}
}
