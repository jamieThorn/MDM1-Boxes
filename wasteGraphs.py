import matplotlib
import numpy as np
plt = matplotlib.pyplot


class handler:

    def compareVariable(self, func, Xvals, constant, variableName):
        Yvals = []
        for each in Xvals:
            Yvals.append(func(Xvals, constant))
        plt.plot(Xvals, Yvals)
        plt.xlabel(variableName)
        plt.ylabel("Waste")
        plt.show()
