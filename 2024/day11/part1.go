package day11

import (
	"advent-of-code-2024/helpers"
	"strconv"
	"strings"
)

func Part1() {
	inputStr := helpers.ParseInput("./day11/input.txt")[0]

	var input []int
	for _, str := range strings.Split(inputStr, " ") {
		input = append(input, helpers.Atoi(str))
	}

	for repeat := 0; repeat < 25; repeat++ {
		for i, val := range input {
			if val == 0 {
				input[i] = 1
				continue
			}
			numDigits, left, right := numberOfDigits(val)
			if numDigits%2 == 0 {
				input[i] = left
				input = append(input, right)
				continue
			}
			input[i] *= 2024
		}
	}

	println(len(input))
}

func numberOfDigits(val int) (int, int, int) {
	valStr := strconv.Itoa(val)
	lenStr := len(valStr)
	var left, right int
	if lenStr%2 == 0 {
		left = helpers.Atoi(valStr[:lenStr/2])
		right = helpers.Atoi(valStr[lenStr/2:])
	}
	return lenStr, left, right
}
