import timeit

def check_prime(n):
    if n <= 1:  # Check for non-prime cases: 1 or negative numbers
        return False
    for i in range(2, int(n**0.5) + 1):  # Check divisibility only up to the square root of n
        if n % i == 0:
            return False
    else:  # If loop finishes without finding a divisor, n is prime
        return True


def prime_factors(N, e):
    """Factor the modulus to obtain prime factors and calculate the private exponent."""
    # Trial division to find prime factors p and q
    p, q = None, None
    for i in range(2, N):
        if N % i == 0 and check_prime(i):
            p = i
            q = N // i
            d = calculate_d_value(p, q, e)
            break
    else:
        raise ValueError("Failed to factorize modulus N")
        
    is_d_correct = check_private_exponent(N, e, d)
    return p, q, d, is_d_correct


def extended_Euclidean(a, b):
    """Extended Euclidean algorithm."""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_Euclidean(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def calculate_d_value(p, q, e):
    """Calculate the private exponent d using the extended Euclidean algorithm."""
    Euler_totient = (p - 1) * (q - 1)
    _, d, _ = extended_Euclidean(e, Euler_totient)
    d = d % Euler_totient
    if d < 0:
        d += Euler_totient
    return d


def check_private_exponent(N, e, d):
    """Check if the private exponent is correct by encrypting and decrypting a test message."""
    test_message = 112233
    encrypted_message = pow(test_message, e, N)
    decrypted_message = pow(encrypted_message, d, N)
    return decrypted_message == test_message


N = 204713
e = 65537
start_time = timeit.default_timer()
p, q, d, is_d_correct = prime_factors(N, e)
end_time = timeit.default_timer()
execution_time = (end_time - start_time) 

print("Prime factor p of modulus N is:", p)
print("Prime factor q of modulus N is:", q)
print("Private exponent d is:", d)
print("The Execution time of the code is:", execution_time, "seconds")
print("Is private exponent correct:", is_d_correct)