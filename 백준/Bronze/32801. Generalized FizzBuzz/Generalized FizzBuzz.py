import sys
import math

n, a, b = map(int, sys.stdin.readline().split())

lcm_ab = (a * b) // math.gcd(a, b)

fizzbuzz_count = n // lcm_ab
fizz_count = (n // a) - fizzbuzz_count
buzz_count = (n // b) - fizzbuzz_count

print(fizz_count, buzz_count, fizzbuzz_count)