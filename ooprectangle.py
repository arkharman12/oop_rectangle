class Size(object):                                 #creating a class name Size and extending it from object
    def __init__(self, width=0, height=0):          #basically it inherts whatever is defined in object
        self.__width = width                        #object is more than an simple argument
        self.__height = height

    def setWidth(self, width):
        self.__width = width
                                                    #defining setters and getters functions for
    def getWidth(self):                             #width and Height and returning the value
        return self.__width                         #to use it later

    def setHeight(self, height):
        self.__height = height

    def getHeight(self):
        return self.__height

    width = property(fset = setWidth, fget = getWidth)
    height = property(fset = setHeight, fget = getHeight)

class Rectangle(Size):                                      #creating a  class name Rectangle with a single argument
    def __init__(self, width=0, height=0):                  #of Size that way I can use the value of Size in this new class
        Size.__init__(self, width, height)

    def getArea(self):
        return self.width * self.height                     #area of a rectangle is width * height

    def setArea(self, area):
        print("Area is something that cannot be set using a setter.")

    def getPerimeter(self):
        return 2 * (self.width + self.height)               #perimeter of a rectangle is 2 * (width + height)

    def setPerimeter(self, area):
        print("Perimeter is something that cannot be set using a setter.")

    area = property(fget = getArea, fset = setArea)
    perimeter = property(fget = getPerimeter, fset = setPerimeter)

    def getStats(self):
        print("width:      {}".format(self.width))
        print("height      {}".format(self.height))                     #defining a new function getStats with self
        print("area:       {}".format(self.area))                       #and printing the values for width, height,
        print("perimeter:  {}".format(self.perimeter))                  #perimeter and area

def main():
    print ("Rectangle a:")
    a = Rectangle(5, 7)
    print ("area:      {}".format(a.area))
    print ("perimeter: {}".format(a.perimeter))                         #the whole main function was given to us

    print ("")
    print ("Rectangle b:")
    b = Rectangle()
    b.width = 10
    b.height = 20
    print (b.getStats())
main()

