'''
Problem Statement:
Write a program to calculate the distance between two points.	
'''

#getting input for the x and y coordinates for the points, and typecasting the values.
x1= int(input("x1:"))
y1= int(input("y1:"))
x2= int(input("x2:"))
y2= int(input("y2:"))

#calculating the distance.
distance= (((x2 - x1)**2) + ((y2 -y1)**2)) ** 0.5


#output
print("The distance between the two points is {}". format (distance))




