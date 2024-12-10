package day10

import (
	"advent-of-code-2024/helpers"
)

func Part2() {
	inputRaw := helpers.ParseInput("./day10/input.txt")

	positions := [][2]int{}
	input := [][]int{}
	for r, row := range inputRaw {
		input = append(input, []int{})
		for c, val := range row {
			if val == '0' {
				positions = append(positions, [2]int{r, c})
			}
			input[r] = append(input[r], int(val)-'0')
		}
	}

	totalRating := 0
	for len(positions) > 0 {
		pos := positions[0]
		positions = positions[1:]
		for _, neighbour := range neighbours(pos, len(input), len(input[0])) {
			if input[pos[0]][pos[1]]+1 == input[neighbour[0]][neighbour[1]] {
				if input[neighbour[0]][neighbour[1]] == 9 {
					totalRating++
				} else {
					positions = append(positions, neighbour)
				}
			}
		}
	}

	println(totalRating)
}
