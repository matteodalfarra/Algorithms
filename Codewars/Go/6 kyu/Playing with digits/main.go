package kata

import (
	"strconv"
)

func DigPow(n, p int) int {
  	s := strconv.Itoa(n)
	sum := 0

	for _, value := range s{
		cprod := 1
		c, err := strconv.Atoi(string(value))
		if err != nil {
			return -1
		}
		for i:=1; i<=p; i++{
			cprod *= c  
		}
		p+=1
		sum += cprod
		cprod = 0
	}

	if (sum % n == 0){
		return sum / n
	} else {
		return -1
	}
}