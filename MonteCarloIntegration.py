import time
import math
import numpy as np

def lcg(modulus, a, c, seed):
    while True:
        seed = (a * seed + c) % modulus
        yield seed

def next_power_of_2(x):
    return 1 if x == 0 else 2**math.ceil(math.log(x))

# Number of samples or Total number of points
n = 10**7 # takes 41 seconds

# modulus 
# Any Monte-Carlo simulation should use an LCG with a 
# modulus greater and preferably much greater than the cube 
# root of the number of random samples which are required. 
m = 2**next_power_of_2(n ** (1. / 3) * 4)


# the generator produces a uniform distribution of integers from 0  to m-1
myLCGx = lcg(m, 22695477, 1, int( time.time() * 1000.0 ))
myLCGy = lcg(m, 1103515245, 12345, int( time.time() * 8000.0 ))

X = []
Y = []
count = 0

for x in myLCGx:
	X.append(x/(m-1))
	count += 1
	if(count == n):
		break

count = 0
for y in myLCGy:
	Y.append(y/(m-1))
	count += 1
	if(count == n):
		break

# x and y should vary independtly
print(np.correlate(X,Y))

# To calculate pi
pointsInsideCircle = 0

def circle(x,y):
	if((x-0.5)**2+(y-0.5)**2<0.5**2):
		return True
	else:
		return False

for i in range(n):
	if(circle(X[i],Y[i])):
		pointsInsideCircle += 1

# 4*pi*(0.5**2)/1**2
pi = 4*pointsInsideCircle/float(n)

print(pi)

# Using np to generate the random points
# n random points in 2d space are generated
pts = np.random.random((n,2))
print(np.correlate(pts[:,0],pts[:,1])) 

def circleNP(x,y):
	if((x-0.5)**2+(y-0.5)**2<0.5**2):
		return True
	else:
		return False


# To calculate pi
pointsInsideCircle = 0

for x,y in pts:
	if(circleNP(x,y)):
		pointsInsideCircle += 1


# 4*pi*(0.5**2)/1**2
pi = 4*pointsInsideCircle/float(n)

print(pi) # 3.14087 not better than 3.141816
# 3.14159265359