package main

import (
	"fmt"
	"os/exec"
	"log"
)

// exec command

func main() {
	cmd := exec.Command("ls", "-la")
	stdoutStdErr, err := cmd.CombinedOutput()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s", stdoutStdErr)
}
