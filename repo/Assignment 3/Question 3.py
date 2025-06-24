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
else:
      print("\n It is not a palindrome no.")