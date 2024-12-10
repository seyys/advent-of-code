package day11

import (
	"advent-of-code-2024/helpers"
	"strconv"
	"strings"
)

func Part2() {
	inputStr := helpers.ParseInput("./day11/input.txt")[0]

	input := make(map[int]int)
	for _, str := range strings.Split(inputStr, " ") {
		input[helpers.Atoi(str)]++
	}

	for repeat := 0; repeat < 75; repeat++ {
		inputCopy := make(map[int]int)
		for key, val := range input {
			inputCopy[key] = val
		}
		input = make(map[int]int)
		for val := range inputCopy {
			if val == 0 {
				input[1] += inputCopy[val]
				continue
			}
			numDigits, left, right := numberOfDigitsPart2(val)
			if numDigits%2 == 0 {
				input[left] += inputCopy[val]
				input[right] += inputCopy[val]
				continue
			}
			input[val*2024] += inputCopy[val]
		}
	}

	total := 0
	for _, val := range input {
		total += val
	}

	println(total)
}

func numberOfDigitsPart2(val int) (int, int, int) {
	valStr := strconv.Itoa(val)
	lenStr := len(valStr)
	var left, right int
	if lenStr%2 == 0 {
		left = helpers.Atoi(valStr[:lenStr/2])
		right = helpers.Atoi(valStr[lenStr/2:])
	}
	return lenStr, left, right
}
