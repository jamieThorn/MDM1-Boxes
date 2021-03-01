import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# General graph. R increases and L remains at a fixed value
# X represents R/L
# Y represents proportion of waste between 0 and 1
# =============================================================================
L = 1
R = range(2,101)


R = np.array(R)
print(R)

X = R/L

NoT = R//(L*2)

print(NoT)

print(R%2)



Y = (0.1 + (4.1*(R%2)))/((8.2*NoT)+(4.1*(R%2)))
print(Y)
Graph = plt.figure(figsize = (20,2))
ax = Graph.add_subplot(111)
ax.plot(X,Y)
plt.xlabel("R/L")
plt.ylabel("Proportion of Waste")
plt.xlim(2,100)
plt.show()