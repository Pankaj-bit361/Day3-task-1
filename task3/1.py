# 1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
#     - *Input*: [("John", 25), ("Jane", 30)]
#     - *Output*: "John is 25 years old. Jane is 30 years old."

a=[("John", 25), ("Jane", 30)]
ok=""
for i in range(len(a)):
    ok+=a[i][0]+" "+"is"+" "+str(a[i][1])+" "+"years"+" "+"old"+". "


print(ok)    