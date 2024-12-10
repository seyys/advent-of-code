package day10

import (
	"advent-of-code-2024/helpers"
)

func Part2() {
	inputRaw := helpers.ParseInput("./day10/input.txt")

	stack := [][2]int{}
	input := [][]int{}
	for r, row := range inputRaw {
		input = append(input, []int{})
		for c, val := range row {
			if val == '0' {
				stack = append(stack, [2]int{r, c})
			}
			input[r] = append(input[r], int(val)-'0')
		}
	}

	totalScore := 0
	for _, trailhead := range stack {
		positions := [][2]int{trailhead}
		for level := 1; level <= 9; level++ {
			positionsOnCurrentLevel := make([][2]int, len(positions))
			copy(positionsOnCurrentLevel, positions)
			positions = [][2]int{}
			for _, positionOnCurrentLevel := range positionsOnCurrentLevel {
				for _, neighbour := range neighbours(positionOnCurrentLevel, len(input), len(input[0])) {
					if input[neighbour[0]][neighbour[1]] == level {
						positions = append(positions, neighbour)
					}
				}
			}
		}
		totalScore += len(positions)
	}

	println(totalScore)
}
