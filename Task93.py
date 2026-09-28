
#here we enter the value
x1, y1, a1, b1, x2, y2 = map(int, input().split())

#convert all times into minute
t1 = x1 * 60 + y1
t2 = x2 * 60 + y2
real1 = a1 * 60 + b1

#calculate how many minutes pass on the slow clock 
dt = (t2 - t1) % 1440

#because the clock runs twice as slow, so twice as much real time passes
real2 = (real1 + 2 * dt) % 1440

#print result
print(real2 // 60, real2 % 60)