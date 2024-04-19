import timeit


def brute_force(N, e, message, cypher):
  phi = N - 1
  for d in range(phi):
    if check_d(N, e, d, message, cypher):
      return d, True
  return None, False


def check_d(N, e, d, message, cypher):
  plain = pow(cypher, d, N)
  return message == plain


N = 1000
e = 3
message = 7
cypher = pow(message, e, N)
start_time = timeit.default_timer()
d, is_correct = brute_force(N, e, message, cypher)
end_time = timeit.default_timer()
execution_time = (end_time - start_time) 
print("The Execution time of the code is:", execution_time, "seconds")
print("Private exponent d is:", d)
print("Is private exponent correct:", is_correct)