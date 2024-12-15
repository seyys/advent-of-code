package day15

import (
	"advent-of-code-2024/helpers"
	"bufio"
)

func Part2() {
	file := helpers.OpenFile("./day15/input.txt")

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
				entities[Coords{2 * c, r}] = Entity{EntityType(BOX_LEFT)}
				entities[Coords{2*c + 1, r}] = Entity{EntityType(BOX_RIGHT)}
			case '@':
				robot = Coords{2 * c, r}
			}
		}
	}

	scanner.Scan()
	instructions = scanner.Text()
	// printGrid()

	// scanner = bufio.NewScanner(os.Stdin)
	for _, instruction := range instructions {
		// scanner.Scan()
		processCommandPart2(instruction)
		// fmt.Println(string(instruction))
		// printGrid()
	}

	printGrid()
	println(checkGpsScore())
}

func processCommandPart2(instruction rune) {
	entitiesToMoveMap := make(map[Coords]struct{})
	var entitiesToMove []Coords
	coordsToCheck := []Coords{robot}
	direction := directionMap[instruction]

	shouldBreak := false
	for !shouldBreak {
		for i, coords := range coordsToCheck {
			coordsToCheck[i] = coords.Add(direction)
		}
		// fmt.Println(coordsToCheck)

		var newCoordsToCheck []Coords
		allEmpty := true
		for _, coords := range coordsToCheck {
			entity, exists := entities[coords]
			if !exists {
				continue
			}
			allEmpty = false
			switch entity.entityType {
			case EntityType(WALL):
				shouldBreak = true
			case EntityType(BOX_LEFT):
				if _, exists := entitiesToMoveMap[coords]; !exists {
					entitiesToMove = append(entitiesToMove, coords)
					entitiesToMove = append(entitiesToMove, coords.Add(directionMap['>']))
					entitiesToMoveMap[coords] = struct{}{}
					entitiesToMoveMap[coords.Add(directionMap['>'])] = struct{}{}
					newCoordsToCheck = append(newCoordsToCheck, coords)
					newCoordsToCheck = append(newCoordsToCheck, coords.Add(directionMap['>']))
				}
			case EntityType(BOX_RIGHT):
				if _, exists := entitiesToMoveMap[coords]; !exists {
					entitiesToMove = append(entitiesToMove, coords)
					entitiesToMove = append(entitiesToMove, coords.Add(directionMap['<']))
					entitiesToMoveMap[coords] = struct{}{}
					entitiesToMoveMap[coords.Add(directionMap['<'])] = struct{}{}
					newCoordsToCheck = append(newCoordsToCheck, coords)
					newCoordsToCheck = append(newCoordsToCheck, coords.Add(directionMap['<']))
				}
			}
		}
		coordsToCheck = newCoordsToCheck
		if allEmpty {
			robot = robot.Add(direction)
			for i := len(entitiesToMove) - 1; i >= 0; i-- {
				entity := entities[entitiesToMove[i]]
				entities[entitiesToMove[i].Add(direction)] = entity
				delete(entities, entitiesToMove[i])
			}
			shouldBreak = true
		}
	}
}
