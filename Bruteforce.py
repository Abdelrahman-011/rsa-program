import math
import random
import time


def decrypt(ciphertext, d, n):
    decrypt = pow(ciphertext, d, n)
    return decrypt


e = int(input("Enter a value for e: "))
n = int(input("Enter a value for n: "))

original_message = random.randint(0, 1000)
encrypted_message = pow(original_message, e, n)

start_time = time.time()

found_d_arr = []

d = 1
calculated_message = None

while d <= n:
    d += 1
    calculated_message = decrypt(encrypted_message, d, n)
    if calculated_message == original_message:
        found_d_arr.append(d)


end_time = time.time()
time_taken = (end_time - start_time) * 1000

print("possible d's found", found_d_arr)
print("Time taken to brute force: ", time_taken, " milliseconds")
