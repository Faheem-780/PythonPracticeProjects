balance=1000.0 #Starting Balance
def check_balance():
    print(f"Your current Balance is ,{balance},😏")
def deposit(amount):
    global balance
    if amount>0:
        balance+=amount
        print(f'Ching Chang🤑!Successfully deposited,{amount} ')
    else:
        print('Warning⚠️!invalid amount. Please deposit a positive amount') 
def withdraw(amount):
    global balance
    if amount>balance:
        print("Insufficient funds❗transactions canceled")
    elif amount<0:
        print("Invalid Amount❗Please enter a value greater than 0")
    else:
        balance-=amount
    print(f"Hurray🎉🤑🥳!well that's genrous.\n You have successfully withdrawn,{amount}")
def atm_menu():
    print("Welcom to PYTHON ATM")
    print("1. Check Balance")
    print("2. Deposite Money")
    print("3. Withdraw Money")
    print("4  Exit")
while True:
    atm_menu()
    choice=input("Select an option (1-4)]")
    if choice=='1':
        check_balance()
        break
    elif choice=='2':
        dep_amount=float(input("Enter a withdrawl amount"))
        deposit(dep_amount)
        break            
    elif choice=='3':
        withdraw_amount=float(input("Enter withdrawl amount:"))
        withdraw(withdraw_amount)
        break
    elif choice=='4':
        print("Thankyou for using our ATM services.\n GoodBye👋")
        break                      
    else:
       print("Invalid selection⚠️ .Please try again")