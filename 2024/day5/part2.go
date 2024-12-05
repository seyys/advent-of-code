package day5

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"strings"
)

func Part2() {
	file := helpers.OpenFile("./day5/input.txt")
	defer file.Close()

	shouldBeBefore := make(map[int]*[]int)

	scanner := bufio.NewScanner(file)
	// Generate map
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			break
		}

		vals := strings.Split(line, "|")
		if len(vals) != 2 {
			panic("Line in wrong format")
		}

		firstVal := helpers.Atoi(vals[0])
		secondVal := helpers.Atoi(vals[1])
		if shouldBeBefore[secondVal] == nil {
			newArray := []int{}
			shouldBeBefore[secondVal] = &newArray
		}
		*shouldBeBefore[secondVal] = append(*shouldBeBefore[secondVal], firstVal)
	}

	total := 0

	// Process pages
	for scanner.Scan() {
		line := scanner.Text()
		pageStrs := strings.Split(line, ",")
		var pages []int
		for _, pageStr := range pageStrs {
			pages = append(pages, helpers.Atoi(pageStr))
		}

		remainingPages := make(map[int]struct{})

		if isValidLine(pages, shouldBeBefore) {
			continue
		}

		for _, page := range pages {
			remainingPages[page] = struct{}{}
		}

		i := 0
		for i < len(pages) {
			if shouldBeBefore[pages[i]] != nil {
				hasIntersection, val := hasIntersection(remainingPages, *shouldBeBefore[pages[i]])
				if hasIntersection {
					idx := findIndex(pages, val)
					pages[i], pages[idx] = pages[idx], pages[i]
					continue
				}
			}
			delete(remainingPages, pages[i])
			i++
		}

		total += pages[len(pages)/2]
	}

	println(total)
}

func hasIntersection(set map[int]struct{}, array []int) (bool, int) {
	for _, val := range array {
		if _, exists := set[val]; exists {
			return true, val
		}
	}
	return false, -1
}

func isValidLine(pages []int, shouldBeBefore map[int]*[]int) bool {
	validLine := true
	shouldNotSeePages := make(map[int]struct{})
	for _, page := range pages {
		if _, exists := shouldNotSeePages[page]; exists {
			validLine = false
			break
		}
		if shouldBeBefore[page] != nil {
			for _, shouldNotSeePage := range *shouldBeBefore[page] {
				shouldNotSeePages[shouldNotSeePage] = struct{}{}
			}
		}
	}
	return validLine
}

func findIndex(slice []int, value int) int {
	for i, v := range slice {
		if v == value {
			return i
		}
	}
	return -1
}
