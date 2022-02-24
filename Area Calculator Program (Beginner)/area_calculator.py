#This program will be used to calculate the area that the foundation of a building covers
Buildingshapeinput = input("What type of shape is it (square, rectangular or round): ")
#Switch input to lower case for accuracy  
BuildingShape = Buildingshapeinput.lower()
#Create if to calculate area of square
#import math to calculate pi
import math
if BuildingShape == "square":
	length = input("Please input length of Square: ")
	areaofSquare = int(length) ** 2 
	print("The area of the square is: " +  str(areaofSquare))
#Create elif to calculate area of a rectangle 
elif BuildingShape == "rectangular":
	length = input("Please input length of Rectangle: ")
	width = input("Please input width of Rectangle: ")
	areaofRectangle = int(length) * int(width)
	print("The area of the rectangle is: " +  str(areaofRectangle))
#Create else to calculate area of a circle 
elif BuildingShape == "round":
	radius = input("Please input radius of Circle: ")
	areaofCircle = math.pi * (int(radius) ** 2)
	print("areaofCircle is: " + str(areaofCircle))
