sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

ob={}

for i in keys:
    for key in sample_dict:
        if i == key:
            ob[key]=sample_dict[key]


print(ob)