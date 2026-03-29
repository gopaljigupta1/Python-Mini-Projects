
    
print("welcome to cafe python")
menu = {
     "tea": 20,
     "coffee": 30,
     "milk": 25,
     "soda": 15
     }
print(menu)
def get_order():
     while True:  #infinite loop to keep asking for inputorder = input("do you want to add more items? (yes/no) ")
         order1 = input("what do you like to order? ")
         if order1 in menu:
            print(f"you have ordered {order1}")
            break
         else:
             print("please enter a valid order")
     return order1
             
     
def add_order():
        additional_item=[]
        while True:
            order2 = input("do you want to add more items? (ya/no) ")
            if order2.lower() == "ya":
                new_order = input("what do you like to order? ")
                if new_order in menu:
                    print(f"you have ordered {new_order}")
                    additional_item.append(new_order)
                else:
                    print("please enter a valid order")
            elif order2.lower() == "no":
                break
            else:
                print("please enter ya or no")
        return additional_item
                

def get_amount(total_cost):
     while True:
         amount = input(f"The cost is ${total_cost}. How much do you want to pay? $")
         if amount.isdigit():
             amount = int(amount)
             if amount >= total_cost:
                 print(f"You have paid ${amount}.")
                 if amount > total_cost:
                     print(f"Here is your change: ${amount - total_cost}")
                 break
             else:
                 print(f"Insufficient amount. Please pay at least ${total_cost}.")
         else:
             print("Please enter a valid number.")
     return amount


order1 = get_order()
additional_order = add_order()


total_cost = menu[order1]
for item in additional_order:
    total_cost += menu[item]


get_amount(total_cost)


if additional_order:
    print(f"Your {order1} and {', '.join(additional_order)} are ready.")
else:
    print(f"Your {order1} is ready.")


print("Thank you for your order!")
