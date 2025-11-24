import json  # importing json module for storage

import os  #   importing  os

FILE_PATH="finance_data.json"  # this is the file which has all the data entered and stored by a programmerr


def load_data(): # defining load data function
    if not os.path.exists(FILE_PATH):
      return [],[]

    with open(FILE_PATH, "r") as file:
        data=json.load(file)
    return data.get("expenses",[]),data.get("incomes", [])


def save_data(expenses, incomes): # defining save_data function to 
    with open(FILE_PATH,"w") as file  :
        json.dump({"expenses": expenses, "incomes": incomes}, file)
        
