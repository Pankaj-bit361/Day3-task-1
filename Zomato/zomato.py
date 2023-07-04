dish=[{"ID":1,"Name":"samosa","Quantity":10,"Price":20},{"ID":2,"Name":"momo","Quantity":5,"Price":10},
      {"ID":3,"Name":"pizza","Quantity":8,"Price":100}]

order=[]

def Add_dish():
    name=(input("Enter Dish Name: "))
    Id=int(input("Enter Dish ID: "))
    price=int(input("Enter Dish Price: "))
    quantity=int(input("Enter Dish Quantity: "))

    ob={
        "ID":Id,
        "Name":name,
        "Price":price,
        "Quantity":quantity

    }



    for i in range(len(dish)):
        if dish[i]["ID"]==Id:
            print()
            print("Dish already exist with this Id")
            print()
            return 


    dish.append(ob)
    print()
    print("Dish Added Successfully !!")



def Show_Menu():
    print()
    print(dish)
    print()

def Remove_dish():
    print("\n")
    Id=int(input("Enter Dish ID: "))

    for i in range(len(dish)):
        if dish[i]["ID"]==Id:
            dish.pop(i)
            print()
            print("Dish Removed Successfully !!")
            print()
            return 
    print()    
    print("Item doesn't exist")  
    print()   

def Update_Availablity():
    Id=int(input("Enter Dish ID: "))
    Inc=int(input("Enter Quantity You want to increase: "))

    for i in range(len(dish)):
        if dish[i]["ID"]==Id:
            dish[i]["Quantity"]=dish[i]["Quantity"]+Inc
    print()
    print("Quantity Increased Successfully")
    print()



         




def New_Order():
    Name=(input("Enter your Name: "))
    Id=int(input("Enter Dish ID: "))
    quantity=int(input("Enter Quantity : "))
  
    ob={
         "Name":Name,
         "ID":Id,
         "status":"pending"
     }
    for i in range(len(dish)):
         if dish[i]["ID"]==Id:
             if dish[i]["Quantity"]>0:
              ob["dish"]=dish[i]["Name"]
              ob["price"]=dish[i]["Price"]*quantity
              dish[i]["Quantity"]=dish[i]["Quantity"]-quantity
        
             else:
                 print()
                 print("Item is out of stock")
                 print()

    order.append(ob) 
    print()  
    print("order done successfully")    
    print() 




def Update_order_status():
     Id=int(input("Enter Dish ID: "))
     
     for i in range(len(order)):
         if order[i]["ID"]==Id:
             order[i]["status"]="recieved"
             print()
             print("order status changed successfully")
             print()
             return 
     print()   
     print("Order with this Id doesn,t exist")
     print()

def Review_Order():
    print(order)

while True:
    print("Welcome to Zesty Zomato")
    print("Choose 1 option out of this")
    print("1. Menu")
    print("2. Add Dish")
    print("3. Remove Dish")
    print("4. Update Availablity") 
    print("5. New Order") 
    print("6. Update order Status")
    print("7, Review all orders")
    print("8. Exit")

    choice = int(input("choose you input: "))

    if choice==1:
        Show_Menu()

    elif choice==2:
        print("\n")
        Add_dish()

    elif choice==3:
        Remove_dish()

    elif choice==4:
        Update_Availablity()

    elif choice==5:
        New_Order()  

    elif choice==6:
        Update_order_status()

    elif choice==7:
        Review_Order()

    elif choice==8:
        print("You have successfully quit!! ")
        break;
    else:
        print("Invalid Input")
        continue
