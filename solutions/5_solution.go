func isPalindrome(x int) bool {
	temp := x
	sum := 0
	rem := 0

	for x > 0 {
		rem = x % 10
		sum = (sum * 10) + rem
		x /= 10
	}

	if sum == temp {
		return true
	}
	return false
}
