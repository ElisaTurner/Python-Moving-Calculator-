# This calculator calculates how long it would take in order to move 
# if saving a certain amount of money per paycheck  


def main():

    # Display intro
    print("Welcome to my Savings Calculator!\n")

    # Prompt for  name
    userName = input("Please enter your name: ")
    
    # prompt for weekly salary
    weeklySalary = float(input(f"\nHow much do you make per week {userName}: $"))
    
    # prompt for weekly expenses 
    weeklyExpenses = float(input(f"\nHow much are your weekly expenses {userName}: $"))
    
    # prompt for amount needed to move
    movingCost = float(input(f"\nHow much do you need to move {userName}: $"))

    # calculate how much i have left per week
    leftOverCash = weeklySalary - weeklyExpenses

    # calculate how many weeks itll take to fufill moving cost
    weeksNeeded = movingCost / leftOverCash

    # display how many weeks needed to move
    print(f"Weeks Needed to move: {weeksNeeded}")

main ()
    

