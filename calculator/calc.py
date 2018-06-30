def addition(num1,num2):
    return num1 + num2

def substraction(num1,num2):
    return num1 - num2

def multiplication(num1,num2):
    return num1 * num2

def division(num1,num2):
    return num1 / num2

print("select operation")
print("1.add")
print("2.substraction")
print("3.multiplication")
print("4.division")

count = input("Enter choice(1/2/3/4): ")

num1 = int(input("Enter any number 1: "))
num2 = int(input("Enter any number 2: "))

if count == '1':
    print(num1,"+",num2,"=",addition(num1,num2))

elif count == '2':
    print(num1,"-",num2,"=",substraction(num1,num2))

elif count == '3':
    print(num1,"*",num2,"=",multiplication(num1,num2))

elif count == '4':
    print(num1,"/",num2,"=",division(num1,num2))

else: 
   print("invalid key")    


