def check_prime(n):
  if n <= 1:# Check for non-prime cases: 1 or negative numbers
    return False
  for i in range(2, int(n**0.5) + 1):# Check divisibility only up to the square root of n
    if n % i == 0:
      return False
  else:# If loop finishes without finding a divisor, n is prime
    return True


def prime_factors(N, e):
    """Factor the modulus to obtain prime factors and calculate the private exponent."""
    
    # Trial division to find prime factors p and q
    p, q = None, None
    for i in range(2, N):
        if N % i == 0 and check_prime(i):
            p = i
            q = N // i
            break
    if p is None or q is None:
        raise ValueError("Failed to factorize modulus N")

    # Calculate private exponent d
    d = calculate_d_value(p, q, e)
    
    return p, q, d
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

N = 21509
e = 65537
p, q, d = prime_factors(N, e)
print("Prime factor p of modulus N is:", p)
print("Prime factor q of modulus N is:", q)
print("Private exponent d is:", d)