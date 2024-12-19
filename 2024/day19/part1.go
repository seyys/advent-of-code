package day19

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"strings"
	"sync"
	"sync/atomic"
)

var patterns map[byte][]string
var cache sync.Map

func Part1() {
	file := helpers.OpenFile("./day19/input.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)

	patterns = make(map[byte][]string)
	scanner.Scan()
	line := scanner.Text()
	for _, pattern := range strings.Split(line, ", ") {
		firstChar := []byte(pattern)[0]
		patterns[firstChar] = append(patterns[firstChar], pattern)
	}

	scanner.Scan()

	var wg sync.WaitGroup
	var result int32 = 0

	for scanner.Scan() {
		wg.Add(1)
		line := scanner.Text()

		go func(line string) {
			defer wg.Done()
			if isValid(line) {
				atomic.AddInt32(&result, 1)
			}
		}(line)
	}

	wg.Wait()
	println(result)
}

func isValid(remaining string) bool {
	if len(remaining) == 0 {
		return true
	}
	if valid, exists := cache.Load(remaining); exists {
		return valid.(bool)
	}

	nextChar := []byte(remaining)[0]
	for _, pattern := range patterns[nextChar] {
		if len(remaining) < len(pattern) {
			continue
		}
		if remaining[:len(pattern)] != pattern {
			continue
		}
		result := isValid(remaining[len(pattern):])
		if result {
			cache.Store(remaining, true)
			return true
		}
	}

	cache.Store(remaining, false)
	return false
}
