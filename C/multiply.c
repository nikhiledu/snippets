#include <stdio.h>
#include <stdlib.h>

int multiply(int a, char *b) {
  return a * (int) strtol(b, &b, 10);
}

int main() {
  int a = 5;
  char *b = "3";

  printf("%d\n", multiply(a, b));
}
