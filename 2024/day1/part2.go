package day1

import (
	"advent-of-code-2024/helpers"
	"fmt"
	"regexp"
)

func Part2() {
	input := helpers.ParseInput("./day1/input1.txt")

	// Parsing
	var left []int
	var right []int

	for _, val := range input {
		re := regexp.MustCompile(`\d+`)
		matches := re.FindAllString(val, 2)

		left = append(left, helpers.Atoi(matches[0]))
		right = append(right, helpers.Atoi(matches[1]))
	}

	// Generate counter
	counter := make(map[int]int)
	for _, v := range right {
		counter[v]++
	}

	// Calculating
	output := 0
	for _, v := range left {
		output += v * counter[v]
	}

	fmt.Println(output)
}
