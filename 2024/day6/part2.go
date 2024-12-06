package day6

import (
	"fmt"
	"os"
)

func Part2() {
	file, err := os.ReadFile("./day6/input.txt")
	if err != nil {
		panic(err)
	}

	grid := [][]byte{}
	grid = append(grid, []byte{})
	row := 0

	var startR, startC int
	for _, char := range file {
		if char == '^' {
			startR = row
			startC = len(grid[row])
		}
		if char == '\n' {
			row++
			grid = append(grid, []byte{})
		} else {
			grid[row] = append(grid[row], char)
		}
	}

	count := 0
	for r, row := range grid {
		for c := range row {
			if grid[r][c] != '.' {
				continue
			}
			newGrid := make([][]byte, len(grid))
			for i := range grid {
				newGrid[i] = make([]byte, len(grid[i]))
				copy(newGrid[i], grid[i])
			}
			newGrid[r][c] = '#'
			if isLoop(startR, startC, newGrid) {
				count++
			}
		}
	}

	fmt.Println(count)
}

func isLoop(startR int, startC int, grid [][]byte) bool {
	r := startR
	c := startC
	startDir := [2]int{-1, 0}
	dir := startDir
	visited := make(map[string]struct{})
	for {
		if r+dir[0] < 0 || r+dir[0] >= len(grid) || c+dir[1] < 0 || c+dir[1] >= len(grid[0]) {
			break
		}
		key := fmt.Sprintf("%d,%d,%d,%d", r, c, dir[0], dir[1])
		if _, exists := visited[key]; exists {
			return true
		}
		visited[key] = struct{}{}
		nextChar := grid[r+dir[0]][c+dir[1]]
		if nextChar == '#' {
			dir[0], dir[1] = dir[1], -dir[0]
		} else {
			grid[r][c] = 'X'
			r += dir[0]
			c += dir[1]
		}
	}

	return false
}
