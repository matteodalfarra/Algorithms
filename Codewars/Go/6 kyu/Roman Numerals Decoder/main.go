package kata

func Decode(roman string) int {
  	legend := make(map[string]int)
	legend["I"] = 1
	legend["V"] = 5
	legend["X"] = 10
	legend["L"] = 50
	legend["C"] = 100
	legend["D"] = 500
	legend["M"] = 1000

	sum := 0
	for i:=len(roman)-1;i>=0;i--{
		if (i>0){
			if (legend[string(roman[i])] > legend[string(roman[i-1])]){
				sum += legend[string(roman[i])] - legend[string(roman[i-1])]
				i-=1
			} else {
				sum += legend[string(roman[i])]
			}
		} else {
			sum += legend[string(roman[i])]
		}
	}

	return sum
}