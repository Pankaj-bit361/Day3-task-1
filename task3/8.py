# 1. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"



def txtfile(inp):
    output=""
    count=1
    for i in range(len(inp)):
        if inp[i]==" ":
            count+=1

    print("Number of words: "+str(count))       




txtfile("Hello world")   