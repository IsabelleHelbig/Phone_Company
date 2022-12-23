total = 0
print("Welcome to Circle Phones' Profit calculator.")
product_number = int(input("Enter product number 1-5, or enter 0 to stop: "))
while product_number:
    if 1<= product_number <=5:
        quantity = int(input("Enter quantity sold: "))   
        if product_number == 1:
            total += 120.45*quantity  
        elif product_number == 2:
            total += 99.50*quantity
        elif product_number == 3:
            total += 75.69*quantity
        elif product_number == 4:
            total += 65.73*quantity
        elif product_number == 5:
            total += 51.49*quantity
        product_number = int(input("Enter product number 1-5, or enter 0 to stop: "))
    else:
        print("Error. Invalid value entered. Please try again.")
        product_number = int(input("Enter product number 1-5, or enter 0 to stop: "))
if product_number == 0:
    print("Your total profit for today is:", total)
        
