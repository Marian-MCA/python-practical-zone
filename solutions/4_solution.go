// https://leetcode.com/problems/valid-palindrome/

package main

import (
	"fmt"
	"strings"
	"unicode"
)

func isIgnoreCase(s rune) bool {
	if unicode.IsLetter(s) || unicode.IsDigit(s) {
		return false
	}
	return true
}
func isPalindrome(s string) bool {

	valid_string := ""
	for _, str := range s {
		if !isIgnoreCase(rune(str)) {
			valid_string += string(str)
		}
	}

	tempStr := strings.ToLower(valid_string)
	dummyString := ""

	for i := len(tempStr) - 1; i >= 0; i-- {
		dummyString += string(tempStr[i])
	}

	return strings.ToLower(valid_string) == string(dummyString)
}

func main() {
	testString := []string{"A man, a plan, a canal: Panama", "race a car", "mala:y:alam", " ", "0P"}

	for _, s := range testString {
		fmt.Println(isPalindrome(s))
	}
}
