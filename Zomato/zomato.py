dish=[{"ID":1,"Name":"samosa","Quantity":10,"Price":20},{"ID":2,"Name":"momo","Quantity":5,"Price":10},
      {"ID":3,"Name":"pizza","Quantity":8,"Price":100}]

order=[]

import tkinter as tk
from tkinter import messagebox

def show_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title("Menu")
    
    # Create a text widget to display the menu
    menu_text = tk.Text(menu_window)
    menu_text.pack()
    
    # Insert menu items into the text widget
    for item in dish:
        menu_text.insert(tk.END, f"ID: {item['ID']} - Name: {item['Name']} - Quantity: {item['Quantity']} - Price: {item['Price']}\n")
    
    # Disable text widget editing
    menu_text.config(state=tk.DISABLED)

def add_dish():
    add_window = tk.Toplevel(root)
    add_window.title("Add Dish")
    
    # Create labels and entry fields for dish details
    name_label = tk.Label(add_window, text="Dish Name:")
    name_label.pack()
    name_entry = tk.Entry(add_window)
    name_entry.pack()
    
    id_label = tk.Label(add_window, text="Dish ID:")
    id_label.pack()
    id_entry = tk.Entry(add_window)
    id_entry.pack()
    
    price_label = tk.Label(add_window, text="Dish Price:")
    price_label.pack()
    price_entry = tk.Entry(add_window)
    price_entry.pack()
    
    quantity_label = tk.Label(add_window, text="Dish Quantity:")
    quantity_label.pack()
    quantity_entry = tk.Entry(add_window)
    quantity_entry.pack()
    
    def add_dish_button():
        name = name_entry.get()
        Id = int(id_entry.get())
        price = int(price_entry.get())
        quantity = int(quantity_entry.get())

        ob = {
            "ID": Id,
            "Name": name,
            "Price": price,
            "Quantity": quantity
        }

        for item in dish:
            if item["ID"] == Id:
                messagebox.showinfo("Error", "Dish already exists with this ID")
                add_window.destroy()
                return

        dish.append(ob)
        messagebox.showinfo("Success", "Dish added successfully")
        add_window.destroy()

    # Create a button to add the dish
    add_button = tk.Button(add_window, text="Add Dish", command=add_dish_button)
    add_button.pack()

def remove_dish():
    remove_window = tk.Toplevel(root)
    remove_window.title("Remove Dish")
    
    # Create a label and entry field for the dish ID
    id_label = tk.Label(remove_window, text="Dish ID:")
    id_label.pack()
    id_entry = tk.Entry(remove_window)
    id_entry.pack()
    
    def remove_dish_button():
        Id = int(id_entry.get())

        for i, item in enumerate(dish):
            if item["ID"] == Id:
                dish.pop(i)
                messagebox.showinfo("Success", "Dish removed successfully")
                remove_window.destroy()
                return

        messagebox.showinfo("Error", "Item doesn't exist")
        remove_window.destroy()

    # Create a button to remove the dish
    remove_button = tk.Button(remove_window, text="Remove Dish", command=remove_dish_button)
    remove_button.pack()

def update_availability():
    update_window = tk.Toplevel(root)
    update_window.title("Update Availability")
    
    # Create labels and entry fields for dish ID and quantity
    id_label = tk.Label(update_window, text="Dish ID:")
    id_label.pack()
    id_entry = tk.Entry(update_window)
    id_entry.pack()
    
    inc_label = tk.Label(update_window, text="Quantity to Increase:")
    inc_label.pack()
    inc_entry = tk.Entry(update_window)
    inc_entry.pack()
    
    def update_availability_button():
        Id = int(id_entry.get())
        inc = int(inc_entry.get())

        for item in dish:
            if item["ID"] == Id:
                item["Quantity"] += inc
                messagebox.showinfo("Success", "Quantity increased successfully")
                update_window.destroy()
                return

        messagebox.showinfo("Error", "Item doesn't exist")
        update_window.destroy()

    # Create a button to update the availability
    update_button = tk.Button(update_window, text="Update Availability", command=update_availability_button)
    update_button.pack()

def new_order():
    order_window = tk.Toplevel(root)
    order_window.title("New Order")
    
    # Create labels and entry fields for customer name, dish ID, and quantity
    name_label = tk.Label(order_window, text="Customer Name:")
    name_label.pack()
    name_entry = tk.Entry(order_window)
    name_entry.pack()
    
    id_label = tk.Label(order_window, text="Dish ID:")
    id_label.pack()
    id_entry = tk.Entry(order_window)
    id_entry.pack()
    
    quantity_label = tk.Label(order_window, text="Quantity:")
    quantity_label.pack()
    quantity_entry = tk.Entry(order_window)
    quantity_entry.pack()
    
    def new_order_button():
        name = name_entry.get()
        Id = int(id_entry.get())
        quantity = int(quantity_entry.get())

        ob = {
            "Name": name,
            "ID": Id,
            "status": "pending"
        }

        for item in dish:
            if item["ID"] == Id:
                if item["Quantity"] > 0:
                    ob["dish"] = item["Name"]
                    ob["price"] = item["Price"] * quantity
                    item["Quantity"] -= quantity
                else:
                    messagebox.showinfo("Error", "Item is out of stock")
                    order_window.destroy()
                    return

        order.append(ob)
        messagebox.showinfo("Success", "Order placed successfully")
        order_window.destroy()

    # Create a button to place the order
    order_button = tk.Button(order_window, text="Place Order", command=new_order_button)
    order_button.pack()

def update_order_status():
    status_window = tk.Toplevel(root)
    status_window.title("Update Order Status")
    
    # Create a label and entry field for the dish ID
    id_label = tk.Label(status_window, text="Dish ID:")
    id_label.pack()
    id_entry = tk.Entry(status_window)
    id_entry.pack()
    
    def update_order_status_button():
        Id = int(id_entry.get())

        for item in order:
            if item["ID"] == Id:
                item["status"] = "received"
                messagebox.showinfo("Success", "Order status changed successfully")
                status_window.destroy()
                return

        messagebox.showinfo("Error", "Order with this ID doesn't exist")
        status_window.destroy()

    # Create a button to update the order status
    status_button = tk.Button(status_window, text="Update Status", command=update_order_status_button)
    status_button.pack()

def review_order():
    review_window = tk.Toplevel(root)
    review_window.title("Review Orders")
    
    # Create a text widget to display the orders
    review_text = tk.Text(review_window)
    review_text.pack()
    
    # Insert orders into the text widget
    for item in order:
        review_text.insert(tk.END, f"Name: {item['Name']} - Dish: {item['dish']} - Price: {item['price']} - Status: {item['status']}\n")
    
    # Disable text widget editing
    review_text.config(state=tk.DISABLED)

# Create the main application window
root = tk.Tk()
root.title("Zesty Zomato")

# Create buttons for each option
menu_button = tk.Button(root, text="Menu", command=show_menu)
menu_button.pack()

add_button = tk.Button(root, text="Add Dish", command=add_dish)
add_button.pack()

remove_button = tk.Button(root, text="Remove Dish", command=remove_dish)
remove_button.pack()

availability_button = tk.Button(root, text="Update Availability", command=update_availability)
availability_button.pack()

order_button = tk.Button(root, text="New Order", command=new_order)
order_button.pack()

status_button = tk.Button(root, text="Update Order Status", command=update_order_status)
status_button.pack()

review_button = tk.Button(root, text="Review All Orders", command=review_order)
review_button.pack()

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack()

# Start the main event loop
root.mainloop()
