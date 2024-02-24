package main

import (
	"os"
	"os/exec"
)

func command(command string) {
	cmd := exec.Command("sh", "-c", command)

	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	cmd.Stdin = os.Stdin

	cmd.Run()
}

func main() {
	command("ls -la")
}
