import sys
print("BMI: Body Mass Index Calculator")
userWeight = input("Enter your weight in pounds: ")
userHeight = input("Enter your height in inches: ")

# myBMI = (703 * float(userWeight)) / (float(userHeight) * float(userheight))
myBMI = (703 * float(userWeight)) / (float(userHeight) ** 2)
myBMI = round(myBMI, 2)
print("Your body mass index (BMI) is " + str(myBMI) + "%")
