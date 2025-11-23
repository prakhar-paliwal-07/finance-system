from utils import print_menu
import math
import matplotlib.pyplot as plt
from services import add_expense, add_income, total_expenses, total_incomes, net_balance
from storage import load_data, save_data
a="    "
b="  "
def run():
    expenses, incomes = load_data() 
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice =="1":
            desc =input("Description: ")
            amt=float(input("Amount: "))
            cat=input("Category: " )
            date=input("Date (YYYY-MM-DD): ")
            add_expense   (expenses, desc, amt, cat, date)
        elif choice=="2":
            src = input("Source: ")
            amt =float(input("Amount: "))
            date = input("Date (YYYY-MM-DD): ")
            add_income(incomes, src,  amt,  date) 
        elif choice== "3":
            print("Total Expenses:", total_expenses(expenses))
            print("Total Income:", total_incomes(incomes))
            print("Net Balance:", net_balance(expenses, incomes))
        elif choice ==   "0"  :
            save_data(expenses, incomes)
            print("Data saved.. Program ending....")
            break




        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    run()













