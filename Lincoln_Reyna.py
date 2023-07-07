import math

def main():
    while True:
        print()
        print("Enter -1 to exit the calculator")
        print("Select an operation")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power\n6. Square Root")
        
        choice = eval(input("Enter your choice "))
        
        if choice == 1:
            num1 = eval(input("Enter the first number "))
            num2 = eval(input("Enter the second number "))
            solution = num1 + num2
            print(solution)
            
        elif choice == 2:
            num1 = eval(input("Enter the first number "))
            num2 = eval(input("Enter the second number "))
            solution = num1 - num2
            print(solution)
            
        elif choice == 3:
            num1 = eval(input("Enter the first number "))
            num2 = eval(input("Enter the second number "))
            solution = num1 * num2
            print(solution)
            
        elif choice == 4:
            num1 = eval(input("Enter the first number "))
            num2 = eval(input("Enter the second number "))
            solution = num1/num2
            print(solution)
            
        elif choice == 5:
            num1 = eval(input("Enter the first number "))
            num2 = eval(input("Enter the power"))
            solution = math.pow(num1, num2)
            print(solution)
            
        elif choice == 6:
            num1 = eval(input("Enter the first number "))
            solution = math.sqrt(num1)
            print(solution)
        
        elif choice == -1:
            quit()
    
        
        elif (choice < -1) | (choice > 6):
            print("Please enter a number 1- 6.")
main()


    
    