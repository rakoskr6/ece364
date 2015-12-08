#include <stdio.h>
#define N 10
unsigned long fib(unsigned long n) {
  if(n <= 0)
    return 0;

  if(n == 1)
    return 1;

  if(n == 2)
    return 1;

  return fib(n-2)+fib(n-1);
}

int main(int argc, char **argv) {
  unsigned long i = 0;
  for(i = 0; i < N; i++) {
    printf("fib(%lu) = %lu\n", i, fib(i));
  }

  return 0;
}
