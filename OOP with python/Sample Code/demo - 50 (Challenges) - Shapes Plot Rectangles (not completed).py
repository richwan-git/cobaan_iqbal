#=======================================================
# Additional challenges for faster students
# Plot out the rectangles using Matplotlib
#=======================================================

import matplotlib.pyplot as plt
import matplotlib.patches as patches

#=== Define Rectangle Class ===
class Rectangle:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def resize(self, factor):
        self.width = self.width * factor
        self.height = self.height * factor

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height

    def drawRectangle(self, fig):
        ax = fig.gca()
        p = patches.Rectangle((self.x, self.y),self.width, self.height)
        ax.add_patch(p)
        


#=== Main Program ===
fig = plt.figure()
plt.ylim(-50, 50)
plt.xlim(-50, 50)

smallRect = Rectangle(5, 10, 0, 0)
smallRect.drawRectangle(fig)

bigRect = Rectangle(2,2, 10, 10)
bigRect.drawRectangle(fig)

plt.show()
