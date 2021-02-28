import sys


class Box:
    #Class defining the dimensions of the box and roll
    cubeWidth = 0.0
    rollWidth = 0.0

    def __init__(self, cDimensions, rDimensions):
        self.cubeWidth = cDimensions
        self.rollWidth = rDimensions

    def checkWaste(self):

        waste = 0
        rWidth = self.accessRoll()
        cWidth = self.accessCube()
        numBoxes = rWidth / cWidth
        if rWidth % netDimensions[0]:
            


    def accessCube(self):
        return self.cubeWidth

    def accessRoll(self):
        return self.rollWidth


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
