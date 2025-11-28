age = int(input("Enter your age : "))
ticket = bool(input("Do you have a ticket 1 for true or 0 for false"))
t = bool(ticket)
if age > 18:
    print("You can watch the movie")
    if age > 18:
         print("Show your id") 
         if ticket == True:
            print("you can go inside")
         elif ticket == False:
             print("you can't go inside")
    elif age < 15:
        print("you can watch the movie with parents")
else:
    print("you are not allowed for the movie")
