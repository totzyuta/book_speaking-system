import sys
import numpy as np

# Prototypes (Images of 0~4)
p0 = [0,1,1,1,0, 1,0,0,0,1, 1,0,0,0,1, 1,0,0,0,1, 0,1,1,1,0]
p1 = [0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0]
p2 = [0,1,1,1,1, 1,0,0,1,0, 0,0,1,0,0, 0,1,0,0,0, 1,1,1,1,1]
p3 = [0,1,1,1,0, 1,0,0,0,1, 0,0,1,1,0, 1,0,0,0,1, 0,1,1,1,0]
p4 = [0,0,1,0,0, 0,1,0,0,0, 1,0,0,1,0, 1,1,1,1,1, 0,0,0,1,0]
p5 = [1,1,1,1,1, 1,0,0,0,0, 1,1,1,1,1, 0,0,0,0,1, 1,1,1,1,1]
p6 = [1,0,0,0,0, 1,0,0,0,0, 1,1,1,1,1, 1,0,0,0,1, 1,1,1,1,1]
p7 = [1,1,1,1,1, 1,0,0,0,1, 0,0,0,0,1, 0,0,0,0,1, 0,0,0,0,1]
p8 = [1,1,1,1,1, 1,0,0,0,1, 1,1,1,1,1, 1,0,0,0,1, 1,1,1,1,1]
p9 = [1,1,1,1,1, 1,0,0,0,1, 1,1,1,1,1, 0,0,0,0,1, 0,0,0,0,1]

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

  def calcd(self, another_image):
      d = 0
      for i in range(0,24):
          d += (self.image[i]-another_image.image[i])**2
      print("Distance: ") 
      print(d) 

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
    d5 = 0;
    for i in range(0,24):
      d5 += (p5[i]-self.image[i])**2
    d6 = 0;
    for i in range(0,24):
      d6 += (p6[i]-self.image[i])**2
    d7 = 0;
    for i in range(0,24):
      d7 += (p7[i]-self.image[i])**2
    d8 = 0;
    for i in range(0,24):
      d8 += (p8[i]-self.image[i])**2
    d9 = 0;
    for i in range(0,24):
      d9 += (p9[i]-self.image[i])**2

# print the distances
    print("Distance")
    print(d0)
    print(d1)
    print(d2)
    print(d3)
    print(d4)
    print(d5)
    print(d6)
    print(d7)
    print(d8)
    print(d9)
    print("")

    x = np.array([d0, d1, d2, d3, d4, d5, d6, d7, d8, d9])
    print("The number of image is %d" % np.argmin(x))

# Sample Image Instance
image1 = Image([0,0,0,1,0, 0,0,0,1,0, 0,0,0,1,0, 0,0,0,1,0, 0,0,0,1,0])
image1.draw()
image1.classify()

# Create incetance or prototype images
imagep0 = Image(p0)
imagep1 = Image(p1)
imagep2 = Image(p2)
imagep3 = Image(p3)
imagep4 = Image(p4)
imagep5 = Image(p5)
imagep6 = Image(p6)
imagep7 = Image(p7)
imagep8 = Image(p8)
imagep9 = Image(p9)
