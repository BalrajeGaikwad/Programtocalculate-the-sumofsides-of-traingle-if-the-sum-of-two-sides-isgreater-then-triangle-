"""
If the three sides of a triangle are entered through the keyboard, write a program to check whether the triangle is valid or not. 
The triangle is valid if the sum of two sides is greater than the largest of the three sides.

"""

side1=float(int(input("Enter the side of triangle :- ")))
side2=float(int(input("Enter the side of triangle :- ")))
side3=float(int(input("Enter the side of triangle :- ")))

largest=max(side1, side2, side3)
print("largest side is",largest)

sum_two_sides=side1+side2+side3-largest
print("sum_two_sides is :- ",sum_two_sides)

if(sum_two_sides>largest):
    print("Triangle is valid :-")
else:
    print("triangle is not valid ")