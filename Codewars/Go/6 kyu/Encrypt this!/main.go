package kata

import (
	"strings"
	"strconv"
)

func EncryptThis(s string) string {
	words := strings.Split(s, " ")

	sEnc := ""

	for _, word := range words{
		for j, letter := range word{
			if (j == 0){
				sEnc += strconv.Itoa(int(letter))
			} else if (j == 1){
				sEnc += string(word[len(word)-1])
			} else if (j == len(word) -1){
				sEnc += string(word[1])
			} else {
				sEnc += string(letter)
			}
		}

		sEnc += " "
	}

	return strings.TrimRight(sEnc, " ")
}