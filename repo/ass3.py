#ques2
a = int(input("Enter first no\n"))
b = int(input("Enter second no\n"))
print("Addition of",a,"and",b,"=",a+b)
print("Subtraction of",a,"and",b,"=",a-b)
print("Multiplication of",a,"and",b,"=",a*b)
if b>0:
   print("Division of",a,"and",b,"=",a/b)
else:
    print("Cannot be divided")

#ques3
n = int(input("\nEnter a no. "))
t = n
s=0
while n>0:
      r = n%10
      s = s*10 + r
      n = n//10
print("Reversed no is: ",s)
if(s == t):
    print("\n It is a palindrome no.")


