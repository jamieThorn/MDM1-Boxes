import sys
import configure as cg
import wasteGraphs


# Calculates overall waste by finding the area of unused roll and dividing this
# by the overall area of roll used

def calcWaste(cubeD, netD, rollW, rollL, orientation):
    areaOfRoll = rollL * rollW
    if orientation:
        usedArea = (rollW // (netD[0] * cubeD)) * (rollL // ((netD[1] * cubeD) + (0.1 * cubeD))) * (((netD[0] * cubeD) * (netD[1] * cubeD)) + (0.1 * cubeD * cubeD))
    else:
        usedArea = (rollW // ((netD[1] * cubeD) + (0.1 * cubeD))) * (rollL // (netD[0] * cubeD)) * (((netD[0] * cubeD) * (netD[1] * cubeD)) + (0.1 * cubeD * cubeD))
    return areaOfRoll - usedArea 


class box:
    #Class defining the dimensions of the box and roll
    cubeWidth = 0.0
    rollWidth = 0.0
    rollLength = 0.0
    areaOfRoll = 0.0

# Sets values for the cube's width and for the roll's dimensions and area

    def __init__(self, cDimensions, rWidth, rLength):
        self.cubeWidth = float(cDimensions)
        self.rollWidth = float(rWidth)
        self.rollLength = float(rLength)
        self.areaOfRoll = float(self.rollLength * self.rollWidth)

# Functions for accessing the previously mentioned values

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

# Initialises the class and takes the dimensions of the net in a list

    def __init__(self, cDimensions, rWidth, rLength):
        box.__init__(self, cDimensions, rWidth, rLength)
        self.netDimensions = [2, 4]

# Accesses the net dimensions

    def accessNet(self):
        nD = self.netDimensions
        return nD

# Checks to see whether the wasted cardboard is greater if the net is vertical
# Or horizontal by comparing which net orientation has a greater waste. If true,
# The horizontal has less waste. If false, the vertical has less waste

    def checkOrientation(self):
        #Retturns true if having the x-side agains the bottom of the roll
        #is most efficient if not returns false
        xWaste = (self.accessNet()[0] * self.accessCube()) % self.accessRollW()
        yWaste = (self.accessNet()[1] * self.accessCube() + 0.1 * self.accessCube()) % self.accessRollW()
        if xWaste >= yWaste:
            return True
        else:
            return False

# Calculates the waste of the orientation found to be most efficient

    def checkWaste(self):
        orientation = self.checkOrientation()
        waste = calcWaste(self.accessCube(), self.accessNet(), self.accessRollW(), self.accessRollL(), orientation)
        return waste
# Uses the wasteGraphs scipt to generate graphs showing why the user may
# wish to alter there cube size or rollw Width
    def displayGraphs(self):
        h = wasteGraphs.handler()
        orientation = self.checkOrientation()
        cubeGraphConstants = [self.accessNet(), self.accessRollW(), self.accessRollL(), orientation]
        rollWidthGraphConstants = [self.accessCube(), self.accessNet(), self.accessRollL(), orientation]
        h.compareVariablebCube(calcWaste, self.accessCube(), cubeGraphConstants)
        h.compareVariableWidth(calcWaste, self.accessRollW(), rollWidthGraphConstants)

# Checks that 2 inputs are inputted and calculates and prints the wasted
# cardboard and shows graphs of what happens as the cube and roll values vary

def main(sysArgs):
    if len(sysArgs) == 2:
        b = efficientNet(sysArgs[0], sysArgs[1], cg.settings().accessRoll())
        print(b.checkWaste())
        b.displayGraphs()
    else:
        print("ERORR: expected 2 inputs")


if __name__ == "__main__":
    #If ran from a shell or terminal then takes 2 system arguments
    arguments = sys.argv[1:]
    print(arguments)
    main(arguments)
