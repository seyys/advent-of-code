package day3

import (
	"advent-of-code-2024/helpers"
	"fmt"
	"regexp"
	"strings"
)

func Part2() {
	result := 0

	inputRaw := helpers.ParseInput("./day3/input.txt")
	input := strings.Join(inputRaw, "")

	reEnableIdx := regexp.MustCompile(`do\(\)`)
	reDisableIdx := regexp.MustCompile(`don't\(\)`)

	matchesEnable := reEnableIdx.FindAllStringIndex(input, -1)
	matchesDisable := reDisableIdx.FindAllStringIndex(input, -1)

	matchesEnableIdx := []int{0}
	for _, val := range matchesEnable {
		matchesEnableIdx = append(matchesEnableIdx, val[0])
	}

	var matchesDisableIdx []int
	for _, val := range matchesDisable {
		matchesDisableIdx = append(matchesDisableIdx, val[0])
	}

	pEnable := 0
	pDisable := 0

	var inputEnabled string
	for pEnable < len(matchesEnable) {
		for pDisable < len(matchesDisableIdx) && matchesDisableIdx[pDisable] < matchesEnableIdx[pEnable] {
			pDisable++
		}
		if pDisable >= len(matchesDisableIdx) {
			inputEnabled += input[matchesEnableIdx[pEnable]:]
			break
		}

		inputEnabled += input[matchesEnableIdx[pEnable]:matchesDisableIdx[pDisable]]

		for pEnable < len(matchesEnableIdx) && matchesEnableIdx[pEnable] < matchesDisableIdx[pDisable] {
			pEnable++
		}
	}

	re := regexp.MustCompile(`mul\((\d+),(\d+)\)`)

	matches := re.FindAllStringSubmatch(inputEnabled, -1)

	for _, match := range matches {
		result += helpers.Atoi(match[1]) * helpers.Atoi(match[2])
	}

	fmt.Println(result)
}
