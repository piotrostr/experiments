package main

import (
	"fmt"
	"runtime"
)

func main() {
	buf := make([]byte, 1<<16)
	all := true

	length := runtime.Stack(buf, all)
	fmt.Println(string(buf[:length]))
}
