package main

import "fmt"

func main() {
  m := map[string][]string{
    "abc": {"1","2"},
    "xyz": {"3","4"},
  }
  fmt.Printf("%v\n", m)
}
