def add_expense(expenses, desc, amt, cat, date): # defining add expense function
    new_id=len(expenses)+1
    exp={"id": new_id,"description": desc,"amount": amt,"category": cat,"date": date}
    expenses.append(exp)
    return exp
def add_income(incomes, src, amt, date):  # defining the add income function
    new_id=len(incomes) + 1
    inc={"id": new_id,"source": src,"amount": amt,"date": date}
    incomes.append(inc)
    return inc

def total_expenses(expenses): # definig the total expense expense function
    return sum(e["amount"] for e in expenses)
def total_incomes(incomes): # defining total income function
    return sum(i["amount"] for i in incomes)
def net_balance(expenses,incomes):  # defining the net balance function
    return total_incomes(incomes) - total_expenses(expenses)

