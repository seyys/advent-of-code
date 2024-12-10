package day10

import (
	"advent-of-code-2024/helpers"

	mapset "github.com/deckarep/golang-set/v2"
)

func Part1() {
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
	positions := mapset.NewSet[[2]int]()
	for _, trailhead := range stack {
		positions.Add(trailhead)
		for level := 1; level <= 9; level++ {
			positionsOnCurrentLevel := positions.Clone()
			positions.Clear()
			for positionOnCurrentLevel := range positionsOnCurrentLevel.Iter() {
				for _, neighbour := range neighbours(positionOnCurrentLevel, len(input), len(input[0])) {
					if input[neighbour[0]][neighbour[1]] == level {
						positions.Add(neighbour)
					}
				}
			}
		}
		totalScore += positions.Cardinality()
		positions.Clear()
	}

	println(totalScore)
}

func neighbours(pos [2]int, maxR int, maxC int) [][2]int {
	result := [][2]int{}
	if pos[0] > 0 {
		result = append(result, [2]int{pos[0] - 1, pos[1]})
	}
	if pos[0] < maxR-1 {
		result = append(result, [2]int{pos[0] + 1, pos[1]})
	}
	if pos[1] > 0 {
		result = append(result, [2]int{pos[0], pos[1] - 1})
	}
	if pos[1] < maxC-1 {
		result = append(result, [2]int{pos[0], pos[1] + 1})
	}
	return result
}
