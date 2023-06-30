# 1. **Selection Sort**: Implement the selection sort algorithm in Python.
    # - *Input*: [64, 25, 12, 22, 11]
    # - *Output*: "[11, 12, 22, 25, 64]"

a=[64, 25, 12, 22, 11]
for i in range(len(a)):
    Index=i
    for j in range(i+1,len(a)):
        if a[j]<a[Index]:
            Index=j

       
    temp=a[Index]
    a[Index]=a[i]
    a[i]=temp    



print(a)    