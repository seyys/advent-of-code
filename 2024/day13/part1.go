package day13

import (
	"advent-of-code-2024/helpers"
	"bufio"
	"math"
	"regexp"

	"gonum.org/v1/gonum/mat"
)

func Part1() {
	file := helpers.OpenFile("./day13/input.txt")
	defer file.Close()

	total := 0

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		aStr := scanner.Text()
		scanner.Scan()
		bStr := scanner.Text()
		scanner.Scan()
		prizeStr := scanner.Text()
		scanner.Scan()

		total += calcMinSteps(aStr, bStr, prizeStr)
	}

	println(total)
}

func calcMinSteps(aStr string, bStr string, prizeStr string) int {
	re, err := regexp.Compile(`[XY].{0,1}([-+]*\d*)`)
	if err != nil {
		panic(err)
	}

	aMatch := re.FindAllStringSubmatch(aStr, 2)
	aX := helpers.Atof64(aMatch[0][1])
	aY := helpers.Atof64(aMatch[1][1])

	bMatch := re.FindAllStringSubmatch(bStr, 2)
	bX := helpers.Atof64(bMatch[0][1])
	bY := helpers.Atof64(bMatch[1][1])

	prizeMatch := re.FindAllStringSubmatch(prizeStr, 2)
	prizeX := helpers.Atof64(prizeMatch[0][1])
	prizeY := helpers.Atof64(prizeMatch[1][1])
	prize := mat.NewVecDense(2, []float64{prizeX, prizeY})

	coeffs := mat.NewDense(2, 2, []float64{
		aX, bX,
		aY, bY,
	})

	var x mat.VecDense
	if ok := x.SolveVec(coeffs, prize); ok != nil {
		return 0
	}

	tokensA := x.AtVec(0)
	tokensB := x.AtVec(1)

	if math.Abs(tokensA-math.Round(tokensA)) > 0.0000001 ||
		math.Abs(tokensB-math.Round(tokensB)) > 0.0000001 {
		return 0
	}

	return int(math.Round(3*tokensA + tokensB))
}
