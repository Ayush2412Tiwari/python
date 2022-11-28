#ROLLING DICE GAME
print("Welcome to the game")
      

#Importing library random
import random
count = 0
#
while True:
    
#Taking choice from user 
    user_choice = int(input("Enter the number you want to choose: "))


    if 1<=user_choice<=6:
#Assigning computer choice
        computer_choice = random.randint(1,6)
        print("computer_choice=",computer_choice)
        print("User choice is: ",user_choice,",computer choice is: ",computer_choice)

#Checking whether player won or lost.
        if user_choice == computer_choice:
            count+=1
            print("You won")
        elif user_choice!=computer_choice:
            print("You loose")
    else:
        print("Wrong Choice")
#Checking whether player wants to continue the game.     
    next=input("Do you want to play again? (yes/no)")
    if next == "yes":
        continue
    else:
        break
print("No of times won=",count)
        
