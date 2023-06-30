# 1. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages.
# Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#  - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#  - *Output*: "{}, {'John': 26}, {}"

def diction(inp):
    name="John"
    age=25
    ob={}
    if inp=="Add":
        ob[name]=age
        print(ob)
    elif inp=="Update":
        ob[name]=age+1
        print(ob)
    else:
        if name in ob:
         del ob[name]
        print(ob)
     

diction("Add")
diction("Update")
diction("Delete")

        