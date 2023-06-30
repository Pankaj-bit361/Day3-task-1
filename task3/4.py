# 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."

def checkpal(str):
  str2=""
  for i in range(len(str)):
    str2+=str[-(i+1)]
  if str==str2:
      print("The word "+str+" is a palindrome.")
  else:
     print("The word "+str+" is not a palindrome.")



   
         



checkpal("madam")