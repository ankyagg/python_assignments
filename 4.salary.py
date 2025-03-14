#to calculate gross salary of an employee

BS = float(input("Enter your base salary :"))

print("You entered your base salary as ", BS)

DA = 0.7*BS

print("DA=", DA)

TA = 0.3*BS

print("TA=", TA)

HRA = 0.1*BS

print("HRA=",HRA)

gross_salary = BS + DA + TA + HRA

print("Your gross salary comes out to be", gross_salary)