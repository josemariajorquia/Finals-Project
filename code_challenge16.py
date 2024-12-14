balance = 0

def create_account(name, initial_deposit = 0):
    Account_name = name
    b = 0
    b = initial_deposit
    balance = b
    print(f"\nAccount for {Account_name} with a initial deposit of {balance} has been created.")

def deposit_amount(amount):
    global balance
    balance += amount
    print(f"\nYou deposited ₱{amount}. New balance is ₱{balance}")

def check_balance():
    global balance
    print(f"Current balance is {balance}")

def get_denomination(amount):
    libo = amount // 1000
    sukli_libo = amount % 1000 

    five_h = sukli_libo // 500
    five_sukli = sukli_libo % 500

    two_h = five_sukli // 200
    two_sukli = five_sukli % 200

    one_h = two_sukli // 100
    one_sukli = two_sukli % 100

    pipti = one_sukli // 50
    sukli_pip = one_sukli % 50

    bente = sukli_pip // 20
    sukli_ben = sukli_pip % 20

    sampo = sukli_ben // 10  
    sukli_sam = sukli_ben % 10

    lima = sukli_sam // 5
    sukli_lima = sukli_sam % 5

    piso = sukli_lima // 1

    print(f"The Breakdown based on Philippine Denomination for the amount of {amount}")
    print(f"{libo} - 1000")
    print(f"{five_h} - 500")
    print(f"{two_h} - 200")
    print(f"{one_h} - 100")
    print(f"{pipti} - 50")
    print(f"{bente} - 20")
    print(f"{sampo} - 10")
    print(f"{lima} - 5")
    print(f"{piso} - 1")

def withdraw_amount(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrew {amount}. New balance is {balance}")
    else:
        print("Insufficient balance")


isCont = True
while isCont == True:
    print("WELCOME TO MY BANK STIMULATION SYSTEM")
    print("================================")
    print("ENTER FROM THE OPTIONS BELOW")
    print("1 --- CREATE ACCOUNT")
    print("2 --- DEPOSIT")
    print("3 --- CHECK BALANCE")
    print("4 --- WITHDRAW")
    print("5 --- EXIT")


    pick = input("Enter your choice here ---> ")

    if pick == "1":
        print("BANK APPLICATION FORM")
        name = input("Enter your FULL name: ")
        amount = eval(input(f"Enter initial deposit for {name}: "))
        create_account(name, amount)
        print(f"\nAccount for {name} with a deposit of {amount} has been created.")
        continue

    elif pick == "2":
        deposit = eval(input("Enter the amount you want to deposit: "))
        deposit_amount(deposit)
    
           
    elif pick == "3":
        check_balance()
        get_denomination(balance)
        continue

    elif pick == "4":
        withdraw = eval(input("Enter the amount you want to withdraw: "))
        amount -= withdraw
        withdraw_amount(withdraw)
        continue 

    elif pick == "5":
        print("Program stopped")
        print(f"\nThank you for using our bank! \nPlease come again!")
        break

    else:
        print("Invalid pick. Please try again.")
        continue