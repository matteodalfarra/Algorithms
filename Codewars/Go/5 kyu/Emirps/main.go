package kata

import (
	"math"
	"strconv"
)

func isPrime(n int) bool {
	if (n < 2){
		return false
	}
	
	if (n == 2){
		return true
	}

	sq := int(math.Floor(math.Sqrt(float64(n))))

	for i:=2; i<=sq; i++{
		if (n%i==0){
			return false
		}
	}

	return true
}

func isEmirp(n int) bool {
	reverse := ""
	s := strconv.Itoa(n)

	for i:=len(s)-1;i>=0; i--{
		reverse += string(s[i])
	}
	reverseInt, err := strconv.Atoi(reverse)
	if err != nil {
		return false
	}

	return n != reverseInt && isPrime(reverseInt)
}	

func FindEmirp(n int) [3]int {
	count := 0
	max := 0
	sum := 0
	for i:=0;i<=n;i++{
		if (isPrime(i)){
			if (isEmirp(i)) {
				count += 1
				if (i > max) {
					max = i
				}
				sum += i
			}
		}
	}
	return [3]int{count,max,sum}
}