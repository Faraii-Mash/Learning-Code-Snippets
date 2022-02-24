#Leap Year Program 
#Initialize variables for year and number of years
year_input = int(input("Please enter a year to start with: "))
number_years = int(input("Please enter how many years ahead to calculate: "))

#For function with range of start year plus the number of years
for num in range(number_years):
	if year_input % 4 == 0:
		print(str(year_input) + " is a leap year")
	else:
		print(str(year_input) + " is not a leap year")
	year_input += 1
