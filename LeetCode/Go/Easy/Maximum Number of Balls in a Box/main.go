func countBalls(lowLimit int, highLimit int) int {
	boxes := make(map[int]int)

	for i := lowLimit; i <= highLimit; i++ {
		box := sumDigit(i)
		if _, exists := boxes[box]; !exists {
			boxes[box] = 1
		} else {
			boxes[box]++
		}
	}

	max := 0
	for _, value := range boxes{
		if value > max{
			max = value
		}
	}

	return max
}

func sumDigit(n int) int {
	s := fmt.Sprintf("%d", n)
	sum := 0
	for _, char := range s {
		digit := int(char - '0')
		sum += digit
	}
	return sum
}