# Vending Machine items and prices

products = {
        '1': {"product_name": "Coca-Cola", "price": 20, "quantity": 10},
        '2': {"product_name": "Pepsi", "price": 20, "quantity": 8},
        '3': {"product_name": "Water Bottle", "price": 12, "quantity": 15},
        '4': {"product_name": "Lays Chips", "price": 10, "quantity": 12},
        '5': {"product_name": "Doritos", "price": 15, "quantity": 10},
        '6': {"product_name": "Trail Mix", "price": 1.75, "quantity": 7},
        '7': {"product_name": "Munch", "price": 10, "quantity": 14},
        '8': {"product_name": "KitKat", "price": 10, "quantity": 10},
        '9': {"product_name": "M&Ms", "price": 25, "quantity": 9},
        '10': {"product_name": "Red Bull", "price": 25, "quantity": 5},
        '11': {"product_name": "Monster", "price": 20, "quantity": 4},
        '12': {"product_name": "Granola Bar", "price": 30, "quantity": 6},
        '13': {"product_name": "Protein Bar", "price": 50, "quantity": 5}
    }

# This function is used to display products

def display():

    try:
    
        # Display available items and prices
        print("Welcome to the Vending Machine!\n")
        print("Please select an product:\n")
        
        for key, product in products.items():

            print(f"{key}.{product["product_name"]} - ₹{product["price"]} - Qty{product["quantity"]}")
            
        selection()    
        
    except Exception as e:
        print("Error in display function",e)

# Taking inputs from user

def selection():
    try:
        print()
        select = input("Enter item number you want to purchase : \n").strip()
        quantity = input("Enter quantity : \n").strip()
        
               
        if select in products and quantity in products:
            
            selected_item = products[select]
            
            selected_quantity = products[quantity]
           
            print(f"Selected item is - {selected_item["product_name"]} and Quantity is - {quantity} ")
            
            amount = selected_item["price"]

            
            if int(quantity) <= selected_item["quantity"]:
                selected_item["quantity"] -= int(quantity)

            
             # total = amount * int(quantity)
             # amount = total
                
             #    print(f"Total amount to pay: ₹{total}\n")
                
             #    while total > 0:
             #        try:
             #            payment = int(input(f"Enter amount ₹{total} \n"))
             #            if payment >= total:
             #                change = payment - total
             #                print(f"Thank you for your purchase your change is : ₹{change}\n")
                            
             #                add_item(selected_item["product_name"],int(quantity),amount)
             #                re_selection()
             #                break
             #            else:
             #                print(f"Insufficient payment. You still owe ₹{total - payment} \n")
             #                total -= payment
                            
             #        except ValueError:
             #            print("Invalid payment amount. Please enter a valid number.\n")
            
            else:
               print("Not enough stock available.\n")
            add_item(selected_item["product_name"],amount,int(quantity))
            re_selection()
        else:
            print("Selction cannot be zero, character or special symbol \n")
            display()
            
    except Exception as e:
        print("Error in Selection Function Selction cannot be zero or character\n",e)


# This function is used to buy product again

def re_selection():
    try:
        re_call = int(input("Do you want to purchase another product\n"
                        "Press '1' to Continue buying\n"
                        "Press '2' to proceed with cart\n"))
        
        if re_call == 1:
            print()
            display()
            
        elif re_call == 2:
            view_cart()
            
        else:
            print("Invalid input\n")
            re_selection()
            
    except ValueError as e:
          print("Input cannot be Number",e)



cart = []

def add_item(name, price, quantity=1):
    try:
        item = {"name": name, "price": price, "quantity": quantity}
        cart.append(item)
        print(f"{quantity} x {name} added to cart.")
        print(cart)
    except Exception as e:
        print("ERROR in view_cart function",e)
    
def view_cart():
    try:
        if not cart:
            print("Your cart is empty.")
            return
        print("--- Your Shopping Cart ---")
        total = 0
        for i, item in enumerate (cart,start=1):
            item_total = item["price"] * item["quantity"]
            print(f"{i}. {item['name']} (x{item['quantity']}) - ₹{item['price']} each | Total: ${item_total}")
            total += item_total

        print(f"Total amount to pay: ₹{total}\n")

        # if int(quantity) <= selected_item["quantity"]:
        #     selected_item["quantity"] -= int(quantity)
            
        #     total = amount * int(quantity)
        #     amount = total
                
        #     print(f"Total amount to pay: ₹{total}\n")
        
        while total > 0:
            try:
                payment = int(input(f"Enter amount ₹{total} \n"))
                if payment >= total:
                    change = payment - total
                    print(f"Thank you for your purchase your change is : ₹{change}\n")
                    
                    # add_item(name, price, quantity=1)
                    # re_selection()
                    break
                else:
                    print(f"Insufficient payment. You still owe ₹{total - payment} \n")
                    total -= payment
                    
            except ValueError:
                print("Invalid payment amount. Please enter a valid number.\n")
            
        print(f"--------------------------")
        print(f"Total Cart Value: ${total}")
    
    except Exception as e:
        print("ERROR in view_cart function",e)

def remove_item(item_index):
    if 1 == item_index < len(cart):
        removed_item = cart.pop(item_index)
        print(f"{removed_item['name']} removed from cart.")
    else:
        print("Invalid item number.")

display()
    