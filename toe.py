print("----------------------------------------------")
print("welcome to tic tac toe")
print("----------------------------------------------")

def make_board():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    return board

def show_board(board):
    print(board[0][0], "|", board[0][1], "|", board[0][2])
    print("-----------")
    print(board[1][0], "|", board[1][1], "|", board[1][2])
    print("-----------")
    print(board[2][0], "|", board[2][1], "|", board[2][2])

def get_move(board, player):
    print(player, "it is your turn.")
    row = int(input("enter the row (1-3): "))
    column = int(input("enter the column (1-3): "))

    while check_move(board, row - 1, column - 1) == False:
        print("invalid spot. try again.")
        row = int(input("enter the row (1-3): "))
        column = int(input("enter the column (1-3): "))

    return row - 1, column - 1

def check_move(board, row, column):
    if row < 0 or row > 2:
        return False

    if column < 0 or column > 2:
        return False

    if board[row][column] == " ":
        return True
    else:
        return False

def check_tie(board):
    for row in board:
        for space in row:
            if space == " ":
                return False

    return True

def check_win(board, symbol):
    for row in board:
        if row[0] == symbol and row[1] == symbol and row[2] == symbol:
            return True

    for column in range(3):
        if board[0][column] == symbol and board[1][column] == symbol and board[2][column] == symbol:
            return True

    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True

    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True

    return False

player1 = input("enter player 1's name: ")
player2 = input("enter player 2's name: ")

board = make_board()

player = player1
symbol = "x"

show_board(board)

while True:
    row, column = get_move(board, player)
    board[row][column] = symbol
    show_board(board)

    if check_win(board, symbol):
        print()
        print(player, "wins")
        print("omg how are you so good")
        break
    if check_tie(board):
        print()
        print("its a tie")
        print("nobody won you both suck")
        break
    if player == player1:
        player = player2
        symbol = "o"
    else:
        player = player1
        symbol = "x"

