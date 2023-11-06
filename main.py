
def sum1(a, b, c):
    return a + b + c

def tie(board):
    f = 1
    for val in board:
        if val.isdigit():
            f=0
            break
        else:
            f=1
    if f == 1:
        print("its a tie")
    return f


def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    board = [{zero},{one},{two},{three},{four},{five},{six},{seven},{eight}]
    print(f"{zero} | {one} | {two}")
    print(f"--|---|---")
    print(f"{three} | {four} | {five}")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight}")
    val = tie(board)
    return val
    
def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum1(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X won the match")
            return 1
        if(sum1(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O won the match")
            return 0
    return -1

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for x and 0 for O
    print("Welcome to tic tac toe")
    while(True):
        val = printBoard(xState, zState)
        cwin = checkWin(xState, zState)
        if(cwin != -1 or val == 1):
            printBoard(xState,zState)
            print("Match over")
            break
        if(turn == 1):
            print("X's chance")
            value = int(input("please enter a value "))
            xState[value] = 1
        else:
            print("O's chance")
            value = int(input("please enter a value "))
            zState[value] = 1
        
        turn = 1-turn