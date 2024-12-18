package day17

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"fmt"
	"math/big"
	"strings"
)

func Part2() {
	file := helpers.OpenFile("./day17/input.txt")

	// var registers Register
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	// registers.A = helpers.Atoi(strings.Split(scanner.Text(), ": ")[1])
	scanner.Scan()
	// registers.B = helpers.Atoi(strings.Split(scanner.Text(), ": ")[1])
	scanner.Scan()
	// registers.C = helpers.Atoi(strings.Split(scanner.Text(), ": ")[1])

	scanner.Scan()
	scanner.Scan()
	program := strings.Split(strings.Split(scanner.Text(), ": ")[1], ",")

	stack := []struct {
		i int
		A *big.Int
	}{{len(program) - 1, big.NewInt(0)}}

	// var B int
	// var C int
	for len(stack) > 0 {
		i := stack[0].i
		A := stack[0].A
		stack = stack[1:]
		println("newLoop", i, A)
		B4 := big.NewInt(int64(helpers.Atoi(program[i])))
		B3 := new(big.Int).Xor(B4, big.NewInt(0b101))
		for c := 0; c < 8; c++ {
			B2 := new(big.Int).Xor(B3, big.NewInt(int64(c)))
			B1 := new(big.Int).Xor(B2, big.NewInt(0b011))
			A1 := new(big.Int).Add(new(big.Int).Lsh(A, 3), B1)
			C := new(big.Int).And(new(big.Int).Rsh(A1, uint(B2.Int64())), big.NewInt(0b111))
			if int(C.Int64()) == c {
				A = A1
				fmt.Printf("A: %b %d\n", A, A)
				fmt.Printf("B1: %b %d\n", B1, B1)
				fmt.Printf("B2: %b %d\n", B2, B2)
				fmt.Printf("B3: %b %d\n", B3, B3)
				fmt.Printf("B4: %b %d\n", B4, B4)
				fmt.Printf("C: %b %d\n", C, C)
				// scanner = bufio.NewScanner(os.Stdin)
				// scanner.Scan()
				if i <= 0 {
					fmt.Println(A.String())
					continue
				}
				stack = append(stack, struct {
					i int
					A *big.Int
				}{i - 1, A})
			}
		}
	}
}
