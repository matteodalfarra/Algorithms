package kata

import (
	"math"
)

func IsPrime(n int) bool {
  if (n < 2) {
    return false
  }
  sq := int(math.Floor(math.Sqrt(float64(n)))) 

	for i:=2; i<=sq; i++{
		if (n % i == 0){
			return false
		}
	}
	return true
}