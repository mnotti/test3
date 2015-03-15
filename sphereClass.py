class Point3:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def computeDistanceSquared(self,point):
        distance = (((self.x - point.x)**2) + ((self.y - point.y)**2) + ((self.z - point.z)**2))
        return distance

def createCoordinates():
    f = open("points.txt", "r")
    contents = f.readlines()
    list = []
    listOfPoints = []

    
    for i in range(len(contents)):   
        contents[i] = contents[i].translate(None, "\",")
        list.extend(contents[i].split())
    f.close()
    for i in range(len(list)):
        if ((i+1)%3 == 1):
            listOfPoints.append(Point3(list[i], list[(i+1)], list[(i+2)]))
 

    for p in listOfPoints:
        print "x: %s y: %s z: %s" % (p.x, p.y, p.z)

def boundingSphere(pointsArray):
    i = 0
    center = Point3(1,1,1)
    distance = 0
    for p in pointsArray:
        if i == 0:
            print "center --- x: %s y: %s z: %s" % (p.x, p.y, p.z)
            i += 1
            center = p
        else:
            tempDis = center.computeDistanceSquared(p)
            if tempDis > distance:
                distance = tempDis
    print "radius = %d" % distance
            

p1 = Point3(0, 0, 0)
p2 = Point3(2, 2, 2)
distance = p1.computeDistanceSquared(p2)
print "distance is %d" % distance

createCoordinates()
p3 = Point3(3,3,3)
p4 = Point3(5,5,5)
p5 = Point3(2,2,2)
pointsList = [p1,p2,p3,p4,p5]
boundingSphere(pointsList)
