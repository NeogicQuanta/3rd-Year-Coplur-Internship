items =[]
quantities = []
prices = []
Total =[]
print("\nBilling system\n")
while True:
    print("1. Create Bill\n")
    print("2.Display item price and total bill amount\n")
    print("3.Display Total\n")
    print("4.Exit\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = input("Enter item: ")
        quantity = int(input("Enter quantity: "))
        price = int(input("Enter price: "))
        total = quantity * price
        items.append(item)
        quantities.append(quantity)
        prices.append(price)
        Total.append(total)
        print("Bill created\n")
    elif choice == 2:
        print("Items: ",items)
        print("Quantity: ",quantities)
        print("Price: ",prices)
        print("Total: ",Total)
    elif choice == 3:
        print("Item price:",prices)
        print("Total: ",Total)
    else:
        print("Exit")
        break