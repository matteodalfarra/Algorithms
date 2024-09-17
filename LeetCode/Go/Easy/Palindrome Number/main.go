func isPalindrome(x int) bool {
    if strconv.Itoa(x) == reverse(strconv.Itoa(x)){
        return true
	} else {
		return false
	}
}

func reverse(x string) string{
	runes := []rune(x)
	newStr := ""

	for i := len(runes)-1; i >= 0; i--{
		newStr += string(runes[i]) 
	} 

	return newStr
}