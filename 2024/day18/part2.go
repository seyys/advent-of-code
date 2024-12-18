package day18

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"fmt"
	"strings"
	"sync"
	"sync/atomic"
)

func Part2() {
	file := helpers.OpenFile("./day18/input.txt")
	defer file.Close()

	xMax := 70
	yMax := 70

	var corruptedCoordsArray []Coords
	corruptedCoords := make(map[Coords]struct{})
	scanner := bufio.NewScanner(file)
	i := 0
	for ; scanner.Scan() && i < 1024; i++ {
		line := strings.Split(scanner.Text(), ",")
		x := helpers.Atoi(line[0])
		y := helpers.Atoi(line[1])

		corruptedCoords[Coords{x, y}] = struct{}{}
		corruptedCoordsArray = append(corruptedCoordsArray, Coords{x, y})
	}

	var wg sync.WaitGroup
	var result int32 = -1

	for ; scanner.Scan(); i++ {
		if atomic.LoadInt32(&result) != -1 {
			break
		}
		line := strings.Split(scanner.Text(), ",")
		x := helpers.Atoi(line[0])
		y := helpers.Atoi(line[1])

		corruptedCoords[Coords{x, y}] = struct{}{}
		corruptedCoordsArray = append(corruptedCoordsArray, Coords{x, y})

		copyCorruptedCoords := make(map[Coords]struct{})
		for key := range corruptedCoords {
			copyCorruptedCoords[key] = struct{}{}
		}

		wg.Add(1)
		go func(corruptedCoords map[Coords]struct{}, i int) {
			defer wg.Done()

			if floodFill(Coords{0, 0}, xMax, yMax, corruptedCoords) == floodFill(Coords{70, 70}, xMax, yMax, corruptedCoords) {
				return
			}
			for {
				current := atomic.LoadInt32(&result)
				if current != -1 && int32(i) > current {
					break
				}
				if atomic.CompareAndSwapInt32(&result, current, int32(i)) {
					break
				}
			}
		}(copyCorruptedCoords, i)
	}

	wg.Wait()

	corruptedCoords = make(map[Coords]struct{})
	for i := 0; i < int(result); i++ {
		corruptedCoords[corruptedCoordsArray[i]] = struct{}{}
	}
	printGridPart2(xMax, yMax, corruptedCoords)
	println(result)
	fmt.Println(corruptedCoordsArray[result])
}

func floodFill(start Coords, xMax, yMax int, corruptedCoords map[Coords]struct{}) int {
	seen := make(map[Coords]struct{})
	open := []Coords{start}
	for len(open) > 0 {
		coords := open[0]
		open = open[1:]
		if coords.x < 0 || coords.x > xMax || coords.y < 0 || coords.y > yMax {
			continue
		}
		if _, exists := corruptedCoords[coords]; exists {
			continue
		}
		if _, exists := seen[coords]; exists {
			continue
		}
		seen[coords] = struct{}{}
		for _, direction := range directions {
			open = append(open, coords.Add(direction))
		}
	}

	return len(seen)
}

func printGridPart2(xMax, yMax int, corruptedCoords map[Coords]struct{}) {
	for y := 0; y <= yMax; y++ {
		for x := 0; x <= xMax; x++ {
			if _, exists := corruptedCoords[Coords{x, y}]; exists {
				print("#")
			} else {
				print(".")
			}
		}
		println()
	}
}
