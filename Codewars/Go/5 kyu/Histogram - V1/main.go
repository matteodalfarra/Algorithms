package kata

import (
	"strings"
	"strconv"
)

func Histogram(rolls [6]int) string {
	graph := "-----------\n1 2 3 4 5 6\n"

	if (rolls[0] == 0 && rolls[1] == 0 && rolls[2] == 0 && rolls[3] == 0 && rolls[4] == 0 && rolls[5] == 0){
		return graph
	}

	max := 0
	for _, value := range rolls{
		if (value > max){
			max = value
		}
	}

	for i:=1; i<=max+1; i++{
		row := ""
		for _, value := range rolls{
		
			if (i <= value){
				row += "# "
			} else if (i == value + 1 && i != 1){
				if (i-1 < 10){
					row += strconv.Itoa(i-1)  + " "
				} else {
					row += strconv.Itoa(i-1)
				}
			} else {
				row += "  "
			}
		}

		graph = strings.TrimRight(row, " ") + "\n" + graph
	}

	return graph
}