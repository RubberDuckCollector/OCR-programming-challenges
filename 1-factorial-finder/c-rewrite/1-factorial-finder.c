#include <stdio.h>

long fact_it(int n) {
  long result = 1;

  for (long i = 1; i < n + 1; i++) {
    result *= i;
  }
  return result;
}

long fact_rec(int n) {
  if (n < 1) {
    return -1;
  } else if (n == 1) {
    return 1;
  } else {
    return n * fact_rec(n - 1);
  }
}

int main() {
  printf("%ld\n", fact_it(10));
  printf("%ld\n", fact_it(5));

  printf("%ld\n", fact_rec(10));

  return 0;
}
