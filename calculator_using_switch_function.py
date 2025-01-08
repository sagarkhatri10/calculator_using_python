def sub(num1, num2):
    return num1-num2

def add(num1, num2):
    return num1+num2

def mul(num1,num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

def calculator(num):
    num1 = float(input("Enter a number 1: "))
    num2 = float(input("Enter a number 2: "))
    switch = {
        1:add(num1,num2),
        2:sub(num1,num2),
        3:mul(num1,num2),
        4:div(num1,num2)
    }
    return switch.get(num, 'Invalid Number')

while True:
    print("Enter a number for operation: \n 1 for add \n 2 for sub \n 3 for mul \n 4 for div \n 0 to exit")
    num = int(input("Select operation: "))
    
    if num == 0:
        print("Exiting the calculator.")
        break
    
    print(f"The result is: {calculator(num)} \n \n")