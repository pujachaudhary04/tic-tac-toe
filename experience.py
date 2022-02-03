from random import shuffle

from Game import checkWin

featureRange = [x for x in range(7)]
testgame = []
initialState = '123456789'


def generateRandomStates(var):
    sequence = []
    state = initialState  # Reset board input
    winning = False
    index = 0
    randomlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    shuffle(randomlist)  # Randomize the slot list
    randomindex = 0
    toggle = var  # setting player 1
    while (winning == False and index < 9):
        toggle += 1
        pos = randomlist[randomindex]  # Enter into a random place
        randomindex += 1
        index += 1
        # print("state ",state)

        temp = list(state)
        player = 'X' if toggle % 2 == 0 else 'O'  # Toggle between x & o
        temp[pos - 1] = player  # marking an empty slot on the board
        state = ''.join(temp)
        sequence.append(state)
        winning = checkWin(index, state)  # Checking win or draw

        if winning == True:
            testgame.append(sequence)
            break


# Generate random states for Non teacher mode
def create_x_and_0_data():
    for _ in range(20):
        generateRandomStates(1)  # Generate 20 games for x
    for _ in range(20):
        generateRandomStates(2)  # Generate 20 games for o
    return testgame
