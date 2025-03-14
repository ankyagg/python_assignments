#calculator
def switch_case(operand):
    match operand:
        case '+':
            print("Addition of a and b is: ",a+b)

        case '-':
            print("subtraction of a and b is: ",a-b)

        case '*':
            print("multiplication of a and b is: ",a*b)

        case '/':
            print("division of a and b is: ",a/b)


a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
operand = input("Enter the operator (+, -, *, /): ")
switch_case(operand)
