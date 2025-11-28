# ATM Machine Simulation (Python)

A simple Python-based ATM program that allows users to authenticate using a PIN and perform basic banking operations such as deposit, withdrawal, and balance inquiry.


## Features

- PIN authentication (3 attempts allowed)
- Deposit money
- Withdraw money with balance check
- Show current account balance
- Invalid input handling
- ATM lock after 3 incorrect PIN attempts

##  How It Works

1. User enters a 4-digit PIN  
2. If correct → user selects an operation  
3. If incorrect → attempts reduce  
4. After 3 wrong attempts → ATM access is blocked  


##  Available Operations

| Option | Operation         |
|--------|-------------------|
|   1    | Deposit Amount    |
|   2    | Withdraw Amount   |
|   3    | Show Balance      |
