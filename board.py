def create_board(w = 1):
    # create a classic 8*8 chess board in array format
    board = []
    for i in range(8):
        line = []
        for j in range(8):
            if (i + j + w) % 2 == 0:
                line.append({"box_color": "W", "piece": ""})
            else:
                line.append({"box_color": "B", "piece": ""})
        board.append(line)

    return board


def fill_board(board, positions, top_color='B'):

    # fill the chess board according to the input
    if top_color == 'B':
        bottom_color = 'W'
    elif top_color == 'W':
        bottom_color = 'B'

    for sp in positions:
        x = sp["position"][0]
        y = sp["position"][1]
        board[x][y]["piece"] = sp["piece"]
        if sp["piece"]["color"] == "":
            if sp["position"][1] == 0 or sp["position"][1] == 1:
                sp["piece"]["color"] = bottom_color
            else:
                sp["piece"]["color"] = top_color

    # print(board)
    return board
    