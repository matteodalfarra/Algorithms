func twoSum(nums []int, target int) []int {
    var ind []int

	for i:= 0; i < len(nums); i++{
		man := target - nums[i]
		for j := i+1; j < len(nums); j++ {
			if nums[j] == man {
				ind = append(ind, i) 
				ind = append(ind, j)
				break;
			}
		}

		if len(ind) == 2{
			break;
		}
	}

	if len(ind) == 2{
		return ind
	} else {
		return []int{}
	}
}