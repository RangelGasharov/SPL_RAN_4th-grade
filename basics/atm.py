selection = 0
bank_balance = 0
isGoing = True

while isGoing:
    selection = int(input("You can choose the following numbers to execute an action:\n"
                          "1: Deposit\n"
                          "2: Withdrawal\n"
                          "3: Bank balance\n"
                          "4: Exit\n"))
    if selection == 1:
        amount = int(input("Please enter the amount that you would like to deposit.\n"))
        bank_balance += amount
        print("You have deposited", amount, "euros.\n")
    if selection == 2:
        amount = int(input("Please enter the amount that you would like to withdrawal.\n"))
        if bank_balance >= amount:
            bank_balance -= amount
            print("You have withdrawn", amount, "euros.\n")
        else:
            print("The amount you would like to withdrawal exceeds your bank balance!\n")
    if selection == 3:
        print("Your current bank amount is", bank_balance, "euros\n")
    if selection == 4:
        isGoing = False
