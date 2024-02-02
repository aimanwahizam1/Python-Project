# ---------------------------------------------------------------------------- #
#                                  Question 1                                  #
# ---------------------------------------------------------------------------- #

# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1x, self.coor1y = coor1
        self.coor2x, self.coor2y = coor2
    
    def distance(self):
        x_displacement = self.coor2x - self.coor1x
        y_displacement = self.coor2y - self.coor1y

        return (((x_displacement)**2) + ((y_displacement)**2))**0.5
    
    def slope(self):
        return (self.coor2y-self.coor1y)/(self.coor2x-self.coor1x)
    
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())
print(li.slope())

# ---------------------------------------------------------------------------- #
#                                  Question 2                                  #
# ---------------------------------------------------------------------------- #

# Fill in the class

class Cylinder:

    pi = 3.14
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return Cylinder.pi * (self.radius**2) * self.height
    
    def surface_area(self):
        return (2 * Cylinder.pi * self.radius * self.height) + (2 * Cylinder.pi * (self.radius**2))
    
c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())