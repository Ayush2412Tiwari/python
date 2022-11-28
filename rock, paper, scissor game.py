#ROCK PAPER SCISSOR GAME CODE
#ROCK PAPER SCISSORS
print("WELCOME TO THE GAME")
import random
while True:
    uS = input("Enter either rock or paper or scissor: ")
    cC = ['rock','paper','scissors']
    cS = random.choice(cC)
    print("user choice is : ",uS,"computer choice is : ",cS)
    if uS == 'rock' and cS == 'rock':
        print("tie")      
    elif uS == 'scissor' and cS == 'scissor':
        print("tie")
    elif uS == 'paper' and cS == 'paper':
        print("tie")
    elif uS == 'rock' and cS == 'scissor':
        print("you win")
    elif uS == 'rock' and cS == 'paper':
        print("you loose")
    elif uS == 'paper' and cS == 'rock':
        print("you win")
    elif uS == 'paper' and cS == 'scissors':
        print("you loose")
    elif uS == 'scissor' and cS == 'rock':
        print("you loose")
    elif uS == 'scissor' and cS == 'paper':
        print("you win")

    choice = input("want to play again?(yes/no)")
    if choice == "yes":
        continue
    else:
        print("thank you for playing")
        break
