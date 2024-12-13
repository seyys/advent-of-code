package day12

import (
	"advent-of-code-2024/helpers"
)

var directions = [4][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

func Part2() {
	inputStr := helpers.ParseInput("./day12/input.txt")

	input := [][]byte{}
	for r, row := range inputStr {
		input = append(input, []byte{})
		for _, val := range row {
			input[r] = append(input[r], byte(val))
		}
	}

	price := 0

	visited := make(map[[2]int]struct{})
	for r, row := range input {
		for c := range row {
			if _, exists := visited[[2]int{r, c}]; exists {
				continue
			}

			blob := make(map[[2]int]struct{})
			area := bfsPart2(input, r, c, blob)
			perimeter := countEdges(blob, len(input), len(input[0]))

			price += area * perimeter

			for key := range blob {
				visited[key] = struct{}{}
			}
		}
	}

	println(price)
}

func bfsPart2(grid [][]byte, r int, c int, visited map[[2]int]struct{}) int {
	if _, exists := visited[[2]int{r, c}]; exists {
		return 0
	}
	area := 1
	visited[[2]int{r, c}] = struct{}{}

	for _, dir := range directions {
		newR := r + dir[0]
		newC := c + dir[1]
		if newR >= 0 && newR < len(grid) && newC >= 0 && newC < len(grid[0]) && grid[r+dir[0]][c+dir[1]] == grid[r][c] {
			area += bfsPart2(grid, r+dir[0], c+dir[1], visited)
		}
	}

	return area
}

// Can probably find maxR and C based on values in blob but can't be bothered
func countEdges(blob map[[2]int]struct{}, maxR int, maxC int) int {
	edges := 0

	visited := make(map[[2][2]int]struct{})

	for r := 0; r < maxR; r++ {
		for c := 0; c < maxC; c++ {
			shouldNotBePartOfBlob := false
			positionsToCheck := [2][2][2]int{{{r + 1, c}, {r, c + 1}}, {{r - 1, c}, {r, c - 1}}}
			if _, exists := blob[[2]int{r, c}]; exists {
				shouldNotBePartOfBlob = true
				positionsToCheck = [2][2][2]int{{{r - 1, c}, {r, c + 1}}, {{r + 1, c}, {r, c - 1}}}
			}
			for _, pos := range positionsToCheck {
				isCorner := true
				compensation := 0
				for _, p := range pos {
					if _, exists := visited[[2][2]int{p, {r, c}}]; exists {
						compensation++
						isCorner = false
						break
					}
					if _, exists := blob[p]; exists == shouldNotBePartOfBlob {
						isCorner = false
						break
					}
				}
				if isCorner {
					visited[[2][2]int{pos[0], {r, c}}] = struct{}{}
					visited[[2][2]int{{r, c}, pos[0]}] = struct{}{}
					visited[[2][2]int{pos[1], {r, c}}] = struct{}{}
					visited[[2][2]int{{r, c}, pos[1]}] = struct{}{}
					edges += 2
				}
			}
		}
	}

	return edges
}
