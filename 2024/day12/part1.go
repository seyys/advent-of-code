package day12

import (
	"advent-of-code-2024/helpers"
)

func Part1() {
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
			perimeter, area := bfs(input, r, c, visited)
			price += perimeter * area
		}
	}

	println(price)
}

func bfs(grid [][]byte, r int, c int, visited map[[2]int]struct{}) (int, int) {
	if _, exists := visited[[2]int{r, c}]; exists {
		return 0, 0
	}
	perimeter := countPerimeter(grid, r, c)
	area := 1
	visited[[2]int{r, c}] = struct{}{}

	p := 0
	a := 0
	for _, dir := range [4][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} {
		newR := r + dir[0]
		newC := c + dir[1]
		if newR >= 0 && newR < len(grid) && newC >= 0 && newC < len(grid[0]) && grid[r+dir[0]][c+dir[1]] == grid[r][c] {
			p, a = bfs(grid, r+dir[0], c+dir[1], visited)
			perimeter += p
			area += a
		}
	}

	return perimeter, area
}

func countPerimeter(grid [][]byte, r int, c int) int {
	perimeter := 0

	for _, dir := range [4][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} {
		newR := r + dir[0]
		newC := c + dir[1]
		if newR < 0 || newR >= len(grid) || newC < 0 || newC >= len(grid[0]) || grid[r][c] != grid[newR][newC] {
			perimeter++
		}
	}

	return perimeter
}
