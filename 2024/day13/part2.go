package day13

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"math/big"
	"regexp"
)

func Part2() {
	file := helpers.OpenFile("./day13/input.txt")
	defer file.Close()

	total := uint64(0)

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		aStr := scanner.Text()
		scanner.Scan()
		bStr := scanner.Text()
		scanner.Scan()
		prizeStr := scanner.Text()
		scanner.Scan()

		total += calcMinStepsPart2(aStr, bStr, prizeStr)
	}

	println(total)
}

func calcMinStepsPart2(aStr string, bStr string, prizeStr string) uint64 {
	re, err := regexp.Compile(`[XY].{0,1}([-+]*\d*)`)
	if err != nil {
		panic(err)
	}

	aMatch := re.FindAllStringSubmatch(aStr, 2)
	aX := big.NewInt(int64(helpers.Atoi(aMatch[0][1])))
	aY := big.NewInt(int64(helpers.Atoi(aMatch[1][1])))

	bMatch := re.FindAllStringSubmatch(bStr, 2)
	bX := big.NewInt(int64(helpers.Atoi(bMatch[0][1])))
	bY := big.NewInt(int64(helpers.Atoi(bMatch[1][1])))

	prizeMatch := re.FindAllStringSubmatch(prizeStr, 2)
	pX := new(big.Int).Add(big.NewInt(int64(helpers.Atoi(prizeMatch[0][1]))), big.NewInt(10000000000000))
	pY := new(big.Int).Add(big.NewInt(int64(helpers.Atoi(prizeMatch[1][1]))), big.NewInt(10000000000000))

	a, remA := new(big.Int).DivMod(
		new(big.Int).Sub(new(big.Int).Mul(bX, pY), new(big.Int).Mul(bY, pX)),
		new(big.Int).Sub(new(big.Int).Mul(aY, bX), new(big.Int).Mul(aX, bY)),
		new(big.Int),
	)
	b, remB := new(big.Int).DivMod(
		new(big.Int).Sub(new(big.Int).Mul(aX, pY), new(big.Int).Mul(aY, pX)),
		new(big.Int).Sub(new(big.Int).Mul(aX, bY), new(big.Int).Mul(aY, bX)),
		new(big.Int),
	)

	if remA.Int64() != 0 || remB.Int64() != 0 {
		return 0
	}

	if a.Int64() < 0 || b.Int64() < 0 {
		return 0
	}

	return new(big.Int).Add(new(big.Int).Mul(a, big.NewInt(3)), b).Uint64()
}
