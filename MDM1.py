import sys
import configure as cg
#import wasteGraphs as wg


def calcWaste(cubeD, netD, rollW, rollL, orientation):
    print(cubeD, netD, rollW, rollL, orientation)
    if orientation:
        return (rollW * rollL) - ((netD[0] * cubeD) // rollW) * ((netD[1] * cubeD) // rollL) * (((netD[0] * cubeD) * (netD[1] * cubeD)) + (0.1 * cubeD * cubeD))
    else:
        return (rollW * rollL) - ((netD[1] * cubeD) // rollW) * ((netD[0] * cubeD) // rollL) * (((netD[0] * cubeD) * (netD[1] * cubeD)) + (0.1 * cubeD * cubeD))


class box:
    #Class defining the dimensions of the box and roll
    cubeWidth = 0.0
    rollWidth = 0.0
    rollLength = 0.0
    areaOfRoll = 0.0

    def __init__(self, cDimensions, rWidth, rLength):
        self.cubeWidth = float(cDimensions)
        self.rollWidth = float(rWidth)
        self.rollLength = float(rLength)
        self.areaOfRoll = float(self.rollLength * self.rollWidth)

    def accessCube(self):
        c = self.cubeWidth
        return c

    def accessRollW(self):
        rW = self.rollWidth
        return rW

    def accessRollL(self):
        rL = self.rollLength
        return rL

    def accessRollArea(self):
        rA = self.areaOfRoll
        return rA


class efficientNet(box):
    #Net dimensions defined with x-dimension followed by y dimension where the
    #tab is given width that is 10% of the side length L so that it scales with
    #size of the cube
    netDimensions = []

    def __init__(self, cDimensions, rWidth, rLength):
        box.__init__(self, cDimensions, rWidth, rLength)
        self.netDimensions = [2, 4]

    def accessNet(self):
        nD = self.netDimensions
        return nD

    def checkOrientation(self):
        #Retturns true if having the x-side agains the bottom of the roll
        #is most efficient if not returns false
        xWaste = (self.accessNet()[0] * self.accessCube()) % self.accessRollW()
        print(xWaste)
        yWaste = (self.accessNet()[1] * self.accessCube() + 0.1 * self.accessCube()) % self.accessRollW()
        print(yWaste)
        if xWaste <= yWaste:
            return True
        else:
            return False

    def checkWaste(self):
        orientation = self.checkOrientation()
        waste = calcWaste(self.accessCube(), self.accessNet(), self.accessRollW(), self.accessRollL(), orientation)
        return waste


def main(sysArgs):
    if len(sysArgs) == 2:
        b = efficientNet(sysArgs[0], sysArgs[1], cg.settings().accessRoll())
        print(b.checkWaste())
    else:
        print("ERORR: expected 2 inputs")


if __name__ == "__main__":
    #If ran from a shell or terminal then takes 2 system arguments
    arguments = sys.argv[1:]
    print(arguments)
    main(arguments)
else:
    #If ran from file then main is called after taking 2 user inputs
    rWidth = float(input("Enter a value for the length of the roll: "))
    cWidth = float(input("Enter a value for the dimensions of the cube:"))
    args = [rWidth, cWidth]
    main(args)
