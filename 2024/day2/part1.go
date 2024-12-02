package day2

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"fmt"
	"regexp"
)

func Part1() {
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

		var diff []int
		for i := 1; i < len(vals); i++ {
			diff = append(diff, vals[i]-vals[i-1])
		}

		if diff[0] < 0 {
			for i := range diff {
				diff[i] = -diff[i]
			}
		}

		isSafe := true
		for _, val := range diff {
			if val < 1 || val > 3 {
				isSafe = false
				break
			}
		}

		if isSafe {
			numSafe++
		}
	}

	fmt.Println(numSafe)
}
