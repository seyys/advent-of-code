package day8

import (
	"advent-of-code-2024/helpers"
)

func Part2() {
	input := helpers.ParseInput("./day8/input.txt")

	nodes := make(map[rune]*[][2]int)
	for r, row := range input {
		for c, antenna := range row {
			if antenna == '.' {
				continue
			}
			if nodes[antenna] == nil {
				arr := [][2]int{}
				nodes[antenna] = &arr
			}
			*nodes[antenna] = append(*nodes[antenna], [2]int{r, c})
		}
	}

	antinodes := make(map[[2]int]struct{})
	for _, positions := range nodes {
		for i := 0; i < len(*positions); i++ {
			for j := i + 1; j < len(*positions); j++ {
				newAntinodes := findAntinodesPart2(
					(*positions)[i],
					(*positions)[j],
					0,
					len(input[0])-1,
					0,
					len(input[1])-1,
				)

				for _, newAntinode := range newAntinodes {
					antinodes[newAntinode] = struct{}{}
				}
			}
		}
	}

	println(len(antinodes))
}

func findAntinodesPart2(
	node1 [2]int,
	node2 [2]int,
	xBoundMinInclusive int,
	xBoundMaxInclusive int,
	yBoundMinInclusive int,
	yBoundMaxInclusive int,
) [][2]int {
	xDiff := node2[0] - node1[0]
	yDiff := node2[1] - node1[1]

	var antinodes [][2]int
	for i := 0; ; i++ {
		coordsToCheck := [2]int{node1[0] - i*xDiff, node1[1] - i*yDiff}
		if !isCoordsWithinMapPart2(
			coordsToCheck,
			xBoundMinInclusive,
			xBoundMaxInclusive,
			yBoundMinInclusive,
			yBoundMaxInclusive,
		) {
			break
		}
		antinodes = append(antinodes, coordsToCheck)
	}

	for i := 0; ; i++ {
		coordsToCheck := [2]int{node2[0] + i*xDiff, node2[1] + i*yDiff}
		if !isCoordsWithinMapPart2(
			coordsToCheck,
			xBoundMinInclusive,
			xBoundMaxInclusive,
			yBoundMinInclusive,
			yBoundMaxInclusive,
		) {
			break
		}
		antinodes = append(antinodes, coordsToCheck)
	}

	return antinodes
}

func isCoordsWithinMapPart2(coords [2]int,
	xBoundMinInclusive int,
	xBoundMaxInclusive int,
	yBoundMinInclusive int,
	yBoundMaxInclusive int) bool {
	return coords[0] >= xBoundMinInclusive &&
		coords[0] <= xBoundMaxInclusive &&
		coords[1] >= yBoundMinInclusive &&
		coords[1] <= yBoundMaxInclusive
}
