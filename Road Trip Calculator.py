# Alex Coffman 28/JUL/23
# CMIS 102/6980 Week 7 Assignment
# This program creates two separate arrays from user inputs:
    # Creates a gas cost and food cost lists
    # Calculates total cost for the gas and the food and displays
    # Calculates each persons share of costs and displays
# The country visited was Greece and the currency is in Euros   
# Welcome message for the user
print("\nWelcome to the road trip cost analysis\n")
print("This program will add up your fuel and food costs as well as calculate each persons share of the costs!")
print("Only enter numeric values for all input requests.")
# Function that prompts user for inputs, appends food and gas costs into empty arrays, loops to ensure the proper inputs are received
def usercostData():
    
    while True:
        try:
            #  Loop to check for negative numbers, also returns if a alpha character is input  
            people = int(input("How many people went on the trip: \n"))
            if people < 0:
                raise ValueError
            # Loop to check for negative numbers, also returns if a alpha character is input  
            days = int(input("How many days did the trip take: \n"))
            if days < 0:
                raise ValueError
            # Initialized arrays for food and gas
            daily_food = []
            daily_gas = []
            # Counts the day in days from the input and prompts for food and gas until it couts up to the number of days entered
            for day in range(1, days + 1):
                while True:
                    # Looped prompt to get the food cost, if it is a possitive numeric value it is appended to the array for food
                    try:
                        daily_foodcost = eval(input(f"Enter the costs for food on Day {day}: "))
                        if daily_foodcost <0:
                            raise ValueError
                        daily_food.append(daily_foodcost)
                        # Looped prompt to get the gas cost, if it is a possitive numeric value it is appended to the array for gas
                        daily_gascost = eval(input(f"Enter the costs for gas on Day {day}: "))
                        if daily_gascost < 0:
                            raise ValueError
                        daily_gas.append(daily_gascost)
                    # If the wrong value is entered, the user is notified
                        break
                    except ValueError:
                        print("Invalid input. Please enter a non-negative numeric number.")
            # The function returns these variables   
            return people, daily_food, daily_gas
        except ValueError:
            print("Invalid input. Please enter a non-negative numeric number.")

# Function that does the cost calculations for the user
def costCalculation(daily_food, daily_gas):
    # Sums the food costs and gas costs separately, then gets the total cost of the trip
    totalFood_cost = sum(daily_food)
    totalGas_cost = sum(daily_gas)
    totalTrip_cost = totalFood_cost + totalGas_cost
    # The function returns these variables rounded to the hundredths place
    return round(totalFood_cost, 2), round(totalGas_cost, 2), round(totalTrip_cost, 2)

# Function that calculates the total shared costs for each person on the road trip
def costPer_person(totalTrip_cost, people):
    # Divides the total cost by the number of people on the trip and rounds to the hundredths place
    perPerson_share = round(totalTrip_cost / people, 2)
    # The function returns the shared cost variable
    return perPerson_share

# The main program that calls all the functions and displays them for the user
def main():
    # Calls the usercostData function, this is needed for costCalculation function to call properly
    people, daily_food, daily_gas = usercostData()
    # Calls the costCalculation function
    totalFood_cost, totalGas_cost, total_trip_cost = costCalculation(daily_food, daily_gas)
    # Prints all the totals for the user in Euros
    print("\nYour totals are as follows:\n")
    print("Total cost of food: €", totalFood_cost)
    print("Total cost of gas: €", totalGas_cost)
    print("Total cost of the trip: €", total_trip_cost)
    # Calls the costPer_person fucntion
    perPerson_share = costPer_person(total_trip_cost, people)
    # Prints the individual costs for each person on the trip in Euros
    print("The shared cost for each person: €", perPerson_share)

main()