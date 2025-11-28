while True:
    print("Select Operation:")
    print("1. Addition(+)")
    print("2. Subtraction(-)")
    print("3. Multiplication(*)")
    print("4. Division(/)")
    print("5. Modulo(%)")
    print("6. Exit")
  
    choice = input("Enter your choice:")
    if choice == "6":
        print("User Say Goodbye Calculator")
        break
    if choice not in ['1','2','3','4','5','6']:
        print("Invalid Choice! Please Enter the Choice between (1-6)")
    try:
        n1 = float(input("Enter your first number:"))
        n2 = float(input("Enter your second number:"))
    except ValueError:
        print("Invalid input! Please enter Integer value")
        continue
    if choice == "1":
        print("Addition of desired two no. is:", n1 + n2)
    elif choice == "2":
        print(f"Subtraction of {n2} from {n1} is:", n1 - n2)
    elif choice == "3":
        print("Multiplication of desired two no. is:", n1 * n2)
    elif choice == "4":
        print(f"Division of {n1} by {n2} is:", n1 / n2)
    elif choice == "5":
        print(f"Modulo of {n1} by {n2} is:", n1 % n2)
