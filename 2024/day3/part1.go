package day3

import (
	"advent-of-code-2024/helpers"
	"fmt"
	"regexp"
	"strings"
)

func Part1() {
	result := 0

	inputRaw := helpers.ParseInput("./day3/input.txt")
	input := strings.Join(inputRaw, "")

	re := regexp.MustCompile(`mul\((\d+),(\d+)\)`)

	matches := re.FindAllStringSubmatch(input, -1)

	for _, match := range matches {
		result += helpers.Atoi(match[1]) * helpers.Atoi(match[2])
	}

	fmt.Println(result)
}
