package main

import (
	"fmt"
	"strings"
)

func prefixThere(str []string, pf string) bool {
	present := ""
	for _, ss := range str {
		if !strings.HasPrefix(ss, pf) {
			present += "n"
		}
	}
	if strings.Contains(present, "n") {
		return false
	}
	return true
}

func longestCommonPrefix(strs []string) string {

	longPrefix := ""
	firstString := strs[0]
	restOfString := strs[1:]

	if len(strs) == 1 {
		longPrefix = firstString
	} else {
		for i := 1; i <= len(firstString); i++ {
			prefix := firstString[0:i]
			if prefixThere(restOfString, prefix) {
				longPrefix = prefix
			}
		}
	}
	return longPrefix
}

func main() {
	sSlice := []string{"flower", "flow", "flight"}
	fmt.Println(longestCommonPrefix(sSlice))
}