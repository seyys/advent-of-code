package day4

import (
	"advent-of-code-2024/helpers"
)

func Part2() {
	count := 0

	grid := helpers.ParseInput("./day4/input.txt")

	for i := 1; i < len(grid)-1; i++ {
		for j := 1; j < len(grid[0])-1; j++ {
			if grid[i][j] == 'A' {
				if checkXmas([2]byte{grid[i-1][j-1], grid[i+1][j+1]}) &&
					checkXmas([2]byte{grid[i+1][j-1], grid[i-1][j+1]}) {
					count++
				}
			}
		}
	}

	println(count)
}

func checkXmas(diag [2]byte) bool {
	if diag == [2]byte{'M', 'S'} || diag == [2]byte{'S', 'M'} {
		return true
	}
	return false
}
