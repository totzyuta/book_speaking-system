import sys
import numpy as np

# Prototypes (Images of 0~4)
p0 = [0,1,1,1,0, 1,0,0,0,1, 1,0,0,0,1, 1,0,0,0,1, 0,1,1,1,0]
p1 = [0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0]
p2 = [0,1,1,1,1, 1,0,0,1,0, 0,0,1,0,0, 0,1,0,0,0, 1,1,1,1,1]
p3 = [0,1,1,1,0, 1,0,0,0,1, 0,0,1,1,0, 1,0,0,0,1, 0,1,1,1,0]
p4 = [0,0,1,0,0, 0,1,0,0,0, 1,0,0,1,0, 1,1,1,1,1, 0,0,0,1,0]

class Image:
  def __init__(self, image):
    self.image = image

  def draw(self):
    print("")
    print("Image:")
    print("")
    sys.stdout.write("     ")
    for i in range(len(self.image)):
      if (self.image[i]==1):
        sys.stdout.write("#")
      else:
        sys.stdout.write(" ")
      if ((i+1)%5==0):
        print("")
        sys.stdout.write("     ")
    print("")

  def classify(self):
    d0 = 0;
    for i in range(0,24):
      d0 += (p0[i]-self.image[i])**2
    d1 = 0;
    for i in range(0,24):
      d1 += (p1[i]-self.image[i])**2
    d2 = 0;
    for i in range(0,24):
      d2 += (p2[i]-self.image[i])**2
    d3 = 0;
    for i in range(0,24):
      d3 += (p3[i]-self.image[i])**2
    d4 = 0;
    for i in range(0,24):
      d4 += (p4[i]-self.image[i])**2

# print the distances
    # print(d0)
    # print(d1)
    # print(d2)
    # print(d3)
    # print(d4)

    x = np.array([d0, d1, d2, d3, d4])
    print("The number of image is %d" % np.argmin(x))

image1 = Image([0,0,0,1,0, 0,0,0,1,0, 0,0,0,1,0, 0,0,0,1,0, 0,0,0,1,0])
image1.draw()
image1.classify()
