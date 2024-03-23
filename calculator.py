num1 = input("Enter 1st Number: ")
num2 = input("Enter 2nd Number: ")

op = input("Which Opertation You want to Perform: ")

if op == "+":
    print("Sum is:", int(num1)+int(num2))
elif op == "-":
    print("Subtract is:", int(num1)-int(num2))
elif op == "*":
    print("Product is:", int(num1)*int(num2))
elif op == "/":
    print("Sum is", int(num1)/int(num2))
else:
    print("Wrong Operation") 