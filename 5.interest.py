print("WELCOME TO SIMPLE INTEREST CALCULATOR")
principal= int(input("Enter your principal amount: "))
rate=int(input("Enter the rate of interest: "))
time= int(input("Enter the amount of time (in years): "))

simple_interest = float((principal*rate*time)/100)

print("The total interest computed is", simple_interest)

print("so the total value payable is",principal+simple_interest)
