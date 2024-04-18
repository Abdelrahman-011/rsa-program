def brute_force_private_exponent(N, e):
    """Brute force the private exponent d."""
    Euler_totient = N - 1  # Since N = pq, Euler's totient function is N - 1
    d = 1  # Start with a candidate value of 1
    while True:  # Loop continues until correct value of d is found
        if (e * d) % Euler_totient == 1:
            return d
        d += 1  # Try the next value of d

N = 21509
e = 65537
private_exponent = brute_force_private_exponent(N, e)
print("Private exponent d is:", private_exponent)