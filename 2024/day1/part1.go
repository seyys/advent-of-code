package day1

import (
	"advent-of-code-2024/helpers"
	"fmt"
	"regexp"
	"sort"
)

func Part1() {
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

	// Sorting
	sort.Ints(left)
	sort.Ints(right)

	// Calculating
	output := 0
	for i := 0; i < len(left); i++ {
		output += helpers.AbsInt(left[i] - right[i])
	}

	fmt.Println(output)
}
