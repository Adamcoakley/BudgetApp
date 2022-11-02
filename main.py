from budget import Budget
import os
from sys import platform

# clear console
if platform == "win32":
    clear = lambda: os.system("cls")
else:
    clear = lambda: os.system("clear")
# create an empty categories list
categories = []
# create an empty objects list
budgets = []

# function to print a menu
def menu():
    print("----------------")
    print("----- MENU -----")
    print("----------------")
    print("1: Create a category")
    print("2: Deposit to a category")
    print("3: Withdraw from a category")
    print("4: Transfer to another category")
    print("5: Get balance from specific category")
    print("6: Exit")
    print("----------------")
    option = int(input("Enter an option: "))
    return option


# while loop to keep the application running
control = True
while control:
    # print the menu
    option = menu()
    if option == 1:
        clear()
        print("1: Create a category")
        # enter a category category to create
        category = input("Please enter a category name: ")
        # check if the category exists
        if category in categories:
            print("Category already exists")
        else:
            # ask the user to enter an amount
            amount = int(input("Enter an amount: "))
            # append to categories and objects list
            budgets.append(Budget(amount, category))
            categories.append(category)
            # open a file with the new category
            with open(f"{category}.txt", "w") as file:
                file.write(f"Category created. Name: {category}, balance: {amount}.\n")
                print(f"Category created. Name: {category}, balance: {amount}.\n")
    elif option == 2:
        clear()
        print("2: Deposit to a category")
        # enter a category category to deposit to
        category = input("Please enter a category name: ")
        if category in categories:
            # category exists, ask the user to enter an amount
            amount = int(input("Enter an amount: "))
            # loop through the budget objects
            for budget in budgets:
                if budget.category == category:
                    budget.deposit(amount)
                    new_balance = budget.getBalance()
            # add a line to the file
            with open(f"{category}.txt", "a") as file:
                file.write(
                    f"Deposited {amount} euro to {category}. New balance: {new_balance} \n"
                )
                print(
                    f"Deposited {amount} euro to {category}. New balance: {new_balance}\n"
                )
        else:
            # category does not exist
            print("Category does not exist.")
    elif option == 3:
        clear()
        print("3: Withdraw from a category")
        # enter a category category to withdraw from
        category = input("Please enter a category name: ")
        if category in categories:
            # category exists, ask the user to enter an amount
            amount = int(input("Enter an amount: "))
            # loop through the budget objects
            for budget in budgets:
                if budget.category == category:
                    budget.withdraw(amount)
                    new_balance = budget.getBalance()
            # add a line to the file
            with open(f"{category}.txt", "a") as file:
                file.write(
                    f"Withdrew {amount} euro from {category}. New balance: {new_balance} \n"
                )
                print(
                    f"Withdrew {amount} euro from {category}. New balance: {new_balance}\n"
                )
        else:
            # category does not exist
            print("Category does not exist.")
    elif option == 4:
        clear()
        print("4: Transfer to another category")
        # enter a category category to deposit into
        to_category = input("Transfer to: ")
        # enter a category category to withdraw from
        from_category = input("Transfer from: ")
        if to_category in categories and from_category in categories:
            # both categories exists, ask the user to enter an amount
            amount = int(input("Enter an amount to transfer: "))
            # loop through budget objects
            for budget in budgets:
                # find the to_category
                if budget.category == to_category:
                    # deposit
                    budget.deposit(amount)
                    # get the new balance
                    new_balance = budget.getBalance()
                    # add a line to the file
                    with open(f"{to_category}.txt", "a") as file:
                        file.write(
                            f"Recieved {amount} euro from {from_category}. New balance: {new_balance} \n"
                        )
                # find the from_category
                if budget.category == from_category:
                    # withdraw
                    budget.withdraw(amount)
                    # get the new balance
                    new_balance = budget.getBalance()
                    # add a line to the file
                    with open(f"{from_category}.txt", "a") as file:
                        file.write(
                            f"Transferred {amount} euro to {to_category}. New balance: {new_balance} \n"
                        )
                        # print to the terminal
                        print(
                            f"Transferred {amount} euro from {from_category} to {to_category}.\n"
                        )
        else:
            # category does not exist
            print("Category does not exist.")
    elif option == 5:
        clear()
        print("5: Get balance from specific category")
        # enter a category category to deposit to
        category = input("Please enter a category name: ")
        if category in categories:
            for budget in budgets:
                # find the to_category
                if budget.category == to_category:
                    balance = budget.getBalance()
                    print(f"Name: {category}, balance: {balance}\n")
        else:
            # category does not exist
            print("Category does not exist.")
    else:
        clear()
        print("Thanks for using my budget application!")
        control = False
