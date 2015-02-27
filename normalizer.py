import sys
import numpy as np
import math

# Prototypes 
p0 = [3,2]
p1 = [3,4]
p2 = [5,4]
p3 = [5,6]

# Average Vector
m = [0, 0]
m[0] = ( p0[0] + p1[0] + p2[0] + p3[0] ) / 4
m[1] = ( p0[1] + p1[1] + p2[1] + p3[1] ) / 4

a = ( (m[0]-p0[0])**2 + (m[0]-p1[0])**2 + (m[0]-p2[0])**2 + (m[0]-p3[0])**2 ) / 4
a = math.sqrt(a)

b = ( (m[1]-p0[1])**2 + (m[1]-p1[1])**2 + (m[1]-p2[1])**2 + (m[1]-p3[1])**2 ) / 4
b = math.sqrt(b)

x0 = [0,0]
x1 = [0,0]
x2 = [0,0]
x3 = [0,0]

x0[0] = p0[0] / a 
x0[1] = p0[1] / b 

x1[0] = p1[0] / a 
x1[1] = p1[1] / b 

x2[0] = p2[0] / a 
x2[1] = p2[1] / b 

x3[0] = p3[0] / a 
x3[1] = p3[1] / b 

print x0
print x1
print x2
print x3
