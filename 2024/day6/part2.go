package day6

import (
	"fmt"
	"os"
	"sync"
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

	// Narrow search space by only placing obstacles on the path that the guard patrols
	r := startR
	c := startC
	dir := [2]int{-1, 0}
	obstaclePositions := [][2]int{}
	for {
		if r+dir[0] < 0 || r+dir[0] >= len(grid) || c+dir[1] < 0 || c+dir[1] >= len(grid[0]) {
			break
		}
		nextChar := grid[r+dir[0]][c+dir[1]]
		if nextChar == '#' {
			dir[0], dir[1] = dir[1], -dir[0]
		} else {
			if grid[r][c] != 'X' {
				obstaclePositions = append(obstaclePositions, [2]int{r, c})
			}
			grid[r][c] = 'X'
			r += dir[0]
			c += dir[1]
		}
	}

	// Count number of positions obstructions can be placed to make guard loop
	count := 0
	var mu sync.Mutex
	var wg sync.WaitGroup

	// Channel to collect results from goroutines
	results := make(chan int, len(grid)*len(grid[0])) // buffer size to avoid blocking

	for _, obstaclePosition := range obstaclePositions {
		r := obstaclePosition[0]
		c := obstaclePosition[1]

		// Increment the WaitGroup counter for each goroutine
		wg.Add(1)

		// Launch a goroutine for each valid iteration
		go func(r, c int) {
			defer wg.Done() // Decrement the WaitGroup counter when the goroutine is done

			newGrid := make([][]byte, len(grid))
			for i := range grid {
				newGrid[i] = make([]byte, len(grid[i]))
				copy(newGrid[i], grid[i])
			}
			newGrid[r][c] = '#'

			if isLoop(startR, startC, newGrid) {
				mu.Lock()
				results <- 1
				mu.Unlock()
			} else {
				results <- 0
			}
		}(r, c) // Pass current r and c to the goroutine
	}

	wg.Wait()
	close(results)

	for result := range results {
		count += result
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
