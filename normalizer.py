import sys
import numpy as np
import math
from matplotlib import pyplot as plt

# sys.stdout.write("Input First Vector: ")
# p[0] = input()
# sys.stdout.write("Input Second Vector: ")
# p[1] = input()
# sys.stdout.write("Input Third Vector: ")
# p[2] = input()
# sys.stdout.write("Input Fourth Vector: ")
# p[3] = input()


# Prototype Vectors 
p = [[0,0]] * 4
p[0] = [3,2]
p[1] = [3,4]
p[2] = [5,4]
p[3] = [5,6]

print p[0]
print p[1]
print p[2]
print p[3]


# Average Vector
m = [0, 0]
m[0] = ( p[0][0] + p[1][0] + p[2][0] + p[3][0] ) / 4
m[1] = ( p[0][1] + p[1][1] + p[2][1] + p[3][1] ) / 4

a = ( (m[0]-p[0][0])**2 + (m[0]-p[1][0])**2 + (m[0]-p[2][0])**2 + (m[0]-p[3][0])**2 ) / 4
a = math.sqrt(a)

b = ( (m[1]-p[0][1])**2 + (m[1]-p[1][1])**2 + (m[1]-p[2][1])**2 + (m[1]-p[3][1])**2 ) / 4
b = math.sqrt(b)

# Normalized Vectors
x = [[0,0]] * 4
x[0] = [0,0]
x[1] = [0,0]
x[2] = [0,0]
x[3] = [0,0]

x[0][0] = p[0][0] / a 
x[0][1] = p[0][1] / b 

x[1][0] = p[1][0] / a 
x[1][1] = p[1][1] / b 

x[2][0] = p[2][0] / a 
x[2][1] = p[2][1] / b 

x[3][0] = p[3][0] / a 
x[3][1] = p[3][1] / b 

print x[0]
print x[1]
print x[2]
print x[3]

px = []
py = []
for i in range(0,4):
    px.append(p[i][0])

for i in range(0,4):
    py.append(p[i][1])

xx = []
xy = []
for i in range(0,4):
    xx.append(x[i][0])

for i in range(0,4):
    xy.append(x[i][1])

# plot 
plt.title('Vecotors / Normalized Vectors')
plt.xlabel('x[1]')
plt.ylabel('x[2]')
plt.xlim(0,8)
plt.ylim(0,8)
plt.plot(px, py, "ro", label='vector')
plt.plot(xx, xy, "go", label='Normalized')
# plt.plot(virginica_sepal_length, virginica_sepal_width, "bo", label='virginica')
plt.legend()

plt.show()
