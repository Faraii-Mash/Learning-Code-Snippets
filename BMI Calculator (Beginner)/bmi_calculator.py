#This program calculates a person's BMI
weight = input("Please enter your Weight here (kgs): ")
height = input("Please enter your Height here (m): ")
#insert formula for BMI = (weight in kg) / ((height in m)*(height in m))
bmi_calculation = int(weight) / (int(height)**2)
#Print appropriate statement according to requirements
if bmi_calculation >= 30:
	print("User BMI is obese.")
elif bmi_calculation >=25:
	print("User BMI is overweight")
elif bmi_calculation >=18.5:
	print("User BMI is normal")
else:
	print("User BMI is underweight")
