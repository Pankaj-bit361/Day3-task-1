# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."

def is_prime(num):
    for i in range(2, int(num) ):
        if num % i == 0:
            return False
    return True


print(is_prime(7))
   