# 10. **List Comprehension**: Use list comprehension to create a list of the squares of the numbers from 1 to 10.
#     - *Input*: None
#     - *Output*: "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"


def square(n):
    list=[]
    for i in range(n+1):
        list.append(i**2)
   
   
    return list



b=square(10)

print(b)