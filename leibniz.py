#leibniz approximation of pi
#ask user for how many time to run the formula
i = input("Enter the number of iterations:")

#initialize denominator and output
x = 1
out = 0

for count in range(int(i)):
    #if we're on an even run subtract
    if (count + 1)%2 == 0:
        out -= 1/x
    #if odd add
    else:
        out += 1/x
    x += 2
print("The approximation of pi is " + str(out*4.0))
