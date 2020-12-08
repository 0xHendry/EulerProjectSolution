
count_of_numbers = 19
prime_rule = count_of_numbers - 9
number_NOD = count_of_numbers
n = count_of_numbers - 1

while n <= count_of_numbers:
    if number_NOD % n != 0:
        number_NOD = number_NOD * n
    else:
        if number_NOD % n == 0 and n > prime_rule:
            number_NOD = number_NOD // n
    n -= 1
    if n == 0:
        break

print(number_NOD)

# For beauty solution we can use gcd from math
"""
import math
gcd_prime = 1
for i in range(1, 21):
    gcd_prime *= i // math.gcd(i, gcd_prime)
print(gcd_prime)
    """