import json
import os

FILE_PATH = "finance_data.json"


def load_data():
    if not os.path.exists(FILE_PATH):
        return [], []

    with open(FILE_PATH, "r") as file:
        data = json.load(file)
        return data.get("expenses", []), data.get("incomes", [])


def save_data(expenses, incomes):
    with open(FILE_PATH, "w") as file:
        json.dump({"expenses": expenses, "incomes": incomes}, file)