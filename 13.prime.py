#to check if a no. is prime

number = int(input("Enter the no. to be checked for prime: "))
if (number==2):
    print("Is a prime no.")
elif (number%2==0):
    print("Is not a prime no.")
else:
    print("Is a prime no.")
