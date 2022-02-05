# Put your code here
wage = float(input("Enter the wage: $"))
hours = float(input("Enter the regular hours: "))
overtime = float(input("Enter the overtime hours: "))

total = (hours * wage) + (wage * overtime * 1.5)

print("The total weekly pay is $%.2f" % total)
