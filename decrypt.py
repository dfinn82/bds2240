# Put your code here
cipher = input("Enter the coded text:")
dist = input("Enter the distance value:")

for x in cipher:
    print(chr(ord(x) - int(dist)),end="")
    
