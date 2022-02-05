#Ask user for hourly wage, hours worked, overtime worked
wage = float(input("Enter the wage: $"))
hours = float(input("Enter the regular hours: "))
overtime = float(input("Enter the overtime hours: "))

#combine regular pay with time and a half
total = (hours * wage) + (wage * overtime * 1.5)

#return total pay
print("The total weekly pay is $%.2f" % total)
