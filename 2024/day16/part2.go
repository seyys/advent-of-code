package day16

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"container/heap"
)

func Part2() {
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
	var optimalPaths []Node
	optimalScore := -1

	for openList.Len() > 0 {
		q := heap.Pop(openList).(Node)
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
			h := calcH(successor.coords, end)
			f := g + h
			newNode := Node{
				f:         f,
				g:         g,
				coords:    successor.coords,
				direction: successor.direction,
				parent:    &q,
			}
			if newNode.coords == end {
				if optimalScore == -1 {
					optimalScore = g
				}
				if g == optimalScore {
					optimalPaths = append(optimalPaths, newNode)
				}
			}

			if node, found := openList.GetNodeAtCoords(newNode.coords); found && node.f < f {
				continue
			}
			if node, found := closedList[[2]Coords{newNode.coords, newNode.direction}]; found && node.f < f {
				continue
			}
			openList.Push(newNode)
		}

		closedList[[2]Coords{q.coords, q.direction}] = q
	}

	bestSpots := make(map[Coords]struct{})
	for _, path := range optimalPaths {
		for path.parent != nil {
			bestSpots[path.coords] = struct{}{}
			path = *path.parent
		}
	}
	println(len(bestSpots))
}
