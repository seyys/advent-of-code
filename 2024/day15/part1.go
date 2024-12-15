package day15

import (
	"advent-of-code-2024/helpers"
	"bufio"
)

type EntityType int

const (
	WALL EntityType = iota
	BOX
)

type Entity struct {
	entityType EntityType
}

type Coords struct {
	x, y int
}

func (c1 Coords) Add(c2 Coords) Coords {
	return Coords{c1.x + c2.x, c1.y + c2.y}
}

var directionMap = map[rune]Coords{
	'^': {0, -1},
	'v': {0, 1},
	'<': {-1, 0},
	'>': {1, 0},
}

var entities map[Coords]Entity
var robot Coords

func Part1() {
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
				entities[Coords{c, r}] = Entity{EntityType(WALL)}
			case 'O':
				entities[Coords{c, r}] = Entity{EntityType(BOX)}
			case '@':
				robot = Coords{c, r}
			}
		}
	}

	scanner.Scan()
	instructions = scanner.Text()

	for _, instruction := range instructions {
		processCommand(instruction)
	}

	printGrid()
	println(checkGpsScore())
}

func processCommand(instruction rune) {
	var entitiesToMove []Coords
	coordsToCheck := robot
	direction := directionMap[instruction]

	shouldBreak := false
	for !shouldBreak {
		coordsToCheck = coordsToCheck.Add(direction)
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
	}
}

func checkGpsScore() int {
	score := 0

	for coords, entity := range entities {
		if entity.entityType == EntityType(WALL) {
			continue
		}
		score += coords.x + coords.y*100
	}

	return score
}

func printGrid() {
	for r := 0; r < 10; r++ {
		for c := 0; c < 20; c++ {
			entity, exists := entities[Coords{c, r}]
			if !exists {
				coords := Coords{c, r}
				if coords == robot {
					print("@")
				} else {
					print(".")
				}
				continue
			}
			switch entity.entityType {
			case EntityType(WALL):
				print("#")
			case EntityType(BOX):
				print("O")
			}
		}
		println()
	}
}
