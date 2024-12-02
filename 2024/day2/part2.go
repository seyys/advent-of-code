package day2

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"fmt"
	"regexp"
)

func Part2() {
	numSafe := 0

	re := regexp.MustCompile(`\d+`)

	file := helpers.OpenFile("./day2/input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()

		var vals []int
		for _, strVal := range re.FindAllString(line, -1) {
			vals = append(vals, helpers.Atoi(strVal))
		}

		isSafe, idx := checkIsSafe(vals)

		if isSafe {
			numSafe++
			continue
		}

		for i := min(0, idx-2); i <= idx; i++ {
			slicedVals := removeElement(vals, i)
			isSafe, _ := checkIsSafe(slicedVals)
			if isSafe {
				numSafe++
				break
			}
		}
	}

	fmt.Println(numSafe)
}

func checkIsSafe(arr []int) (bool, int) {
	var diff []int
	for i := 1; i < len(arr); i++ {
		diff = append(diff, arr[i]-arr[i-1])
	}

	if diff[0] < 0 {
		for i := range diff {
			diff[i] = -diff[i]
		}
	}

	isSafe := true
	var maxIdx int
	for i, val := range diff {
		if val < 1 || val > 3 {
			isSafe = false
			maxIdx = i + 1
			break
		}
	}

	return isSafe, maxIdx
}

func removeElement(slice []int, index int) []int {
	var output []int
	for i, val := range slice {
		if i == index {
			continue
		}
		output = append(output, val)
	}

	return output
}
