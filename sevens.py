#some sort of dice game where if you roll 7 you get $4, else you lose $1
import random

#ask user for how much they are betting
money = int(input("How many dollars do you have?"))

rolls = 0

#keep track of when user had most money
maxpot = [0,money]

#while money still remains roll dice
while money > 0:
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    if d1 + d2 == 7:
        money += 4
    else:
        money -= 1
    rolls += 1

    #set max winning and record which roll we're at
    if money > maxpot[1]:
        maxpot[0],maxpot[1] = rolls,money
print("You are broke after %d rolls." % (rolls))
print("You should have quit after %d rolls when you had $%d." % (maxpot[0],maxpot[1]))
