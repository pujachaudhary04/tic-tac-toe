from Game import feature1, feature2, feature3

from random import shuffle

featureRange = [x for x in range(7)]
w = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

def displayBoard(board):
    print("\n")
    print(board[1] + " | " + board[2] + " | " + board[3] + "     1 | 2 | 3")
    print('---------     ---------')
    print(board[4] + " | " + board[5] + " | " + board[6] + "     4 | 5 | 6")
    print('---------     ---------')
    print(board[7] + " | " + board[8] + " | " + board[9] + "     7 | 8 | 9")
    print("\n")

def startMove(state):
        #print("state...", state)
        maximumValue = -100
        move = 0
        commonValues = []
        for i in range(9):
            if ord(state[i]) >= 49 and ord(state[i]) <= 57:
                temp = list(state)
                temp[i] = 'X'
                temp = ''.join(temp)
                v = vCapp(temp)
                if maximumValue < v:
                    maximumValue = v
                    commonValues = []
                    commonValues.append(i)
                    move = i
                elif maximumValue == v:
                    commonValues.append(i)

            shuffle(commonValues)
            move = commonValues[0] if commonValues else 0
        return move

def vCapp(boardstate):
    featureRange[0] = 1

    featureRange[1], featureRange[2] = feature1(boardstate)  # featureRange 1 is # of 'x' & featureRange 2 to is # of 'o'
    featureRange[3], featureRange[4] = feature2(boardstate)  # featureRange 3 is # of two 'x' per row & featureRange 4 to is # of two 'o' per row
    featureRange[5], featureRange[6] = feature3(boardstate)  # featureRange 5 is # of three 'x' & featureRange 6 to is # of three 'o' per row
    vHat = 0
    for i in range(6):
        vHat = vHat + w[i] * featureRange[i];
    return vHat
