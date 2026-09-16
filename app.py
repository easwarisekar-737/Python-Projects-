exprenses=[]

def add_expense():
    
    print("\n------Add Expense------")
    
    name=input("Enter the name of the expense:")
    amount=float(input("Enter the amount :"))
    category=input("Enter the category :")
    date=input("Enter the date[dd/mm/yyyy]:")
    

    expense={
        "name": name,
        "amount":amount,
        "category":category,
        "date":date
    }
    
    exprenses.append(expense)
    
    print("\n✔Expense are added succesfully......")

def view_expense():
    print("\n------View All Expenses------")
    
    if len(exprenses) == 0:
        print("No expenses to display.")
        return
    
    else:
        for i, expense in enumerate(exprenses, start=1):
            print(f"\nExpense {i}")

            
            print(
                f"Name: {expense['name']}"
                f"Amount: ₹{expense['amount']} "
                f"Category: {expense['category']} "
                f"Date: {expense['date']}"
            )


def total_spending():
    total=0
    
    for expense in exprenses:
        total += expense['amount']
    
    print(f"\nTotal Spending: {total}/-")

def main():
    while True:
        print("\n--------------------------------")
        print("         Expense Tracker          ")
        print("\n--------------------------------")

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expense()
        elif choice == '3':
            total_spending()
        elif choice == '4':
            print("\nThank you for using Expense Tracker!")
            break
        else:
            print("❌Invalid choice. Please try again.")
            
main()
