def larger_num(num1, num2):
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1 > num1:
        print (f"{num2} is greater than {num1}")
    else:
        print (f"{num1 and num2} are equal")
    
num1 = int(input("enter a num1: "))
num2 = int(input("enter a num2: "))
larger_num(num1, num2)
    
