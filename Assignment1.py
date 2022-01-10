print('''Twinkle, twinkle, little star,
               How I wonder what you are!
                      Up above the world so high,
                      Like a diamond in the sky.
         Twinkle, twinkle, little star,
               How I wonder what you are!''')

import sys
print("python version")
print(sys.version)
print(sys.version_info)

import datetime
TodayDate = datetime.datetime.now()
print(TodayDate)

from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

fname = input("Amina : ")
lname = input("kiran : ")
print ("Hello  " + lname + " " + fname)

a=int(input("enter first number : "))
b=int(input("enter second number : "))
print("sum of",a, "and",b,"is",a+b)





