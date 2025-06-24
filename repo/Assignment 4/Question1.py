import csv
data = [["Name","Address","Mobile","Email"],
        ["Mahendra","Racecourse, Ranchi","1234567890","msd@yahoo.com"],
        ["Sachin","Tourist Road, Una","9876543210","sachin@hotmail.com"],
        ["Suresh","Sports Complex, Chennai","5555555555","suresh@gmail.com"]]

with open ("address_book.csv","w",newline="") as file:
    writer = csv.writer(file)
    for i in data:
        writer.writerow(i)

with open("address_book.csv","r") as file:
    reader = csv.reader(file)
    for i in reader:
        print(f"The Name is {i[0]}, Address is {i[1]}, Mobile is {i[2]}, Email is {i[3]}")

