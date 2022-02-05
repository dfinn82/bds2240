#figure out if user entered a right triangle
first = int(input("Enter the first side: "))
second = int(input("Enter the second side: "))
third = int(input("Enter the third side: "))

#since we don't know which value is the hypotenuse we test all 3
f = first ** 2 == (second ** 2 + third ** 2)
s = second ** 2 == (first ** 2 + third ** 2)
t = third ** 2 == (first ** 2 + second ** 2)

#if any of the tests is true we have a right triangle
if f or s or t:
    print("The triangle is a right triangle")
else:
    print("The triangle is not a right triangle")

