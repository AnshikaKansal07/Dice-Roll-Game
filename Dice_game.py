import random as r
print("Welcome to dice roll game: ")
win_c=0
win_u=0
dice=int(input("How many dies do you wish to use: "))
while True:
    sum_u=0
    sum_c=0
    oper=input("Enter roll to play or quit to exit game: ").lower()
    if oper=="quit":
        break
    else:
        print("You rolled: ")
        for i in range(dice):
            user=r.randint(1,6)
            print(user)
            sum_u= sum_u + user
        print("Computer rolled: ")
        for i in range(dice):
            comp=r.randint(1,6)
            print(comp)
            sum_c= sum_c + comp
        if sum_c>sum_u:
            print("Computer won this round.")
            win_c+=1
        elif sum_c<sum_u:
            print("You won this round.")
            win_u+=1
        else:
            print("Match draw.")
print("You won %d times and computer won %d times."%(win_u, win_c))
if win_c>win_u:
    print("Computer won this game.")
elif win_c<win_u:
    print("You won this game.")
else:
     print("Game draw.")
print("ThankYou for playing this game.")

    
