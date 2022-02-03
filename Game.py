# Feature evaluation for blocking two 'X's or two 'O's

winningCombination = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

def feature1(string):
    x = 0
    o = 0

    for item in winningCombination:
        # Feature 1 is one 'X' in the same row as two 'O'
        if (string[item[0] - 1] == 'O' and string[item[1] - 1] == 'O' and string[item[2] - 1] == 'X') or (
                string[item[0] - 1] == 'X' and string[item[1] - 1] == 'O' and string[item[2] - 1] == 'O') or (
                string[item[0] - 1] == 'O' and string[item[2] - 1] == 'X' and string[
            item[2] - 1] == 'O'):  # comparing combination of the boardstate with winning combination array
            x += 2

            # Feature 2 is one 'O' in the same row as two 'X'
        if (string[item[0] - 1] == 'X' and string[item[1] - 1] == 'X' and string[item[2] - 1] == 'O') or (
                string[item[0] - 1] == 'O' and string[item[1] - 1] == 'X' and string[item[2] - 1] == 'X') or (
                string[item[0] - 1] == 'X' and string[item[1] - 1] == 'O' and string[
            item[2] - 1] == 'X'):  # comparing combination of the boardstate with winning combination array
            o += 2
    return x, o

    # Feature evaluation for two 'X' & 'O' per row


def feature2(string):
    x = 0
    o = 0
    for item in winningCombination:
        if (string[item[0] - 1] == 'X' and string[item[1] - 1] == 'X') or (string[item[1] - 1] == 'X' and string[item[2] - 1] == 'X') or (
                string[item[0] - 1] == 'X' and string[
            item[2] - 1] == 'X'):  # comparing combination of the boardstate with winning combination array
            x += 0.2

        if (string[item[0] - 1] == 'O' and string[item[1] - 1] == 'O') or (string[item[1] - 1] == 'O' and string[item[2] - 1] == 'O') or (
                string[item[0] - 1] == 'O' and string[
            item[2] - 1] == 'O'):  # comparing combination of the boardstate with winning combination array
            o += 0.2;
    return x, o  # returns number of two 'X' & 'O' per row


# Feature evaluation for three 'X' & 'O' per row
def feature3(string):
    x = 0
    o = 0
    for item in winningCombination:
        if string[item[0] - 1] == 'X' and string[item[1] - 1] == 'X' and string[
            item[2] - 1] == 'X':  # comparing combination of the board with winning combination array
            x += 10

        if string[item[0] - 1] == 'O' and string[item[1] - 1] == 'O' and string[
            item[2] - 1] == 'O':  # comparing combination of the board with winning combination array
            o += 10;
    return x, o  # returns number of three 'X' & 'O' per row

def checkWin(index, state):
        x, o = feature3(state)
        result = True if x > 0 else True if o > 0 else False
        if index == 9:
            return True
        if result == False and index < 9:
            return False
        return result


def checkIfWon(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
                bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (
                       bo[2] == le and bo[5] == le and bo[8] == le) or (
                       bo[3] == le and bo[6] == le and bo[9] == le) or (
                       bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)
