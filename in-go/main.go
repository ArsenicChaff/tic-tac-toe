package main

import (
	"bufio"
	"fmt"
	"os"
)

func readUserInput() string {
	// var reader *bufio.Reader
	var reader *bufio.Reader = bufio.NewReader(os.Stdin) // Initialize 'reader' with the return value of bufio.NewReader

	fmt.Print("Input: ")
	input, err := reader.ReadString('\n')

	if err != nil {
		fmt.Println("Error reading input:", err)
		return ""
	}
	return input
}

func main() {
	fmt.Println("hello world")
	fmt.Println("Would you like to play a game?")
	var name string = readUserInput()
	fmt.Print(name)
}
