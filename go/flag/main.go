package main

import (
	"flag"
	"fmt"
)

var flagvar int

func init() {
	flag.IntVar(&flagvar, "flagname", 1234, "help message for flagname")
}

func main() {
	var ip = flag.Int("name", 1234, "help message for flagname")

	flag.Parse()

	fmt.Println("ip has value ", *ip)
	fmt.Println("flagvar has ", flagvar)
}
