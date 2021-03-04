#configure.py

class settings:
    rollLength = 0.0
    graphDefinition = 0.0
    graphRange = 0.0

    def __init__(self):
        attributes = []
        with open("config.txt", mode='r', encoding='utf-8') as file:
            for line in file:
                currentAtr = line.strip("\n")
                currentAtr = currentAtr.split(" ")
                attributes.append(currentAtr[-1])
        self.rollLength = int(attributes[0])
        self.graphDefinition = int(attributes[1])
        self.graphRange = int(attributes[2])

    def accessRoll(self):
        rL = self.rollLength
        return rL
