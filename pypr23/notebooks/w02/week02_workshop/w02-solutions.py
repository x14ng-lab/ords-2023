# Task 1

p = 1
q = 1
fibo = [1, 1]

#  # Using positive indexing
#  fibo.append(p*fibo[1] + q*fibo[0])
#  fibo.append(p*fibo[2] + q*fibo[1])
#  print(fibo)

# Using negative indexing (better -- it never changes!)
fibo.append(p*fibo[-1] + q*fibo[-2])
fibo.append(p*fibo[-1] + q*fibo[-2])
print(fibo)


# Task 3: (P, Q)-Fibonacci sequence with loop and function

def pq_fibo(p, q, n):
    '''
    Returns a list containing the first n elements
    of the (P, Q)-Fibonacci sequence.
    '''
    seq = [1, 1]
    for i in range(2, n):
        seq.append(p * seq[-1] + q * seq[-2])
    return seq

print(pq_fibo(6, 4, 10))
