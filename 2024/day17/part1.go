package day17

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"fmt"
	"strconv"
	"strings"
)

type Register struct {
	A, B, C, ins uint64
	out          []string
	err          bool
}

func Part1() {
	file := helpers.OpenFile("./day17/inputtest.txt")

	var registers Register
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	registers.A, _ = strconv.ParseUint(strings.Split(scanner.Text(), ": ")[1], 10, 64)
	scanner.Scan()
	registers.B, _ = strconv.ParseUint(strings.Split(scanner.Text(), ": ")[1], 10, 64)
	scanner.Scan()
	registers.C, _ = strconv.ParseUint(strings.Split(scanner.Text(), ": ")[1], 10, 64)

	scanner.Scan()
	scanner.Scan()
	program := strings.Split(strings.Split(scanner.Text(), ": ")[1], ",")
	fmt.Println(registers)

	for registers.ins = 0; registers.ins < uint64(len(program)) && !registers.err; registers.ins += 2 {
		opcode, _ := strconv.ParseUint(program[registers.ins], 10, 64)
		operand, _ := strconv.ParseUint(program[registers.ins+1], 10, 64)
		registers = doInstruction(opcode, operand, registers)
	}

	println(strings.Join(registers.out, ","))
}

func doInstruction(opcode uint64, literal uint64, registers Register) Register {
	combo := literal
	switch literal {
	case 4:
		combo = registers.A
	case 5:
		combo = registers.B
	case 6:
		combo = registers.C
	case 7:
		registers.err = true
		return registers
	}

	switch opcode {
	case 0:
		return adv(literal, combo, registers)
	case 1:
		return bxl(literal, combo, registers)
	case 2:
		return bst(literal, combo, registers)
	case 3:
		return jnz(literal, combo, registers)
	case 4:
		return bxc(literal, combo, registers)
	case 5:
		return out(literal, combo, registers)
	case 6:
		return bdv(literal, combo, registers)
	case 7:
		return cdv(literal, combo, registers)
	default:
		registers.err = true
		return registers
	}
}

func adv(literal uint64, combo uint64, registers Register) Register {
	numerator := registers.A
	denominator := uint64(0b1 << combo)
	registers.A = numerator / denominator
	return registers
}

func bxl(literal uint64, combo uint64, registers Register) Register {
	registers.B ^= literal
	return registers
}

func bst(literal uint64, combo uint64, registers Register) Register {
	registers.B = combo & 0b111
	return registers
}

func jnz(literal uint64, combo uint64, registers Register) Register {
	if registers.A == 0 {
		return registers
	}
	registers.ins = literal - 2
	return registers
}

func bxc(literal uint64, combo uint64, registers Register) Register {
	registers.B ^= registers.C
	return registers
}

func out(literal uint64, combo uint64, registers Register) Register {
	registers.out = append(registers.out, strconv.Itoa(int(combo&0b111)))
	return registers
}

func bdv(literal uint64, combo uint64, registers Register) Register {
	numerator := registers.A
	denominator := uint64(0b1 << combo)
	registers.B = numerator / denominator
	return registers
}

func cdv(literal uint64, combo uint64, registers Register) Register {
	numerator := registers.A
	denominator := uint64(0b1 << combo)
	registers.C = numerator / denominator
	return registers
}
