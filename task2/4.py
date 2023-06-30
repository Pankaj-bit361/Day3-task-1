### Problem **4: Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. 
# Write a program to arrange the characters of a string so that all lowercase letters should come first.

str1 = "PyNaTive"
str2 = ""
for i in range(len(str1)):
    if str1[i].islower():
        str2 += str1[i]


for y in range(len(str1)):
    if str1[y].isupper():
        str2+=str1[y]  

 
print(str2)