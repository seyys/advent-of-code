package day15

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"fmt"
	"os"
)

func Part2() {
	file := helpers.OpenFile("./day15/test3.txt")

	entities = make(map[Coords]Entity)
	var instructions string

	scanner := bufio.NewScanner(file)
	for r := 0; scanner.Scan(); r++ {
		line := scanner.Text()

		if line == "" {
			break
		}

		for c, ch := range line {
			switch ch {
			case '#':
				entities[Coords{2 * c, r}] = Entity{EntityType(WALL)}
				entities[Coords{2*c + 1, r}] = Entity{EntityType(WALL)}
			case 'O':
				entities[Coords{2 * c, r}] = Entity{EntityType(BOX)}
			case '@':
				robot = Coords{2 * c, r}
			}
		}
	}

	scanner.Scan()
	instructions = scanner.Text()
	printGrid()

	scanner = bufio.NewScanner(os.Stdin)
	for _, instruction := range instructions {
		if instruction == '>' || instruction == '<' {
			processCommandHorizontal(instruction)
		} else {
			processCommandVertical(instruction)
		}
		printGrid()
		scanner.Scan()
	}

	printGrid()
	println(checkGpsScore())
}

func processCommandVertical(instruction rune) {
	var entitiesToMove []Coords
	coordsToCheck := make(map[Coords]struct{})
	coordsToCheck[robot] = struct{}{}
	coordsToCheck[robot.Add(directionMap['<'])] = struct{}{}
	direction := directionMap[instruction]

	shouldBreak := false
	for !shouldBreak {
		var oldCoords []Coords
		for coords := range coordsToCheck {
			coordsToCheck[coords.Add(direction)] = struct{}{}
			oldCoords = append(oldCoords, coords)
		}
		for _, coords := range oldCoords {
			delete(coordsToCheck, coords)
		}
		fmt.Println(coordsToCheck)

		for coords := range coordsToCheck {
			if shouldBreak {
				break
			}
			entity, exists := entities[coords]
			if !exists {
				robot = robot.Add(direction)
				for i := len(entitiesToMove) - 1; i >= 0; i-- {
					entity := entities[entitiesToMove[i]]
					delete(entities, entitiesToMove[i])
					entities[entitiesToMove[i].Add(direction)] = entity
				}
				shouldBreak = true
				break
			}
			switch entity.entityType {
			case EntityType(WALL):
				shouldBreak = true
			case EntityType(BOX):
				entitiesToMove = append(entitiesToMove, coords)
				coordsToCheck[coords.Add(directionMap['<'])] = struct{}{}
				coordsToCheck[coords.Add(directionMap['>'])] = struct{}{}
			}
		}
	}
}

func processCommandHorizontal(instruction rune) {
	var entitiesToMove []Coords
	direction := directionMap[instruction]
	coordsToCheck := robot.Add(direction)
	if direction == directionMap['<'] {
		coordsToCheck = coordsToCheck.Add(direction)
	}

	shouldBreak := false
	for !shouldBreak {
		entity, exists := entities[coordsToCheck]
		if !exists {
			robot = robot.Add(direction)
			for i := len(entitiesToMove) - 1; i >= 0; i-- {
				entity := entities[entitiesToMove[i]]
				delete(entities, entitiesToMove[i])
				entities[entitiesToMove[i].Add(direction)] = entity
			}
			break
		}
		switch entity.entityType {
		case EntityType(WALL):
			shouldBreak = true
		case EntityType(BOX):
			entitiesToMove = append(entitiesToMove, coordsToCheck)
		}
		coordsToCheck = coordsToCheck.Add(direction).Add(direction)
	}
}
