#variables for the total cost of each period of time
daytotal = 0
weekdaytotal = 0
weektotal = 0
weekendtotal = 0

#lists to go through for each period of time
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekend = ["Saturday", "Sunday"]

#entrance messages
print("Welcome to Circle Phones' Profit calculator.\n")
print("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend.")
print("Enter:")
print("\t1 - For specific Day\n".expandtabs(3),"\t2 - For the Week\n".expandtabs(2),"\t3 - For Week Business Days\n".expandtabs(2),"\t4 - For Weekend Days\n".expandtabs(2),"\t0 - Exit".expandtabs(2))

#checking if period of time works
PeriodOfTime = input()
while PeriodOfTime != "1" and PeriodOfTime != "2" and PeriodOfTime != "3" and PeriodOfTime != "4" and PeriodOfTime != "0":
    print("Did not enter a  valid period of time. Please try again.")
    print("Enter:")
    print("\t1 - For specific Day\n".expandtabs(3),"\t2 - For the Week\n".expandtabs(2),"\t3 - For Week Business Days\n".expandtabs(2),"\t4 - For Weekend Days\n".expandtabs(2),"\t0 - Exit".expandtabs(2))
    PeriodOfTime = input()
PeriodOfTime = int(PeriodOfTime)

while PeriodOfTime:
    
    if PeriodOfTime == 1:

        #asking for specific day and checking if it is a valid day
        day = input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: ")
        day = day.capitalize()
        while day != "Monday" and day != "Tuesday" and day != "Wednesday" and day != "Thursday" and day != "Friday" and day != "Saturday" and day != "Sunday":
            print("Did not enter a valid day. Please try again.")
            day = input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: ")
            day = day.capitalize()
        print("For", day)
        
        product_number = input("Enter product number 1-5, or enter 0 to stop: ")
        while product_number != "0" and product_number != "1" and product_number != "2" and product_number != "3" and product_number != "4" and product_number != "5":
            print("Error. Invalid value entered. Please try again.")
            product_number = input("Enter product number 1-5, or enter 0 to stop: ")
        product_number = int(product_number)
        
        
        while product_number:
            
            quantity = input("Enter quantity sold: ")
            while quantity.isdigit() == False:
                print("Error. Invalid value entered. Please try again.")
                quantity = input("Enter quantity sold: ")
            quantity = int(quantity)
            
            if product_number == 1:
                daytotal += 120.45*quantity  
            elif product_number == 2:
                daytotal += 99.50*quantity
            elif product_number == 3:
                daytotal += 75.69*quantity
            elif product_number == 4:
                daytotal += 65.73*quantity
            elif product_number == 5:
                daytotal += 51.49*quantity
            
            product_number = input("Enter product number 1-5, or enter 0 to stop: ")
            while product_number != "0" and product_number != "1" and product_number != "2" and product_number != "3" and product_number != "4" and product_number != "5":
                print("Error. Invalid value entered. Please try again.")
                product_number = input("Enter product number 1-5, or enter 0 to stop: ")
            product_number = int(product_number)
        
        if product_number == 0:
            print(f"Your total profit for {day} is: $", format(daytotal,".2f")) 
        
        if daytotal >= 10000:
            print("You did well this period! Keep up the great work!")
        else: 
            print("We didn't reach our goal for this period. More work is needed.") 
        
        print("\n\nYou can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend.")
        print("Enter:")
        print("\t1 - For specific Day\n".expandtabs(3),"\t2 - For the Week\n".expandtabs(2),"\t3 - For Week Business Days\n".expandtabs(2),"\t4 - For Weekend Days\n".expandtabs(2),"\t0 - Exit".expandtabs(2))
        
        PeriodOfTime = input()
        while PeriodOfTime != "1" and PeriodOfTime != "2" and PeriodOfTime != "3" and PeriodOfTime != "4" and PeriodOfTime != "0":
            print("Did not enter a  valid period of time. Please try again.")
            print("Enter:")
            print("\t1 - For specific Day\n".expandtabs(3),"\t2 - For the Week\n".expandtabs(2),"\t3 - For Week Business Days\n".expandtabs(2),"\t4 - For Weekend Days\n".expandtabs(2),"\t0 - Exit".expandtabs(2))
            PeriodOfTime = input()
        PeriodOfTime = int(PeriodOfTime)
    
    elif PeriodOfTime == 2:
        
        for weekday in week:
            print (f"For {weekday}")

            product_number = input("Enter product number 1-5, or enter 0 to stop: ")
            while product_number != "0" and product_number != "1" and product_number != "2" and product_number != "3" and product_number != "4" and product_number != "5":
                print("Error. Invalid value entered. Please try again.")
                product_number = input("Enter product number 1-5, or enter 0 to stop: ")
            product_number = int(product_number)

            while product_number:

                quantity = input("Enter quantity sold: ")
                while quantity.isdigit() == False:
                    print("Error. Invalid value entered. Please try again.")
                    quantity = input("Enter quantity sold: ")
                quantity = int(quantity)

                if product_number == 1:
                    weektotal += 120.45*quantity  
                elif product_number == 2:
                    weektotal += 99.50*quantity
                elif product_number == 3:
                    weektotal += 75.69*quantity
                elif product_number == 4:
                    weektotal += 65.73*quantity
                elif product_number == 5:
                    weektotal += 51.49*quantity

                product_number = input("Enter product number 1-5, or enter 0 to stop: ")
                while product_number != "0" and product_number != "1" and product_number != "2" and product_number != "3" and product_number != "4" and product_number != "5":
                    print("Error. Invalid value entered. Please try again.")
                    product_number = input("Enter product number 1-5, or enter 0 to stop: ")
                product_number = int(product_number)

        if product_number == 0:
            print(f"Your total profit for the week is: $", format(weektotal,".2f")) 
        
        if weektotal >= 10000:
            print("You did well this period! Keep up the great work!")
        else: 
            print("We didn't reach our goal for this period. More work is needed.") 
        
        print("\n\nYou can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend.")
        print("Enter:")
        print("\t1 - For specific Day\n".expandtabs(3),"\t2 - For the Week\n".expandtabs(2),"\t3 - For Week Business Days\n".expandtabs(2),"\t4 - For Weekend Days\n".expandtabs(2),"\t0 - Exit".expandtabs(2))
        
        PeriodOfTime = input()
        while PeriodOfTime != "1" and PeriodOfTime != "2" and PeriodOfTime != "3" and PeriodOfTime != "4" and PeriodOfTime != "0":
            print("Did not enter a  valid period of time. Please try again.")
            print("Enter:")
            print("\t1 - For specific Day\n".expandtabs(3),"\t2 - For the Week\n".expandtabs(2),"\t3 - For Week Business Days\n".expandtabs(2),"\t4 - For Weekend Days\n".expandtabs(2),"\t0 - Exit".expandtabs(2))
            PeriodOfTime = input()
        PeriodOfTime = int(PeriodOfTime)

    elif PeriodOfTime == 3:
        
        for weekday in weekdays:
            
            print (f"For {weekday}")
            
            product_number = input("Enter product number 1-5, or enter 0 to stop: ")
            while product_number != "0" and product_number != "1" and product_number != "2" and product_number != "3" and product_number != "4" and product_number != "5":
                print("Error. Invalid value entered. Please try again.")
                product_number = input("Enter product number 1-5, or enter 0 to stop: ")
            product_number = int(product_number)
        
            while product_number:
            
                quantity = input("Enter quantity sold: ")
                while quantity.isdigit() == False:
                    print("Error. Invalid value entered. Please try again.")
                    quantity = input("Enter quantity sold: ")
                quantity = int(quantity)
            
                if product_number == 1:
                    weekdaytotal += 120.45*quantity  
                elif product_number == 2:
                    weekdaytotal += 99.50*quantity
                elif product_number == 3:
                    weekdaytotal += 75.69*quantity
                elif product_number == 4:
                    weekdaytotal += 65.73*quantity
                elif product_number == 5:
                    weekdaytotal += 51.49*quantity
                
                product_number = input("Enter product number 1-5, or enter 0 to stop: ")
                while product_number != "0" and product_number != "1" and product_number != "2" and product_number != "3" and product_number != "4" and product_number != "5":
                    print("Error. Invalid value entered. Please try again.")
                    product_number = input("Enter product number 1-5, or enter 0 to stop: ")
                product_number = int(product_number)
            
        if product_number == 0:
            print("Your total profit for this week (business days) is: $", format(weekdaytotal,".2f")) 
        
        if weekdaytotal >= 10000:
            print("You did well this period! Keep up the great work!")
        else: 
            print("We didn't reach our goal for this period. More work is needed.") 
        
        print("\n\nYou can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend.")
        print("Enter:")
        print("\t1 - For specific Day\n".expandtabs(3),"\t2 - For the Week\n".expandtabs(2),"\t3 - For Week Business Days\n".expandtabs(2),"\t4 - For Weekend Days\n".expandtabs(2),"\t0 - Exit".expandtabs(2))
        
        PeriodOfTime = input()
        while PeriodOfTime != "1" and PeriodOfTime != "2" and PeriodOfTime != "3" and PeriodOfTime != "4" and PeriodOfTime != "0":
            print("Did not enter a  valid period of time. Please try again.")
            print("Enter:")
            print("\t1 - For specific Day\n".expandtabs(3),"\t2 - For the Week\n".expandtabs(2),"\t3 - For Week Business Days\n".expandtabs(2),"\t4 - For Weekend Days\n".expandtabs(2),"\t0 - Exit".expandtabs(2))
            PeriodOfTime = input()
        PeriodOfTime = int(PeriodOfTime)

    elif PeriodOfTime == 4:
        
        for weekday in weekend:

            print (f"For {weekday}")

            product_number = input("Enter product number 1-5, or enter 0 to stop: ")
            while product_number != "0" and product_number != "1" and product_number != "2" and product_number != "3" and product_number != "4" and product_number != "5":
                print("Error. Invalid value entered. Please try again.")
                product_number = input("Enter product number 1-5, or enter 0 to stop: ")
            product_number = int(product_number)

            while product_number:
                    
                quantity = input("Enter quantity sold: ")
                while quantity.isdigit() == False:
                    print("Error. Invalid value entered. Please try again.")
                    quantity = input("Enter quantity sold: ")
                quantity = int(quantity)   
                    
                if product_number == 1:
                    weekendtotal += 120.45*quantity  
                elif product_number == 2:
                    weekendtotal += 99.50*quantity
                elif product_number == 3:
                    weekendtotal += 75.69*quantity
                elif product_number == 4:
                    weekendtotal += 65.73*quantity
                elif product_number == 5:
                    weekendtotal += 51.49*quantity
                
                product_number = input("Enter product number 1-5, or enter 0 to stop: ")
                while product_number != "0" and product_number != "1" and product_number != "2" and product_number != "3" and product_number != "4" and product_number != "5":
                    print("Error. Invalid value entered. Please try again.")
                    product_number = input("Enter product number 1-5, or enter 0 to stop: ")
                product_number = int(product_number)

        if product_number == 0:
            print(f"Your total profit for the weekend is: $", format(weekendtotal,".2f")) 
        
        if weekendtotal >= 10000:
            print("You did well this period! Keep up the great work!")
        else: 
            print("We didn't reach our goal for this period. More work is needed.") 
        
        print("\n\nYou can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend.")
        print("Enter:")
        print("\t1 - For specific Day\n".expandtabs(3),"\t2 - For the Week\n".expandtabs(2),"\t3 - For Week Business Days\n".expandtabs(2),"\t4 - For Weekend Days\n".expandtabs(2),"\t0 - Exit".expandtabs(2))
        
        PeriodOfTime = input()
        while PeriodOfTime != "1" and PeriodOfTime != "2" and PeriodOfTime != "3" and PeriodOfTime != "4" and PeriodOfTime != "0":
            print("Did not enter a  valid period of time. Please try again.")
            print("Enter:")
            print("\t1 - For specific Day\n".expandtabs(3),"\t2 - For the Week\n".expandtabs(2),"\t3 - For Week Business Days\n".expandtabs(2),"\t4 - For Weekend Days\n".expandtabs(2),"\t0 - Exit".expandtabs(2))
            PeriodOfTime = input()
        PeriodOfTime = int(PeriodOfTime)
    
    elif PeriodOfTime == 0:
        break