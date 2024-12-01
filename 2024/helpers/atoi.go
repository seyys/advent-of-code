package helpers

import "strconv"

func Atoi(str string) int {
	val, err := strconv.Atoi(str)
	if err != nil {
		panic("Parsing error.")
	}

	return val
}