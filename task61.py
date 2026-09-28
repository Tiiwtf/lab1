
#here we enter the value
t = int(input("Minutes:"))
h = int(input("Hour:"))
m = int(input("Minutes:"))

#convert hours in minutes
total = h * 60 + m + t

#print result
print("Need hours:", total // 60)
print("Need minutes:", total % 60)