from flask import Flask,request,jsonify
import pickle


app=Flask(__name__)

dish=[{"id":1,"dish":"burger","quantity":10,"price":30}]
order=[]



with open("data.pkl", "wb") as file:
    pickle.dump(dish, file)

# Load data using Pickle
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)

# Print the loaded data
print(loaded_data)



@app.route("/")
def welcome():
    return "Welcome to home page"

@app.route("/addDish", methods=["POST"])
def adddish():
    if request.method == 'POST':
        data = request.get_json()  
        dish.append(data)  
        return jsonify(data)

@app.route("/menu",methods=["GET"])
def showmenu():
 if request.method=="GET":
  return jsonify(dish) 



      
@app.route("/delete/<int:Id>", methods=["DELETE"])
def deleteDish(Id):
    print("Requested id:", Id)
    if request.method == "DELETE":
        for i in range(len(dish)):
            print("Current dish id:", dish[i]["id"])
            if dish[i]["id"] == Id: 
                dish.pop(i)
                return jsonify("Dish has been removed successfully")
        
        return jsonify("Dish not found") 

@app.route("/updateDish/<int:Id>",methods=["PATCH"])
def updateDish(Id):
   if request.method == "PATCH":
        for i in range(len(dish)):
          if dish[i]["id"] ==Id:
            data = request.get_json()  
            print(data)
            dish[i]["quantity"]=data["quantity"]
            return jsonify("successfully update the quantity")
         
        return jsonify("Id not Found") 


@app.route("/order",methods=["POST"])
def oderDish():
   if request.method == "POST":
      data=request.get_json()
      for i in range(len(dish)):
       if dish[i]["id"] ==data["id"]:
          dish[i]["quantity"]=dish[i]["quantity"]-data["quantity"]
          data["dish"]=dish[i]["dish"]
          data["price"]=dish[i]["price"]*data["quantity"]
          data["status"]="recieved"
          order.append(data)
          return jsonify("Order Created Successfully")
       return jsonify("ID not found")

@app.route("/allorder",methods=["GET"])
def getOrder():
   return jsonify(order)



@app.route("/updateOrder/<name>",methods=["PATCH"])
def UpdateOrder(name):
   for i in range(len(order)):
      if order[i]["name"]==name:
         if order[i]["status"]=="recieved":
            order[i]["status"]="preparing"
            print("Order Status changed successfully !!")
            return  jsonify("Order Status changed successfully !!")
         elif(order[i]["status"]=="preparing"):
            order[i]["status"]="ready for pickup"
            print("Order Status changed successfully !!")
            return  jsonify("Order Status changed successfully !!")
         elif(order[i]["status"]=="ready for pickup"):
            order[i]["status"]="delivered"
            return  jsonify("Order Status changed successfully !!")
         elif (order[i]["status"]=="delivered"):
            return 
            
           
            
   return jsonify("Order With this name doesn't Exist")
   
if __name__ == '__main__':
    app.run()

 

