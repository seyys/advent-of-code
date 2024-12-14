package day14

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"regexp"
)

type Robot struct {
	x, y, vx, vy int
}

// //test.txt
// const MAX_X = 11
// const MAX_Y = 7

// input.txt
const MAX_X = 101
const MAX_Y = 103

func Part1() {
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

	for i := 0; i < 100; i++ {
		tick(robots)
	}

	println(calculateSafety(robots))
}

func tick(robots []*Robot) {
	for _, robot := range robots {
		robot.x = (((robot.x + robot.vx) % MAX_X) + MAX_X) % MAX_X
		robot.y = (((robot.y + robot.vy) % MAX_Y) + MAX_Y) % MAX_Y
	}
}

func calculateSafety(robots []*Robot) int {
	var quadrant [4]int
	for _, robot := range robots {
		q := findQuadrant(robot.x, robot.y)
		if q == -1 {
			continue
		}
		quadrant[q]++
	}

	result := 1
	for _, val := range quadrant {
		result *= val
	}
	return result
}

func findQuadrant(x int, y int) int {
	midX, midY := MAX_X/2, MAX_Y/2

	switch {
	case x < midX && y < midY:
		return 0
	case x > midX && y < midY:
		return 1
	case x < midX && y > midY:
		return 2
	case x > midX && y > midY:
		return 3
	default:
		return -1
	}
}
