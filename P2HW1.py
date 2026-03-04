#Durante, Adrian
#20260303
#P2HW1
#Width Formatting

#def get_budget():

#Get input from the user
#Convert the input string to a float


#3. Ask user to enter their budget
#Check if the budget is a positive number
budget_input = input("Please enter your budget amount: $")
budget = float(budget_input)

if budget < 4000:
    print("You do not have enough.")
else: 
    print("Proceed")
#4. Ask user to enter travel destination

destination = input("Enter your travel destination: ")


print(f"Your travel destination is: {destination}")

#5. Ask user for amount they will spend on gas
#
#6. Ask user for amount they will spend on accommodation
#
#7. Ask user for amount they will spend on food
#
#8. Add expenses
#
#9. Subtract expenses from budget
#
#10. Display results

print("-------- Travel Expenses --------")
print(f"{'Location:':<20}{'New York City':<15}")
print(f"{'Initial Budget:':<20}${2000.00:<7.2f}")
print(f"{'Fuel:':<20}${450.00:<7.2f}")
print(f"{'Accomodation:':<20}${600.00:<7.2f}")
print(f"{'Food:':<20}${250.00:<7.2f}")
print("---------------------------------")

print(f"{'Remaining Balance:':20}${700.00:<7.2f}")