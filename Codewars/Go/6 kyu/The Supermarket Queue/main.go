package kata


func QueueTime(customers []int, n int) int {
	if (n == 1){
		sum := 0
		for i:=0; i<len(customers);i++{
			sum += customers[i]
		}
		return sum
	}
	if (n > len(customers)){
		max := 0
		for _, value := range customers{
			if (value > max){
				max = value
			}
		}

		return max
	}
	
	cas := make(map[int]int)
	for i:=1; i<=n; i++{
		cas[i] = customers[i-1]
	}

	for _, time := range customers[n:]{
        min := int(^uint(0) >> 1)  
        casMin := 0
        for key, value := range cas {
            if value < min {
                min = value
                casMin = key
            }
        }

		cas[casMin] += time
	}


	max := 0
	for _, value := range cas{
		if (value > max){
			max = value
		}
	}

	return max
}