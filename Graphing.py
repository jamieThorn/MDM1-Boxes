import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# General graph. R increases and L remains at a fixed value
# X represents R/L
# Y represents proportion of waste between 0 and 1
# =============================================================================

# Creates a numpy array with arbitrary value 1 for L and range of 2 to 100 for R

def WasteGraph():
    L = 1
    R = range(2,101)


    R = np.array(R)

# X = R/L is same as R but for clarity's sake


    X = R/L

# Creates value for maximum number of horizontal templates roll width R
# can print: NoT

    NoT = R//(L*2)




# Y calculates waste as a proportion of overall used cardboard i.e wasted
# cardboard/ used cardboard


    Y = (0.1 + (4.1*(R%2)))/((8.2*NoT)+(4.1*(R%2)))


# Creates a plot with a long x axis and small y axis

    Graph = plt.figure(figsize = (20,2))
    Graph = Graph.add_subplot(111)
    Graph.plot(X,Y)

# labels


    plt.xlabel("R/L")
    plt.ylabel("Proportion of Waste")
    plt.xlim(2,100)
    plt.show()
    
WasteGraph()