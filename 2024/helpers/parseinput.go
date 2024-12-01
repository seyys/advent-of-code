package helpers

import (
	"bufio"
)

func ParseInput(filepath string) []string {
	var input []string

	file := OpenFile(filepath)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		input = append(input, scanner.Text())
	}

	return input
}
