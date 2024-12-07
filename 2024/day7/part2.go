package day7

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"strconv"
	"strings"
)

func Part2() {
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
		if isValidLineDay7Part2(0, totalLine, values) {
			totalCalibration += totalLine
		}
	}

	println(totalCalibration)
}

func isValidLineDay7Part2(runningTotal int, total int, values []int) bool {
	if len(values) == 0 {
		return runningTotal == total
	}
	return isValidLineDay7Part2(runningTotal*values[0], total, values[1:]) ||
		isValidLineDay7Part2(runningTotal+values[0], total, values[1:]) ||
		isValidLineDay7Part2(concat(runningTotal, values[0]), total, values[1:])
}

func concat(a int, b int) int {
	return helpers.Atoi(strconv.Itoa(a) + strconv.Itoa(b))
}
