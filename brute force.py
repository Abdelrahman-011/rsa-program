import timeit

def calculate_phi(N):
    """
    Calculate Euler's totient function (phi) of N.
    """
    phi = N - 1  # Initialize phi with N - 1
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            while N % i == 0:
                N //= i
            phi -= phi // i
    if N > 1:
        phi -= phi // N
    return phi

def brute_force(N, e):
    """
    Brute force the private exponent d.
    """
    phi = calculate_phi(N)
    start_time = timeit.default_timer()
    for d in range(phi):
        if (e * d) % phi == 1:
            end_time = timeit.default_timer()
            return d, end_time - start_time
    return None, None

def check_d(d, N, e, message):
    """
    Verify if the calculated private exponent (d) is correct.
    """
    encrypted_message = pow(message, e, N)
    decrypted_message = pow(encrypted_message, d, N)
    return decrypted_message == message, None, None  # Return the correctness and placeholder values for time

# Test the functions
N = 204713
e = 65537
message = 12345

d, time_taken = brute_force(N, e)
is_correct, encrypt_time, decrypt_time = check_d(d, N, e, message)
print("Private exponent d is:", d)
print("Is private exponent correct:", is_correct)
print("Total time taken:", time_taken, "seconds")