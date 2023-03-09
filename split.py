def splitwise(expenses,balances):
    total_spent = sum(expenses.values()) #900
    num_users = len(expenses) #3
    avg_spent = total_spent // num_users   #300
    #balances = {}
    for user in expenses:
        balance = expenses[user] - avg_spent  #600-300
        balances[user] = balance
    return balances

def add_expense(expenses,balances):
    user = input("Enter the name of user: ")
   
    amount = int(input("Enter the amount spent by user: "))
    balances[user] = amount
    for user in expenses:
        balance=expenses[user]-amount
        balances[user]=balance
    return balances  
           

def split_equally(expenses,balances):
        print("Select the option :\n 1. New Expense \n 2. Add expense \n 3. Show Balance \n 4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            num_users = int(input("Enter the number of users: "))
            for i in range(num_users):
                user = input("Enter the name of user: ")
                if user not in expenses:
                    
                    amount = int(input("Enter the amount spent by user: "))
                    expenses[user] = amount
                else:
                    print("User already exists")
                    return split_equally(expenses,balances)
            balances = splitwise(expenses,balances)
            print("----------------------------------")
            for user in balances:
                if balances[user] < 0:
                    print("----------------------------------")
                    print(f"{user} owes {abs(balances[user])}")
                    print("----------------------------------")
                else:
                    print(f"{user} is owed {balances[user]}")
                    print("----------------------------------")

    #print(balances)
        elif choice == 2:
                    add_expense(expenses,balances)
                    print("----------------------------------")
                    print("Expense added successfully")
                    print("----------------------------------")
                    for user in balances:
                        if balances[user] < 0:
                            print("----------------------------------")
                            print(f"{user} owes {abs(balances[user])}")
                            print("----------------------------------")
                        else:
                            print(f"{user} is owed {balances[user]}")
                            print("----------------------------------")
        elif choice == 3:
            # balances = splitwise(expenses,balances)
            print("----------------------------------")
            for user in balances:
                if balances[user] < 0:
                    print("----------------------------------")
                    print(f"{user} owes {abs(balances[user])}")
                    print("----------------------------------")
                else:
                    print(f"{user} is owed {balances[user]}")
                    print("----------------------------------")
        elif choice == 4:
            return main()
def payback(expenses,balances):
    print("Select the option :\n 1. Payback \n 2. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        user1 = input("Enter the name of user who is paying back: ")
        user2 = input("Enter the name of user who is receiving the amount: ")
        amount = int(input("Enter the amount to be paid back: "))
        if(amount > abs(balances[user2])):
            print("Amount to be paid back is greater than the amount owed")
            return payback(expenses,balances)
        else:
            balances[user1] = balances[user1] + amount
            balances[user2] = balances[user2] - amount
            print("----------------------------------")
            print("Amount paid back successfully")
            print("----------------------------------")
            for user in balances:
                if balances[user] < 0:
                    print("----------------------------------")
                    print(f"{user} owes {abs(balances[user])}")
                    print("----------------------------------")
                else:
                    print(f"{user} is owed {balances[user]}")
                    print("----------------------------------")
    elif choice == 2:
        return main()
    else:
        print("Invalid choice")
        return main()
        
def main():
    expenses = {}
    balances = {}
    while True:
        print("Welcome to Splitwise")
        print("1. Split amount equally among all users")
        print("2. Payback amount")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            split_equally(expenses,balances)
        elif choice == 2:
            payback(expenses,balances)
        elif choice == 3:
            exit()
        else:
            print("Invalid choice")
            return main()
    
if __name__ == "__main__":
    main()
    