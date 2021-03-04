import matplotlib.pyplot as plt
import numpy as np
import configure as cg


class handler:
    definition = cg.settings().graphDefinition
    range = cg.settings().graphRange

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
