package day19

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"strings"
	"sync"
	"sync/atomic"
)

func Part2() {
	file := helpers.OpenFile("./day19/input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)

	patterns = make(map[byte][]string)
	scanner.Scan()
	line := scanner.Text()
	for _, pattern := range strings.Split(line, ", ") {
		firstChar := pattern[0]
		patterns[firstChar] = append(patterns[firstChar], pattern)
	}

	scanner.Scan()

	var wg sync.WaitGroup
	var result uint64 = 0

	for scanner.Scan() {
		wg.Add(1)
		line := scanner.Text()

		go func(line string) {
			defer wg.Done()
			numCombinations := isValidPart2(line)
			atomic.AddUint64(&result, uint64(numCombinations))
		}(line)
	}

	wg.Wait()
	println(result)
}

func isValidPart2(remaining string) int {
	if len(remaining) == 0 {
		return 1
	}
	if numCombinations, exists := cache.Load(remaining); exists {
		return numCombinations.(int)
	}

	nextChar := remaining[0]
	result := 0
	for _, pattern := range patterns[nextChar] {
		if len(remaining) < len(pattern) {
			continue
		}
		if remaining[:len(pattern)] != pattern {
			continue
		}
		numCombinations := isValidPart2(remaining[len(pattern):])
		result += numCombinations
		cache.Store(remaining[len(pattern):], numCombinations)
	}

	return result
}
