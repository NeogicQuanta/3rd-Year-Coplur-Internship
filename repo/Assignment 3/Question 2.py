a = int(input("Enter first no\n"))
b = int(input("Enter second no\n"))
def add(x, y):
   result = x + y
   print("Addition of", x, "and", y, "=", result)
   return result

def subtract(x, y):
   result = x - y
   print("Subtraction of", x, "and", y, "=", result)
   return result

def multiply(x, y):
   result = x * y
   print("Multiplication of", x, "and", y, "=", result)
   return result

def divide(x, y):
   if y != 0:
      result = x / y
      print("Division of", x, "and", y, "=", result)
      return result
   else:
      print("Cannot be divided")
      return None

add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)