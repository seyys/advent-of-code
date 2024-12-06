package day6

import (
	"fmt"
	"os"
)

func Part1() {
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

	r := startR
	c := startC
	startDir := [2]int{-1, 0}
	dir := startDir
	count := 0
	for {
		if r+dir[0] < 0 || r+dir[0] >= len(grid) || c+dir[1] < 0 || c+dir[1] >= len(grid[0]) {
			if grid[r][c] != 'X' {
				count++
			}
			break
		}
		nextChar := grid[r+dir[0]][c+dir[1]]
		if nextChar == '#' {
			dir[0], dir[1] = dir[1], -dir[0]
		} else {
			if grid[r][c] != 'X' {
				count++
			}
			grid[r][c] = 'X'
			r += dir[0]
			c += dir[1]
		}
	}

	println(count)
}

func printGrid(grid [][]byte) {
	for _, row := range grid {
		for _, val := range row {
			fmt.Print(string(val))
		}
		fmt.Println()
	}
}
