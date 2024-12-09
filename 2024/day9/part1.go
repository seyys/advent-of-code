package day9

import (
	"advent-of-code-2024/helpers"
)

func Part1() {
	input := helpers.ParseInput("./day9/input.txt")[0]

	var fs []int
	isFile := true
	id := 0
	for _, block := range input {
		if isFile {
			catRepeatValsToArray(&fs, id, int(block-'0'))
			id++
		} else {
			catRepeatValsToArray(&fs, -1, int(block-'0'))
		}
		isFile = !isFile
	}

	left := 0
	right := len(fs) - 1
	for {
		for left < len(fs) && fs[left] != -1 {
			left++
		}
		for right >= 0 && fs[right] == -1 {
			right--
			pop(&fs)
		}
		if left >= right || left > len(fs) {
			break
		}
		fs[left] = fs[right]
		pop(&fs)
		left++
		right--
	}

	result := calculateChecksum(fs)

	println(result)
}

func catRepeatValsToArray(arr *[]int, val int, repeatTimes int) {
	for i := 0; i < repeatTimes; i++ {
		*arr = append(*arr, val)
	}
}

func pop(alist *[]int) int {
	f := len(*alist)
	rv := (*alist)[f-1]
	*alist = (*alist)[:f-1]
	return rv
}

func calculateChecksum(fileSystem []int) int {
	result := 0
	for i, val := range fileSystem {
		result += i * val
	}

	return result
}
