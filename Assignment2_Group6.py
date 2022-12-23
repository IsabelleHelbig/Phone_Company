#This is Assignment 2-Programming Strategies.
#Khang Trinh, Isabelle Helbig, Liam Marrie
#Oct 28,2022.
#Circle Phones is an online retail business specializing in cell phones and tablets.
#The owner initially hired us to create an application to calculate Circle Phones’ profits.
#This program was made to calculate their profits.

#variable lists
condition_a= True
week =["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
product_dictionaries={1:120.45,2:99.50,3:75.69,4:65.73,5:51.49}
profit=[]

print("Welcome to Circle Phones' Profit Calculator.")

while True:

    #entrance message
    print('\nYou can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend.')
    print('Enter:\n\t1 - For specific Day\n'.expandtabs(3),'\t2 - For the Week\n'.expandtabs(2),'\t3 - For Week Business Days\n'.expandtabs(2),'\t4 - For Weekend Days\n'.expandtabs(2),'\t0 - Exit'.expandtabs(2))

    #checking if input is valid
    input_type= input()
    while input_type != "1" and input_type != "2" and input_type != "3" and input_type != "4" and input_type != "0":
        print("Did not enter a  valid period of time. Please try again.")
        print("Enter:")
        print("\t1 - For specific Day\n".expandtabs(3),"\t2 - For the Week\n".expandtabs(2),"\t3 - For Week Business Days\n".expandtabs(2),"\t4 - For Weekend Days\n".expandtabs(2),"\t0 - Exit".expandtabs(2))
        input_type = input()
    input_type = int(input_type)

    match input_type:
        case 1:
            day = input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: ")
            day = day.capitalize()
            while day != "Monday" and day != "Tuesday" and day != "Wednesday" and day != "Thursday" and day != "Friday" and day != "Saturday" and day != "Sunday":
                print("Did not enter a valid day. Please try again.")
                day = input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: ")
                day = day.capitalize()
            print("For", day)
            while condition_a == True:
                a=input('Enter product number 1-5, or enter 0 to stop: ')
                while a != "0" and a != "1" and a != "2" and a != "3" and a != "4" and a != "5":
                    print("Error. Invalid value entered. Please try again.")
                    a = input("Enter product number 1-5, or enter 0 to stop: ")
                a = int(a)
                if a == 0:
                    break
                else:
                    quantity = input("Enter quantity sold: ")
                    while quantity.isdigit() == False:
                        print("Error. Invalid value entered. Please try again.")
                        quantity = input("Enter quantity sold: ")
                    quantity = int(quantity)
                    profit_per_product = product_dictionaries.get(a)
                    total_profit = profit_per_product*quantity
                    profit.append(total_profit)
            total_profit = sum(profit)
            print(f"Total Profit for the {day} is: ${total_profit:.2f}")     
            if total_profit <= 10000:
                print("We didn't reach our goal for this period. More work is needed.")
            else:
                print("You did well this period! Keep up the great work!")
            profit.clear()
            
    match input_type:
        case 2:
            for weekday in week:
                print (f"For {weekday}")
                while condition_a == True:
                    a=input('Enter product number 1-5, or enter 0 to stop: ')
                    while a != "0" and a != "1" and a != "2" and a != "3" and a != "4" and a != "5":
                        print("Error. Invalid value entered. Please try again.")
                        a = input("Enter product number 1-5, or enter 0 to stop: ")
                    a = int(a)
                    if a == 0:
                        break
                    else:
                        quantity = input("Enter quantity sold: ")
                        while quantity.isdigit() == False:
                            print("Error. Invalid value entered. Please try again.")
                            quantity = input("Enter quantity sold: ")
                        quantity = int(quantity)
                        profit_per_product = product_dictionaries.get(a)
                        total_profit = profit_per_product*quantity
                        profit.append(total_profit)
            total_profit = sum(profit)
            print(f"Total Profit for the week is: ${total_profit:.2f}")
            if total_profit <= 10000:
                print("We didn't reach our goal for this period. More work is needed.")
            else:
                print("You did well this period! Keep up the great work!")
            profit.clear()
    
    match input_type:
        case 3:
            for weekday in week[0:5]:
                print (f"For {weekday}")
                day = "the week"
                while condition_a == True:
                    a=input('Enter product number 1-5, or enter 0 to stop: ')
                    while a != "0" and a != "1" and a != "2" and a != "3" and a != "4" and a != "5":
                        print("Error. Invalid value entered. Please try again.")
                        a = input("Enter product number 1-5, or enter 0 to stop: ")
                    a = int(a)
                    if a == 0:
                        break
                    else:
                        quantity = input("Enter quantity sold: ")
                        while quantity.isdigit() == False:
                            print("Error. Invalid value entered. Please try again.")
                            quantity = input("Enter quantity sold: ")
                        quantity = int(quantity)
                        profit_per_product = product_dictionaries.get(a)
                        total_profit = profit_per_product*quantity
                        profit.append(total_profit)
            total_profit = sum(profit)
            print(f"Total Profit for the week (business day) is: ${total_profit:.2f}")
            if total_profit <= 10000:
                print("We didn't reach our goal for this period. More work is needed.")
            else:
                print("You did well this period! Keep up the great work!")
            profit.clear()
    
    match input_type:
        case 4:
            for weekday in week[5:7]:
                print (f"For {weekday}")
                while condition_a == True:
                    a=input('Enter product number 1-5, or enter 0 to stop: ')
                    while a != "0" and a != "1" and a != "2" and a != "3" and a != "4" and a != "5":
                        print("Error. Invalid value entered. Please try again.")
                        a = input("Enter product number 1-5, or enter 0 to stop: ")
                    a = int(a)
                    if a == 0:
                        break
                    else:
                        quantity = input("Enter quantity sold: ")
                        while quantity.isdigit() == False:
                            print("Error. Invalid value entered. Please try again.")
                            quantity = input("Enter quantity sold: ")
                        quantity = int(quantity)
                        profit_per_product = product_dictionaries.get(a)
                        total_profit = profit_per_product*quantity
                        profit.append(total_profit)
            total_profit = sum(profit)
            print(f"Total Profit for the week (weekend) is: ${total_profit:.2f}")
            if total_profit <= 10000:
                print("We didn't reach our goal for this period. More work is needed.")
            else:
                print("You did well this period! Keep up the great work!")
            profit.clear()
    
    match input_type:
        case 0:
            exit()

