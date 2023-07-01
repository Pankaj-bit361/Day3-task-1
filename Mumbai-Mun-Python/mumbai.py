
arr=[]


def Add_sanck():
    name = input("Enter snack name: ")
    Id = input("Enter snack id: ")
    price = int(input("Enter snack price: "))

    obj={
        "Name":name,
        "ID":Id,
        "Price":price
    }

    for i in arr:
        # print(i)
        if i["ID"] == Id:
            print("Id is already exists!!")
            return
    
    
    
    arr.append(obj)
    print("Item added Successfully!!")


def Remove_snack():
    Id = input("Enter snack id: ")

    for i in arr:
        if i["ID"] == Id:
            arr.remove(i)
            print("Item removed Successfully!!")
            return
            # break;
    
    print("Item not found!! ")
    return


    

def Update_snack():
    Id = input("Enter snack id: ")
    New_price = int(input("Enter snack new price: "))
    for i in arr:
        if i["ID"] == Id:
            i["Price"] = New_price
            print("Item Updated Successfully!!")
            return
            # break;
    
    print("Item not found!! ")
    return



def Record_sale():
    print(arr)


while True :
    print("Welcome to Mumbai Munchies!")
    print("Please choose one of the following options:")
    print("1. Add Snack")
    print("2. Remove Snack")
    print("3. Update Snack Availability")
    print("4. Record Sale")
    print("5. Exit")

    choise = int(input("choose you input: "))

    if choise == 1:
        Add_sanck()

    elif choise == 2:
        Remove_snack()
    
    elif choise == 3:
        Update_snack()

    elif choise == 4:
        Record_sale()

    elif choise == 5:
        print("You have successfully quit!! ")
        break;
    else:
        print("Invalid input try again")
        continue