package kata

func GetMiddle(s string) string {
  n := len(s)
	index := (len(s) - 1) / 2
	char := ""
	if (n % 2 == 0){
		char = string(s[index:index+2])
	} else if (n == 1) {
		return s
	} else {
		char = string(s[index])
	} 
	return char
}