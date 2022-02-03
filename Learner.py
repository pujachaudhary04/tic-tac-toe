from random import shuffle

from Game import feature3, checkIfWon
from Player import vCapp, featureRange, startMove
from experience import create_x_and_0_data

playUntil = 0
nextFlag = True

xwin = 0
owin = 0
tiematch = 0
initialState = '123456789'
w = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
gameSequence = []
learningRate = 0.01

board = [' ' for x in range(10)]



def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'O\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if checkIfBlank(move):
                    run = False
                    inputWithPosition('O', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def inputWithPosition(letter, pos):
    board[pos] = letter


def checkIfBlank(pos):
    return board[pos] == ' '




def readStates():
    filename = "board_input.txt"  # Reading the input file
    fp = open(filename, "r")
    while True:
        line = fp.readline()
        if line == "":
            break
        line_split = line.split('\n')  # Splitting each line
        for i in line_split:
            if i == "":
                break
            state = (i.split(' '))  # Splitting each board input
            gameSequence.append(state)
    fp.close()

def checkStart(boardinput):

        x, o = feature3(boardinput)  # Feature 5 is # of three 'x' & Feature 6 to is # of three 'o' per row
        target = 1 if x > o else 2
        return target

def winCheck(boardinput):
        global xwin ,owin,tiematch
        x_Win, o_Win = feature3(boardinput)  # Feature 5 is # of three 'x' & Feature 6 to is # of three 'o' per row
        xwin += x_Win
        owin += o_Win
        target = 100 if x_Win > 0 else -100 if o_Win > 0 else 0
        if target == 0:
            tiematch += 1
        return target

def calculateweights(game):

        global learningRate
        for row in range(len(game)):
            index = len(game[row]) - 1  # Calculating weights from the final board state
            start = checkStart(game[row][index])
            v_Train = winCheck(game[row][index])  # getting the Vtrain value based on the win status of the game
            index = len(game[row]) - start
            while index > -1:
                boardinput = game[row][index]
                for i in range(6):
                    vhat = vCapp(boardinput)  # Calculating the vhat for the current board state
                    w[i] += (learningRate * (v_Train - vhat) * featureRange[i])  # updating the weights
                v_Train = vhat  # Updating the V_train value with the Vhat for the next best move
                index -= 2


def possibleStep():
    possible_Moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    for let in ['X', 'O']:
        for i in possible_Moves:
            board_Copy = board[:]
            board_Copy[i] = let
            if checkIfWon(board_Copy, let):
                move = i
                print("moves...to..be..taken..",move)
                return move


def validate_move():
    possible_Moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    #print("possibale move ..",possibleMoves)

    for let in ['X', 'O']:
        for i in possible_Moves:
            board_Copy = board[:]
            board_Copy[i] = let
            if checkIfWon(board_Copy, let):
                move = i
                return move

    cornersOpen = []
    for i in possible_Moves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possible_Moves:
        move = 5
        return move

    edgesOpen = []
    for i in possible_Moves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move



def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def checkIsBoardNotEmpty(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print('Welcome to Tic Tac Toe!')
    from Player import displayBoard
    #displayBoard(board)
    global xwin
    global owin
    global tiematch

    #----------
    randomlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    shuffle(randomlist)  # Randomize the slot list
    state = initialState  # Reset board state

    index = 0
    toggle = 1
    sequence = []
    while not (checkIsBoardNotEmpty(board)):
        if not (checkIfWon(board, 'O')):
            move = validate_move()

            #move = startMove(state)

            print('Computer plays at', move)
            index += 1
            temp = list(state)
            player = 'O' if toggle % 2 == 1 else 'X'  # Toggle between x & o
            temp[move-1] = player  # marking an empty slot on the board
            state = ''.join(temp)
            #print("sequence",state)
            sequence.append(state)


            # print("winnwe",win)
            if move == 0:
                print('Tie Game!')
                tiematch += 1
            else:
                inputWithPosition('X', move)
                print('Computer placed an \'X\' in position', move, ':')
                displayBoard(board)
        else:
            xwin += 1
            print('X\'s won this time! Good Job!')
            break

        if not (checkIfWon(board, 'X')):
            if checkIsBoardNotEmpty(board):
                print('Tie Game!')
            else:
                playerMove()
                displayBoard(board)
        else:
            owin = + 1
            print('Sorry, X\'s won this time!')
            break

    #if checkIsBoardNotEmpty(board):
     #   print('Tie Game!')

def selectoption():

    global playUntil
    global nextFlag
    global board
    option = int(input("1. Teacher Mode\n2. Non Teacher mode\nOption:"))

    if option == 1:
        gameshouldwork = input('Enter number of time the game should work : ')
        playUntil = gameshouldwork
        spam = 0

        readStates()  # Reading games from the board_input.txt file
        calculateweights(gameSequence)
        weights = w
        print('\n', weights, '\n')
        printpercentage(gameSequence)

        while spam < int(playUntil):
            spam = spam + 1
            board = [' ' for x in range(10)]
            print("==============================")
            print("Playing game count ", spam)
            print("===============================")
            main()


    elif option == 2:
        gameshouldwork = input('Enter number of time the game should work : ')
        playUntil = gameshouldwork
        spam = 0
        #printwinningpercentage(int(playUntil))
        trainingData = create_x_and_0_data()
        #print(trainingData)
        calculateweights(trainingData)
        printpercentage(trainingData)
        print('\n', w, '\n')


        while spam < int(playUntil):
            spam = spam + 1
            board = [' ' for x in range(10)]
            print("==============================")
            print("Playing game count ",spam)
            print("===============================")
            main()


def printpercentage(game):
    global xwin
    global owin
    global tiematch


    print('Win percentage = ', 10 * xwin / len(game))
    print('Loss percentage = ', 10 * owin / len(game))
    print('Draw percentage = ', 100 * tiematch / len(game), '\n')


selectoption()