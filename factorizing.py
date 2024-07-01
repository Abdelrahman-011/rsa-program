import random
import time

def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    def miller_rabin_test(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False

    for _ in range(k):
        a = random.randrange(2, n - 1)
        if not miller_rabin_test(a):
            return False

    return True

def find_prime_factors(n):
    for i in range(2, n):
        if n % i == 0 and is_prime(i):
            return i, n // i
    return None, None

def calculate_private_key(e, phi_n):
    return pow(e, -1, phi_n)


e = int(input("Enter e: "))
n = int(input("Enter n: "))

start_time = time.time()

p, q = find_prime_factors(n)
if p is None or q is None:
    print("Failed to find prime factors.")

phi_n = (p - 1) * (q - 1)
d = calculate_private_key(e, phi_n)

end_time = time.time()
time_taken = (end_time - start_time) * 1000

print("Private exponent d:", d)
print("Time taken:", time_taken, "milliseconds")
