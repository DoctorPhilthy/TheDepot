

hourly_pay = float(input("How many dollars do you make per hour?: "))
hours_worked = float(input("How many hours do you work per week?: "))

pretax_pay = (hourly_pay * hours_worked)

print("You make $" + str(pretax_pay) + " per week.\n Sad...\n")

answer = input("\n Is that even enough to live on? y/n: ")

if answer == "y":
    print("\nMy, you live a frugal lifestyle.")

else:
        print("\nThen get a real job!")
        
