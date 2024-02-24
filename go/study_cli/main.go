package main

import (
	"fmt"
	"log"
	"os"

	"github.com/urfave/cli"
)

func main() {
	app := cli.NewApp()
	app.Name = "hooooge"
	app.Usage = "便利なツールの練習"
	app.Action = func(c cli.Context) error {
		fmt.Println("boom i say")
		return nil
	}
	err := cli.NewApp().Run(os.Args)
	if err != nil {
		log.Fatal(err)
	}
}
