# Put your code here
i = input("Enter the number of iterations:")

x = 1
out = 0
for count in range(int(i)):
    if (count + 1)%2 == 0:
        out -= 1/x
    else:
        out += 1/x
    x += 2
print("The approximation of pi is " + str(out*4.0))
