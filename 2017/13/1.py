

class FirewallLayer:
    def __init__(self, lenght = 0):
        self._lenght = lenght
        self._goingDown = True
        self._currIndex = 0

    def setLenght(lenght):
        self._lenght = lenght

    def move(self):
        if self._lenght == 0:
            return

        self._currIndex += 1 if self._goingDown else -1
        if self._currIndex == 0 or self._currIndex == self._lenght - 1:
            self._goingDown = not(self._goingDown)

    def getCurrIndex(self):
        return -1 if self._lenght == 0 else self._currIndex

    def getLenght(self):
        return self._lenght

    def reset(self):
        self._currIndex = 0
        self._goingDown = True

input = open('input').readlines()
lenghts = {}

for l in input:
    data = l.strip().split(': ')
    lenghts[int(data[0])] = int(data[1])

layers = [None] * (max(lenghts.keys()) + 1)

for i in range(len(layers)):
    layers[i] = FirewallLayer(lenghts[i] if i in lenghts else 0)


def moveAllLayers():
    for layer in layers:
        layer.move()

caught = True
nbOfSecondsToWait = -1

while caught:
    caught = False
    nbOfSecondsToWait+=1

    for i in range(nbOfSecondsToWait):
        moveAllLayers()

    for i in range(len(layers)):
        if layers[i].getCurrIndex() == 0:
            caught = True
            break

        moveAllLayers()

    for layer in layers:
        layer.reset()

    print nbOfSecondsToWait

print nbOfSecondsToWait
