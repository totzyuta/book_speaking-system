import sys
import numpy as np
import math
from matplotlib import pyplot as plt

p = [[0,0]] * 4

# Prototype Vectors 
p[0] = [3,2]
p[1] = [3,4]
p[2] = [5,4]
p[3] = [5,6]

# Normalized Vectors
x = [[0,0]] * 4
for i in range(0,4):
    x[i] = [0,0]


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


class Vector:
    def __init__(self, vector):
        self.vector = vector

    def show(self):
        print self.vector

    def normalize(self):
        print "normalizing..."
# Average Vector
        m = [0, 0]
        m[0] = ( self.vector[0][0] + self.vector[1][0] + self.vector[2][0] + self.vector[3][0] ) / 4
        m[1] = ( self.vector[0][1] + self.vector[1][1] + self.vector[2][1] + self.vector[3][1] ) / 4

        a = ( (m[0]-self.vector[0][0])**2 + (m[0]-self.vector[1][0])**2 + (m[0]-self.vector[2][0])**2 + (m[0]-self.vector[3][0])**2 ) / 4
        a = math.sqrt(a)

        b = ( (m[1]-self.vector[0][1])**2 + (m[1]-self.vector[1][1])**2 + (m[1]-self.vector[2][1])**2 + (m[1]-self.vector[3][1])**2 ) / 4
        b = math.sqrt(b)

# Normalized Vectors
        x = [[0,0]] * 4
        for i in range(0,4):
            x[i] = [0,0]

        x[0][0] = self.vector[0][0] / a 
        x[0][1] = self.vector[0][1] / b 

        x[1][0] = self.vector[1][0] / a 
        x[1][1] = self.vector[1][1] / b 

        x[2][0] = self.vector[2][0] / a 
        x[2][1] = self.vector[2][1] / b 

        x[3][0] = self.vector[3][0] / a 
        x[3][1] = self.vector[3][1] / b 

        return x

    def plot(self):
        print "ploting..."

        p = self.vector
        x = self.normalize()

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
        plt.xlim(0,12)
        plt.ylim(0,12)
        plt.plot(px, py, "ro", label='vector')
        plt.plot(xx, xy, "go", label='Normalized')
        plt.legend()

        plt.show()
