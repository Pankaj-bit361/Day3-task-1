# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"


a=[2, 7, 11, 15]
k=13

for i in range(len(a)):
    for j in range (i+1,len(a)):
        if a[i]+a[j]==k:
            print([i,j])


