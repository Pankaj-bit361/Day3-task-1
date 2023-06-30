### Problem **3: Append new string in the middle of a given string**
# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.
# s1 = "Ault"
# s2 = "Kelly"
# ```
# **Expected Output**:AuKellylt

s1="Ault"
s2="Kelly"
count1=len(s1)/2
count2=0

str=""

for i in s1:
    if count2<count1:
        str+=i;
        count2+=1
    else:
        str=str+s2
        break;


count3=0
for y in s1:
    if count3<count1:
        count3+=1
    else: 
        str=str+y


print(str)