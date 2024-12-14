package helpers

import "strconv"

func Atof64(str string) float64 {
	val, err := strconv.Atoi(str)
	if err != nil {
		panic(err)
	}

	return float64(val)
}
