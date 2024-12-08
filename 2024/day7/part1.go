package day7

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"strings"
)

func Part1() {
	file := helpers.OpenFile("./day7/input.txt")
	defer file.Close()

	totalCalibration := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.Fields(strings.ReplaceAll(scanner.Text(), ":", ""))
		totalLine := helpers.Atoi(line[0])
		values := []int{}
		for _, val := range line[1:] {
			values = append(values, helpers.Atoi(val))
		}
		if isValidLine(0, totalLine, values) {
			totalCalibration += totalLine
		}
	}

	println(totalCalibration)
}

func isValidLine(runningTotal int, total int, values []int) bool {
	if runningTotal > total {
		return false
	}
	if len(values) == 0 {
		return runningTotal == total
	}
	return isValidLine(runningTotal*values[0], total, values[1:]) ||
		isValidLine(runningTotal+values[0], total, values[1:])
}
