"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("number_of_primes must be greater than 0")
    else:
        prime_numbers = []
        last_prime = 0
        for i in range(1, number_of_primes + 1):
            last_prime = next_prime_after(last_prime)
            prime_numbers.append(last_prime)
        return prime_numbers


def next_prime_after(number):
    while True:
        number += 1
        if is_prime(number):
            return number


def is_prime(number):
    if number <= 1:
        return False
    else:
        for i in range(2, int(number / 2 + 1)):
            if number % i == 0:
                return False
        return True
