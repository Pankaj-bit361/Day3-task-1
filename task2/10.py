# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222
# **Given**:
tuple1 = (11, [22, 33], 44, 55)

# **Expected output:**tuple1 = (11, [222, 33], 44, 55)


for i in tuple1:
    if type(i)==list:
        print
        i[0]=222



print(tuple1)