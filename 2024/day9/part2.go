package day9

import (
	"advent-of-code-2024/helpers"
)

type Block struct {
	size int
	id   int
}

func Part2() {
	input := helpers.ParseInput("./day9/input.txt")[0]

	var fsRepresentation []Block
	isFile := true
	id := 0
	for _, block := range input {
		blockSize := int(block) - '0'
		if isFile {
			fsRepresentation = append(fsRepresentation, Block{size: blockSize, id: id})
			id++
		} else {
			fsRepresentation = append(fsRepresentation, Block{size: blockSize, id: -1})
		}
		isFile = !isFile
	}

	right := len(fsRepresentation) - 1
	for ; right >= 0; right-- {
		if fsRepresentation[right].id == -1 {
			continue
		}
		blockSize := fsRepresentation[right].size
		for left := 0; left < right; left++ {
			if fsRepresentation[left].id == -1 && fsRepresentation[left].size >= blockSize {
				remainder := fsRepresentation[left].size - blockSize
				insertBlocks := []Block{{size: blockSize, id: fsRepresentation[right].id}}
				if remainder > 0 {
					insertBlocks = append(insertBlocks, Block{size: remainder, id: -1})
					right++
				}
				fsRepresentation = append(fsRepresentation[:left], append(insertBlocks, fsRepresentation[left+1:]...)...)
				fsRepresentation[right].id = -1
				break
			}
		}
	}

	var fs []int
	for _, block := range fsRepresentation {
		id := block.id
		if id < 0 {
			id = 0
		}
		catRepeatValsToArray(&fs, id, block.size)
	}

	result := calculateChecksum(fs)

	println(result)
}
