#    13. BMI Calculator
height = float(input("Enter Height in Cm:"))
weight = float(input("Enter Weight in Kg:"))
bmi = (weight/(height/100)**2)
print("Your BMI is",bmi)