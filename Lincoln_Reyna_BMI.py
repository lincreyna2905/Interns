import math

def endScreen():
        calculation = input("Enter yes to do another calculation , enter no to quit (y or n) ")

        if calculation.find('y') != -1 :
            main()
            

        if calculation.find('n') != -1:
            quit()
            
        else:
            print()
            print("Please enter a valid response ")
            endScreen()



def main():
    
    while True:
        output = ["Your BMI is ", "You are ", "PLease enter a valid number"]
        print()
        print("This program calculates your body mass index(BMI)")

        height = eval(input("Enter your height in inches "))
        weight = eval(input("Enter your weight in pounds "))

        BMI = (weight/math.pow(height, 2) * 703) 
        formatted_BMI = "{:.1f}".format(BMI)


        if BMI < 18.5:
            print(output[0], formatted_BMI)
            print(output[1] + "underweight")

        elif (BMI >= 18.5) & (BMI <= 24.9):
            print(output[0], formatted_BMI)
            print(output[1] + " a normal weight")

        elif (BMI >= 25.0) & (BMI <= 29.9):
            print(output[0],  formatted_BMI)
            print(output[1] + " overweight")

        elif BMI >= 30:
            print(output[0], formatted_BMI)
            print(output[1] + " obese")
            
       

        endScreen()

main()
        
    

    
    