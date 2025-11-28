PASSWORD_FILE = "password.txt"
MASTER_PASSWORD = "admin123"  

def add_password():
    account = input("Enter account/service name: ")
    identifier = input("Enter username/email/phone: ")
    pwd = input("Enter password: ")
    with open(PASSWORD_FILE, "a") as file:
        file.write(f"{account}:{identifier}:{pwd}\n")
    print(f"Password for {account} saved successfully.\n")

def view_passwords():
    entered = input("Enter master password to view passwords: ")
    if entered != MASTER_PASSWORD:
        print("Wrong password! Access denied.\n")
        return
    try:
        with open(PASSWORD_FILE, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No passwords stored yet.\n")
                return
            print("\nStored Passwords:")
            for line in lines:
                account, identifier, pwd = line.strip().split(":", 2)
                print(f"Account: {account}, Identifier: {identifier}, Password: {pwd}")
            print()
    except FileNotFoundError:
        print("No passwords stored yet.\n")

def delete_password():
    account_to_delete = input("Enter account/service name to delete: ")
    try:
        with open(PASSWORD_FILE, "r") as file:
            lines = file.readlines()
        found = False
        with open(PASSWORD_FILE, "w") as file:
            for line in lines:
                account, identifier, pwd = line.strip().split(":", 2)
                if account != account_to_delete:
                    file.write(line)
                else:
                    found = True
        if found:
            print(f"{account_to_delete} deleted successfully.\n")
        else:
            print(f"No account named {account_to_delete} found.\n")
    except FileNotFoundError:
        print("No passwords stored yet.\n")

def password_manager():
    while True:
        print("----- Simple Password Manager -----")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Delete Password")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            delete_password()
        elif choice == "4":
            break
        else:
            print("Invalid choice! Try again.\n")


def bmi_calculator():
    while True:
        print("\n=== BMI Calculator ===")
        
        name = input("Enter your name: ")
        
        # Trigger personal dashboard if secret pin is entered
        if name == "1234":
             print("\nSecret pin detected! Launching Password Manager...\n")
             password_manager()
             continue
        
        try:
            weight = float(input("Enter your weight in kgs: "))
            height = float(input("Enter your height in cm: "))
        except ValueError:
            print("Please enter valid numbers for weight and height.")
            continue

        height_m = height / 100
        bmi = weight / (height_m ** 2)
        print(f"{name}'s BMI is: {bmi:.2f}")
        
        if bmi < 18.5:
            print("You are underweight")
        elif 18.5 <= bmi < 25:
            print("You are normal weight")
        elif 25 <= bmi < 30:
            print("You are overweight")
        else:
            print("You are obese")
        
        again = input("Do you want to calculate again? (yes/no): ").lower()
        if again != "yes":
            print("Thank you --- Goodbye!")
            break
            
if __name__ == "__main__":
    bmi_calculator()
