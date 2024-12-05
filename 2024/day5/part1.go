package day5

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"strings"
)

func Part1() {
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
		pages := strings.Split(line, ",")
		shouldNotSeePages := make(map[int]struct{})

		validLine := true
		for _, pageStr := range pages {
			page := helpers.Atoi(pageStr)
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

		if validLine {
			total += helpers.Atoi(string(pages[len(pages)/2]))
		}
	}

	println(total)
}
