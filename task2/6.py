### Problem **6: Concatenate two lists in the following order**

# ```
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# ```

# **Expected output:** ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list=[]

for i in range(len(list1)):
    for y in range(len(list2)):
     str=list1[i]+" "+list2[y]
     list.append(str)

print(list)