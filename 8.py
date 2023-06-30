# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."



def main (n):
    y=fun(n)
    print(y)


def fun(n):
    if n==0 or n==1:
     return 1
    else:
     return n*fun(n-1)


main(5)