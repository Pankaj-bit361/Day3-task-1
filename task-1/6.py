# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"



a="Hello"
count=0
for i in a:
    if i in "aeiou":
      count+=1

 
print(count)
    
