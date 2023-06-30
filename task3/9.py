# 2. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."



def numb(a,b):
    if a==0 or b==0:
        print("Cannot divide by zero.")
    elif a%b==0:
        print(a/b)
    else:
        print(float(a/b))    



numb(5,0)        