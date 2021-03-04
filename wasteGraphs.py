import matplotlib
import numpy as np
plt = matplotlib.pyplot


class handler:
    definition = 0.0
    range = 0.0

    def __init__(self, gDef, gRange):
        self.definition = gDef
        self.range = gRange

    def generate(cube):
        
    def compareVariable(self, func, Xvals, constant, variableName):
        Yvals = []
        for each in Xvals:
            Yvals.append(func(Xvals, constant))
        plt.plot(Xvals, Yvals)
        plt.xlabel(variableName)
        plt.ylabel("Waste")
        plt.show()
