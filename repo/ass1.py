#ques1
name = input("Enter the name\n")
st_class = int(input("Enter the class\n"))
print("Enter 5 subject marks")
Mark1 = int(input())
Mark2 = int(input())
Mark3 = int(input())
Mark4 = int(input())
Mark5 = int(input())
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
#ques2
str1 = input("Enter string 1\n")
str2 = input("Enter string 2\n")
a = str1+str2
print(a.upper())
print(a.lower())
print(a.startswith("hel"))
print(str1.join(str2))
b = "name\nclass\nmarks"
print(b.splitlines())
print(a.maketrans(str1,str2))