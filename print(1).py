'''
a =10
b=20

choice = int(input("1.Add \n2. Sub\n3. Div\n4.Mul\n\n \tEnter your Choice:"))
match choice:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case _:
        print("Invalid Choice")
        
print("Is Even") if a%2==0 else print("Is Odd")
print(str[0:5])
print(str[5:10])

for i in range(1, 11):
    pass
    print(i, "X", 5, "=", i * 5)



l =[]
print(l)
l.append(1)
l.append(2)
l.append([3, 4, 5])
l.extend([6, 7, 8])
print(l)


d = {'name': 'Eshan', 'age': 20, 'city': 'Jaipur'}
d2 = {'brand': 'Toyota', 'model': 'Corolla', 'year': 2022}
print(d.update(d2))
print(d)
l= [1, 2, 3, 4, 5]
print (l[:0:-1])

t = (1, 2, 3, 4, 5)
print(t)

t1 = list(t)

print( t[2:60] )

s ={"a", "b", "c", "d", "e"}
print(s)

'''

# This code is a simple calculator that performs basic arithmetic operations
def calculator():
    a = 10
    b = 20

    choice = int(input("1.Add \n2.Subtract\n3.Divide\n4.Multiply\n\n\tEnter your Choice: "))
    match choice:
        case 1:
            print(f"Result: {a + b}")
        case 2:
            print(f"Result: {a - b}")
        case 3:
            print(f"Result: {a / b}")
        case 4:
            print(f"Result: {a * b}")
        case _:
            print("Invalid Choice")

    print("Is Even") if a % 2 == 0 else print("Is Odd")


