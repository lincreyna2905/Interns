import math

def main():
    a = eval(input("Enter the value of a: "))
    b = eval(input("Enter the value of b: "))
    c = eval(input("Enter the value of c: "))

    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print() 
    print("The solutions are: ", root1, root2)

main()
