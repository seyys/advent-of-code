package helpers

import (
	"fmt"
	"os"
)

func OpenFile(filepath string) *os.File {
	file, err := os.Open(filepath)
	if err != nil {
		errMessage, _ := fmt.Printf("Error opening file: %s", err)
		panic(errMessage)
	}

	return file
}
