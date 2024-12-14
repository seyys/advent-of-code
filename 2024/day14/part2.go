package day14

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"math"
	"regexp"
	"sync"
	"sync/atomic"
)

// Point represents a 2D coordinate
type Point struct {
	X, Y int
}

func Part2() {
	file := helpers.OpenFile("./day14/input.txt")

	re := regexp.MustCompile(`p=(\d+),(\d+)\s*v=(-?\d+),(-?\d+)`)

	var robots []*Robot

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()

		parsedLine := re.FindAllStringSubmatch(line, 1)[0]

		robot := Robot{
			x:  helpers.Atoi(parsedLine[1]),
			y:  helpers.Atoi(parsedLine[2]),
			vx: helpers.Atoi(parsedLine[3]),
			vy: helpers.Atoi(parsedLine[4]),
		}

		robots = append(robots, &robot)
	}

	var wg sync.WaitGroup
	var stop int32 = 0
	var iResult int
	var result []Robot

	for i := 0; ; i++ {
		if atomic.LoadInt32(&stop) == 1 {
			break
		}
		var theseRobots []Robot
		for _, robot := range robots {
			theseRobots = append(theseRobots, *robot)
		}

		wg.Add(1)
		go func(robots []Robot, i int) {
			defer wg.Done()

			var points []Point
			for _, robot := range robots {
				points = append(points, Point{X: robot.x, Y: robot.y})
			}
			largestCluster := findLargestCluster(points)
			if largestCluster > 20 {
				iResult = i
				result = append(result, robots...)
				atomic.StoreInt32(&stop, 1)
			}
		}(theseRobots, i)

		tick(robots)
	}

	wg.Wait()

	println(iResult)
	printGrid(result)
}

func printGrid(robots []Robot) {
	robotsPositions := make(map[[2]int]struct{})
	for _, robot := range robots {
		robotsPositions[[2]int{robot.x, robot.y}] = struct{}{}
	}

	for r := 0; r < MAX_Y; r++ {
		for c := 0; c < MAX_X; c++ {
			if _, exists := robotsPositions[[2]int{c, r}]; exists {
				print("x")
			} else {
				print(".")
			}
		}
		println()
	}
}

// isAdjacent checks if two points are adjacent (horizontally or vertically)
func isAdjacent(p1, p2 Point) bool {
	dx := int(math.Abs(float64(p1.X - p2.X)))
	dy := int(math.Abs(float64(p1.Y - p2.Y)))
	return (dx == 1 && dy == 0) || (dx == 0 && dy == 1)
}

// findLargestCluster finds the largest cluster of adjacent points
func findLargestCluster(points []Point) int {
	visited := make(map[Point]bool)
	largestCluster := []Point{}

	for _, point := range points {
		if !visited[point] {
			// Get the current cluster using DFS
			cluster := dfs(point, points, visited)
			if len(cluster) > len(largestCluster) {
				largestCluster = cluster
			}
		}
	}

	return len(largestCluster)
}

// dfs performs depth-first search to find all points in the cluster
func dfs(start Point, points []Point, visited map[Point]bool) []Point {
	stack := []Point{start}
	cluster := []Point{}

	for len(stack) > 0 {
		current := stack[len(stack)-1] // Get the last element from the stack
		stack = stack[:len(stack)-1]   // Pop the element from the stack

		if visited[current] {
			continue
		}

		visited[current] = true
		cluster = append(cluster, current)

		// Check for all adjacent points
		for _, neighbor := range points {
			if !visited[neighbor] && isAdjacent(current, neighbor) {
				stack = append(stack, neighbor)
			}
		}
	}

	return cluster
}
