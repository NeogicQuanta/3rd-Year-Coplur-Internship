#ques3
from random import choice

print("Enter a number: ")
a = int(input())
f=1
for i in range(1,a+1):
     f *= i

print("Factorial is: ",f)
#ques4
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
#ques 5
list1 = [10,2,8,17,23]
smallest = min(list1)
print("Smallest no in list: ",smallest)
first = list1[0]
sec = list1[0]
for i in range(len(list1)):
    if list1[i]>first:
        sec = first
        first = list1[i]
    elif first > list1[i] > sec:
        sec = list1[i]
print("\nSecond greatest no in list: ",sec)
first = list1[0]
sec = list1[0]
for i in range(len(list1)):
    if list1[i]< first:
        sec = first
        first = list1[i]
    elif first<list1[i]<sec:
         sec = list1[i]
print("\n Second smallest: ",sec)

