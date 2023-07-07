import math

def Addition(num1, num2):
    return num1 + num2

def Subtraction(num1, num2):
    return num1 - num2

def Division(num1, num2):
    return num1/num2

def Multiplication(num1, num2):
    return num1 * num2

def Power(num1, num2):
    return math.pow(num1,num2)

def SquareRoot(num1):
    return math.sqrt(num1)


def Calculator(operation, num1, num2):
    switcher = {
        '+': Addition(num1, num2),
        '-': Subtraction(num1, num2),
        '/': Division(num1, num2),
        '*': Multiplication(num1,num2),
        '^': Power(num1, num2),
        '2': SquareRoot(num1)
        
        
    }
    return switcher.get(operation, "nothing")
    
    
    
    
    
def main(): 
    
    print()
    print("Select an operation")
    print("+\n-\n*\n/\n^\n2")
    choice = (input("Enter your choice "))
    
    if choice.find('+') != -1:
        Calculator('+', 5, 7)
            
main()