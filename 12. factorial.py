#factorial calculator

Num = int(input("Enter the no. to be calculated for factorial: "))
factorial = 1
for i in range(Num,0,-1):
    factorial = factorial * i
    
print(f"The factorial of {Num} is",factorial)


