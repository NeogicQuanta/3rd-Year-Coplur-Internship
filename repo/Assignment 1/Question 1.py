name = input("Enter the name: ")
st_class = int(input("Enter the class: "))
print("Enter 5 subject marks")
Mark1 = int(input("Enter marks for Subject 1: "))
Mark2 = int(input("Enter marks for Subject 2: "))
Mark3 = int(input("Enter marks for Subject 3: "))
Mark4 = int(input("Enter marks for Subject 4: "))
Mark5 = int(input("Enter marks for Subject 5: "))
per = float((Mark1 + Mark2 + Mark3 + Mark4 + Mark5)/5)
print("Name:",name,"\tClass:",st_class,"\tPercentage:",per)
if per>=60:
    print("Grade A")
elif per>=50 and per<60:
    print("Grade B")
elif per>=40 and per<50:
    print("Grade C")
elif per>=33 and per<40:
    print("Grade D")
else:
    print("Fail")