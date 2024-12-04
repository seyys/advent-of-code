package day4

import (
	"advent-of-code-2024/helpers"
	"regexp"
)

func Part1() {
	count := 0

	grid := helpers.ParseInput("./day4/input.txt")
	count += countXmasInGrid(grid)

	grid45 := rotateGrid45(grid)
	count += countXmasInGrid(grid45)

	grid90 := rotateGrid90(grid)
	count += countXmasInGrid(grid90)

	grid135 := rotateGrid45(grid90)
	count += countXmasInGrid(grid135)

	grid180 := rotateGrid90(grid90)
	count += countXmasInGrid(grid180)

	grid235 := rotateGrid45(grid180)
	count += countXmasInGrid(grid235)

	grid270 := rotateGrid90(grid180)
	count += countXmasInGrid(grid270)

	grid315 := rotateGrid45(grid270)
	count += countXmasInGrid(grid315)

	println(count)
}

func countXmasInGrid(grid []string) int {
	count := 0
	for _, s := range grid {
		count += countXmas(s)
	}
	return count
}

func countXmas(str string) int {
	re := regexp.MustCompile(`XMAS`)
	matches := re.FindAllString(str, -1)
	return len(matches)
}

func rotateGrid90(grid []string) []string {
	rotatedGrid := []string{}
	for i := 0; i < len(grid[0]); i++ {
		rotatedGrid = append(rotatedGrid, "")
	}

	for i := 0; i < len(grid[0]); i++ {
		for j := 0; j < len(grid); j++ {
			rotatedGrid[len(grid)-j-1] += string(grid[i][j])
		}
	}

	return rotatedGrid
}

func rotateGrid45(grid []string) []string {
	rotatedGrid := []string{}
	for sum := 0; sum < len(grid)+len(grid[0]); sum++ {
		rotatedGrid = append(rotatedGrid, "")
	}
	for sum := 0; sum < len(grid)+len(grid[0]); sum++ {
		for i := 0; i < sum+1; i++ {
			if i >= len(grid) {
				continue
			}
			if sum-i >= len(grid[0]) {
				continue
			}
			rotatedGrid[sum] += string(grid[i][sum-i])
		}
	}

	return rotatedGrid
}
