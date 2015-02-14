import sys

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
    print("classify the image!")

image1 = Image([1,0,1,1,0,1,1,0,0,1,1,1,1,0,0,0,0,0,1,1,0,1,1,1,0])
image1.draw()
