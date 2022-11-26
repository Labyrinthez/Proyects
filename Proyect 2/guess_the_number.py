import random as r
def gessing_game(attempts):
    number_in_mind = r.randint(0,100)
    while True:
        number = int(input("Type a number: "))
        if number > number_in_mind:
            print("Too high")
            attempts-=1
        elif number < number_in_mind:
            print("Too low")
            attempts -=1
        else:
            print("You win uwu")
            exit()
        if attempts == 0:
            print("You lose!")
            exit()
        print("Remaining attempts are: ",attempts)

print("Welcome to the guessing number game!\nI'm thinking in a number between 1 and 100")
level = input("Select the difficulty: 'easy' or 'hard': ")
if level == 'easy':
    gessing_game(10)
elif level == 'hard':
    gessing_game(5)
else:
    print("Invalid option, try again")