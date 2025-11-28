balance = 9000      
pin = 1234         
attempts = 0        

while attempts < 3:    
    user_pin = input("Enter your pin:")

    if not user_pin.isdigit():
        print("PIN must be a number!")
        attempts += 1
        print(f"Attempts left: {3 - attempts}")
        continue

    user_pin = int(user_pin)       

    if user_pin == pin:            
        print("PIN verified successfully")
        print("1. Amount Deposit")
        print("2. Amount Withdrawal")
        print("3. Show Balance")

        choice = input("Enter your operation (1, 2 or 3):")

        if choice not in ['1','2','3']:   # Validate choice
            print("Invalid Choice! Please select between (1-3)")
            continue

       
        if choice == "3":
            print("ACCOUNT BALANCE")
            print(f"Available Balance: ₹{balance}")
            break

       
        try:
            amount = int(input("Enter the amount:"))
        except ValueError:
            print("Invalid input! Please enter amount in numerals")
            continue

        
        if choice == "2":
            if amount <= balance:
                balance -= amount

                print("TRANSACTION ALERT")
                print(f"₹{amount} Debited from Your Account")
                print("Txn Type       : ATM Cash Withdrawal")
                print("Status         : Successful")
                print(f"Available Balance : ₹{balance}")

            else:
                print("TRANSACTION FAILED")
                print("Reason: Insufficient Balance")

       
        elif choice == "1":
            balance += amount

            print("TRANSACTION ALERT")
            print(f"₹{amount} Credited to Your Account")
            print("Txn Type       : Cash Deposit")
            print("Status         : Successful")
            print(f"Available Balance : ₹{balance}")

        break

    else:
        attempts += 1         
        print("Incorrect PIN")

        if attempts == 3:    
            print("Your ATM access is Blocked after 3 invalid attempts")
        else:
            print(f"Attempts left: {3 - attempts}")
