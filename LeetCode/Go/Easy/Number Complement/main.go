func findComplement(num int) int {
	binNum := fmt.Sprintf("%b", num)
	runes := []rune(binNum)
	newBit := ""
	for i := 0; i < len(runes); i++{
		if string(runes[i]) == "1"{
			newBit += "0"
		}  else{
			newBit += "1"
		}
	}

    num64, err := strconv.ParseInt(newBit, 2, 64)
    if err != nil {
        fmt.Println("Errore durante la conversione:", err)
        return 0
    } else{
		return int(num64)
	}
}