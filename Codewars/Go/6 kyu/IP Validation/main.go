package kata

import (
	"strings"
	"strconv"
)

func Is_valid_ip(ip string) bool {
	s := strings.Split(ip, ".")
	l := len(s) 
	if (l != 4){
		return false
	}

    for i := 0; i < l; i++ {
		octet := s[i]
		lo := len(octet)
		if (lo > 3){
			return false
		}

		if (lo == 3 && octet[0] == '0'){
			return false
		} else if (lo == 2 && octet[0] == '0'){
			return false
		}

		val, err := strconv.Atoi(octet)
		if err != nil {
			return false
		}
		if val > 255 || val < 0 {
			return false
		}
	}
	return true
}