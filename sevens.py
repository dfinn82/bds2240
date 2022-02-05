# Put your code here
import random
money = int(input("How many dollars do you have?"))

rolls = 0
maxpot = [0,money]
while money > 0:
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    if d1 + d2 == 7:
        money += 4
    else:
        money -= 1
    rolls += 1
    if money > maxpot[1]:
        maxpot[0],maxpot[1] = rolls,money
print("You are broke after %d rolls." % (rolls))
print("You should have quit after %d rolls when you had $%d." % (maxpot[0],maxpot[1]))
