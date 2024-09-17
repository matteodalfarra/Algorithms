package kata

func Perimeter(n int) int {
	n1 := 1
	n2 := 1
	n3 := 0
	sum := 2

	for i := 2; i < n+1; i++ {
		n3 = n1 + n2
		sum += n3
		n1 = n2
		n2 = n3
	}

	return 4 * sum
}
