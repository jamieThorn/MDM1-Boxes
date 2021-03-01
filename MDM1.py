import sys


class box:
    #Class defining the dimensions of the box and roll
    cubeWidth = 0.0
    rollWidth = 0.0
    rollLength = 0.0
    areaOfRoll = 0.0

    def __init__(self, cDimensions, rWidth, rLenght):
        self.cubeWidth = cDimensions
        self.rollWidth = rWidth
        self.rollLength = rLenght
        self.areaOfRoll = self.rollLength * self.rollWidth

    def accessCube(self):
        return self.cubeWidth

    def accessRollW(self):
        return self.rollWidth

    def accessRollL(self):
        return self.rollLength

    def accessRollArea(self):
        return self.areaOfRoll


class efficientNet(box):
    #Net dimensions defined with x-dimension followed by y dimension where the
    #tab is given width that is 10% of the side length L so that it scales with
    #size of the cube
    netDimensions = [2 * box.accessCube(), (4 * box.accessCube())]

    def accessNet(self):
        return self.netDimensions

    def checkOrientation(self):
        #Retturns true if having the x-side agains the bottom of the roll
        #is most efficient if not returns false
        xWaste = self.accessNet()[0] % box.accessRoll()
        yWaste = self.accessNet()[1] + 0.1 * box.accessCube() % box.accessRoll()
        if xWaste <= yWaste:
            return True
        else:
            return False

    def checkWaste(self):

        if self.checkWaste():
            waste = areaOfRoll - ((self.accessNet()[0] * self.accessNet()[1]) + (0.1 * box.accessCube() * box.accessCube())) + (self.accessNet()[0] % box.accessRoll() * box.accessRollL())
            return waste
        else:
            waste = areaOfRoll - ((self.accessNet()[0] * self.accessNet()[1]) + (0.1 * box.accessCube() * box.accessCube())) + (self.accessNet()[0] % box.accessRoll() * box.accessRollW())
            return waste


def main(sysArgs):
    if len(sysArgs) == 2:
        box(sysArgs[0], sysArgs[1])
    else:
        print("ERORR: expected 2 inputs")


if __name__ == "__main__":
    #If ran from a shell or terminal then takes 2 system arguments
    arguments = sys.argv[:1]
    main()
else:
    #If ran from file then main is called after taking 2 user inputs
    rWidth = float(input("Enter a value for the length of the roll: "))
    cWidth = float(input("Enter a value for the dimensions of the cube:"))
    args = [rWidth, cWidth]
    main(args)
