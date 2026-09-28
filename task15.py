
#here we enter the value
feet = int(input("Feet:"))
inches = int(input("Inches:"))

#convert height to centimetres
height = feet * 30.48 + inches * 2.54

#print result
print("Your height is:", round(height), "cm.")
