# area of triangle with 3 sides
import math

a=int(input("enter the side a: "))
b=int(input("eneter the side b:"))
c=int(input("enter the side c :"))
s= (a+b+c)/2
area= math.sqrt((s*(s-a)*(s-b)*(s-c)))
print ("the area of the triangle is",area)
    