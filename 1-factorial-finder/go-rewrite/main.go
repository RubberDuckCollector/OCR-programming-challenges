package main

import (
	"fmt"
)

func factorial_rec(n int) int {
	if n < 2 {
		return 1
	} else {
		return n * factorial_rec(n-1)
	}
}

func factorial_it(n int) int {
	fact := 1

	for n > 0 {
		fact *= n
		n--
	}

	return fact
}

func main() {
	// recursive
	for i := 0; i < 6; i++ {
		fmt.Printf("rec. %d: %d\n", i, factorial_rec(i))
	}

	fmt.Println("")

	// iterative
	for i := 0; i < 6; i++ {
		fmt.Printf("it. %d: %d\n", i, factorial_it(i))
	}
}
