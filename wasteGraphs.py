import matplotlib.pyplot as plt
import numpy as np
import configure as cg


class handler:
    #Graph definition is the ammount of values considered when plotting the graph
    definition = cg.settings().graphDefinition
    #Range is the values either side of the user input between which the graph is plotted
    range = cg.settings().graphRange

# Creates a graph comparing how waste varies as the cube length is altered
    def compareVariablebCube(self, func, Xval, constants):
        Xval = int(Xval)
        if (Xval - self.range) > 0:
            Xvals = np.linspace(Xval - self.range, Xval + self.range, num=self.definition)
        else:
            Xvals = np.linspace(0, Xval + self.range, num=self.definition)
        Yvals = []
        for each in Xvals:
            value = func(each, constants[0], constants[1], constants[2], constants[3])
            if value >= 0:
                Yvals.append(value)
            else:
                Yvals.append(0)
        plt.plot(Xvals, Yvals)
        plt.xlabel("Cube Length")
        plt.ylabel("Waste")
        plt.show()

# Creates a graph comparing how waste varies as the roll width is altered
    def compareVariableWidth(self, func, Xval, constants):
        Xval = int(Xval)
        if (Xval - self.range) > 0:
            Xvals = np.linspace(Xval - self.range, Xval + self.range, num=self.definition)
        else:
            Xvals = np.linspace(0, Xval + self.range, num=self.definition)
        Yvals = []
        for each in Xvals:
            value = func(constants[0], constants[1], each, constants[2], constants[3])
            if value >= 0:
                Yvals.append(value)
        plt.plot(Xvals, Yvals)
        plt.xlabel("Roll Width")
        plt.ylabel("Waste")
        plt.show()
