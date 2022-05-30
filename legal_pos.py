from operator import truediv
from turtle import ycor
from gs import gs,c_castle


def pawn(position,color,game_state):
    possible_moves = []
    if color == 'B':

        temp = []
        if position[1] > 0:

            if position[0] > 0:
                temp.append([position[0]-1,position[1]-1])
            if position[0] < 7:
                temp.append([position[0]+1,position[1]-1])
        possible_moves.append(temp)

        temp = []
        if position[1] == 6:
            for i in range(1,3):
                temp.append([position[0],position[1]-i])
        elif position[1] < 6:
            temp.append([position[0],position[1]-1])
        possible_moves.append(temp)
    
    
    if color == 'W':

        temp = []
        if position[1] < 7:

            if position[0] > 0:
                temp.append([position[0]-1,position[1]+1])
            if position[0] < 7:
                temp.append([position[0]+1,position[1]+1])
        possible_moves.append(temp)

        temp = []
        if position[1] == 1:
            for i in range(1,3):
                temp.append([position[0],position[1]+i])
        elif position[1] > 1:
            temp.append([position[0],position[1]+1])
        possible_moves.append(temp)


    for x in range(8):
        for y in range(8):
            if game_state[x][y]['piece']:
                for a in possible_moves[0]:
                    # print(a)
                    if game_state[x][y]['piece']['color'] == color:
                        if [x,y] == a or game_state[a[0]][a[1]]['piece'] == '':
                            possible_moves[0].remove(a)
                for f in possible_moves[1]:
                    if [x,y] == f:
                            ind = possible_moves[1].index(f)
                            while len(possible_moves[1]) > ind:
                                possible_moves[1].pop()
    final = []
    for i in possible_moves:
        for j in i:
            final.append(j)
    return final

# print(pawn([2,1],'W'))

def rook(position,color,game_state):
    possible_moves = []

    # up
    temp = []
    for i in range(1,7-position[1]+1):
        temp.append([position[0],position[1]+i])
    possible_moves.append(temp)
    
    
    # down
    temp = []
    for i in range(position[1]):
        temp.append([position[0],position[1]-1-i])
    possible_moves.append(temp)

    # left
    temp = []
    for i in range(position[0]):
        temp.append([position[0]-1-i,position[1]])
    possible_moves.append(temp)

    # right
    temp = []
    for i in range(1,7-position[0]+1):
        temp.append([position[0]+i,position[1]])
    possible_moves.append(temp)



    for x in range(8):
        for y in range(8):
            if game_state[x][y]['piece']:
                for i in possible_moves:
                    for j in i:
                        if j == [x,y]:
                            if game_state[x][y]['piece']['color'] == color:
                                a = 0
                            else:
                                a = 1
                            ind = i.index(j)
                            while len(i) > ind+a:
                                i.pop()
    final = []
    for i in possible_moves:
        for j in i:
            final.append(j)
    return final
# print(rook([5,1],'B'))


def bishop(position,color,game_state):
    possible_moves = []

    # top left
    temp = []
    if position[0] < 7 - position[1]:
        tl = position[0]
    else:
        tl = 7 - position[1]
    for i in range(1,tl+1):
        temp.append([position[0]-i,position[1]+i])
    possible_moves.append(temp)


    # top right
    temp = []
    if 7 - position[0] < 7 - position[1]:
        tl = 7 - position[0]
    else:
        tl = 7 - position[1]
    for i in range(1,tl+1):
        temp.append([position[0]+i,position[1]+i])
    possible_moves.append(temp)


    # bottom left
    temp = []
    if position[0] < position[1]:
        tl = position[0]
    else:
        tl = position[1]
    for i in range(1,tl+1):
        temp.append([position[0]-i,position[1]-i])
    possible_moves.append(temp)


    # bottom right
    temp = []
    if 7 - position[0] < position[1]:
        tl = 7 - position[0]
    else:
        tl = position[1]
    for i in range(1,tl+1):
        temp.append([position[0]+i,position[1]-i])
    possible_moves.append(temp)



    for x in range(8):
        for y in range(8):
            if game_state[x][y]['piece']:
                for i in possible_moves:
                    for j in i:
                        if j == [x,y]:
                            if game_state[x][y]['piece']['color'] == color:
                                a = 0
                            else:
                                a = 1
                            ind = i.index(j)
                            while len(i) > ind+a:
                                i.pop()
                            
    final = []
    for i in possible_moves:
        for j in i:
            final.append(j)
    return final

# print(bishop([4,3],'W'))

def queen(position,color,game_state):
    possible_moves = []
    diagonals = bishop(position,color,game_state)
    straights = rook(position,color,game_state)

    for i in straights:
        possible_moves.append(i)
    for i in diagonals:
        possible_moves.append(i)

    return possible_moves

# print(queen([4,4],'W'))

def king(position,color,game_state):
    possible_moves = []

    for i in range(3):
        for j in range(3):

            if i < 1:
                x_sign = 0
            elif i == 1:
                x_sign = 1
            else:
                x_sign = -1


            if j < 1:
                y_sign = 0
            elif j == 1:
                y_sign = 1
            else:
                y_sign = -1
            
            possible_moves.append([position[0]+x_sign,position[1]+y_sign])
    # print(possible_moves)

    for x in range(8):
        for y in range(8):
            if game_state[x][y]['piece']:
                for i in possible_moves:
                    if i == [x,y]:
                        if game_state[x][y]['piece']['color'] == color:
                            possible_moves.remove(i)
    final = []
    for i in possible_moves:
        final.append(i)
    for i in possible_moves:
        if i[0] > 7 or i[0] < 0 or i[1] > 7 or i[1] < 0:
            final.remove(i)
        elif position == i:
            final.remove(i)

    
    return final

# print(king([4,7],'W'))

def knight(position,color,game_state):
    possible_moves = []

    for i in range(2):
        if i % 2 == 0:
            d1 = 1
            d2 = 2
        else:
            d1 = 2
            d2 = 1
        for j in range(2):
            if j % 2 == 0:
                s1 = 1
            else:
                s1 = -1
            for k in range(2):
                if k % 2 == 0:
                    s2 = 1
                else:
                    s2 = -1
                possible_moves.append([position[0]+d1*s1,position[1]+d2*s2])
    
    for x in range(8):
        for y in range(8):
            if game_state[x][y]['piece']:
                for j in possible_moves:   
                    if j == [x,y]:
                        if game_state[x][y]['piece']['color'] == color:
                            possible_moves.remove(j)
    final = []
    for i in possible_moves:
        final.append(i)
    for i in possible_moves:
        if i[0] > 7 or i[0] < 0 or i[1] > 7 or i[1] < 0:
            final.remove(i)
    return final

# print(knight([1,1],'W'))


def stg1_legal_pos(piece,position,color,game_state):

    if piece == 'p':
        all_pos = pawn(position,color,game_state)
    elif piece == 'r':
        all_pos = rook(position,color,game_state)
    elif piece == 'b':
        all_pos = bishop(position,color,game_state)
    elif piece == 'q':
        all_pos = queen(position,color,game_state)
    elif piece == 'k':
        all_pos = king(position,color,game_state)
    elif piece == 'n':
        all_pos = knight(position,color,game_state)
    return all_pos


# can tell if anyone's in check in given game_state
def check(p='pos',game_state=gs):
    check_clr = ''
    check_pos = ''
    king_pos = []

    for x in range(8):
        for y in range(8):
            if game_state[x][y]['piece']:
                if game_state[x][y]['piece']['name'] == 'k':
                    king_pos.append({'color':game_state[x][y]['piece']['color'],'coords':[x,y]})

    for clr in ['W','B']:

        k = [None,None]

        for z in king_pos:
            if z['color'] == clr:
                k = z['coords']

        for x in range(8):
            for y in range(8):
                if game_state[x][y]['piece']:
                    piece = game_state[x][y]['piece']['name']
                    color = game_state[x][y]['piece']['color']

                    if color != clr:

                        all_pos = stg1_legal_pos(piece,[x,y],color,game_state)
                        for z in all_pos:
                            if z == k:
                                check_pos = z
                                check_clr = clr

    if p == 'pos':
        return check_pos
    else:
        return check_clr

def legal_pos(piece,position,color,turn,gs):

    all_pos = stg1_legal_pos(piece,position,color,gs)
    temp_pos = []
    for z in all_pos:
        temp_pos.append(z)
    for z in temp_pos:

        temp_gs = []
        for x in gs:
            line = []
            for y in x:
                box = {}
                bx_clr = y['box_color']
                temp_piece = y['piece']
                box = {'box_color':bx_clr,'piece':temp_piece}
                line.append(box)
            temp_gs.append(line)

        temp_gs[z[0]][z[1]]["piece"] = temp_gs[position[0]][position[1]]["piece"]
        temp_gs[position[0]][position[1]]["piece"] = ""
        
        chk = check('clr',temp_gs)

        if chk == turn:
            all_pos.remove(z)

    if piece == 'k':
        can_castle = castle(turn,gs)
        if can_castle[0]:

            all_pos.append([6,can_castle[2]])
        if can_castle[1]:

            all_pos.append([2,can_castle[2]])
    return all_pos

def if_checkmate(turn):
    total_pos = []
    for x in range(8):
        for y in range(8):
            piece = gs[x][y]['piece']
            if piece and piece['color'] == turn:
                temp = legal_pos(piece['name'],[x,y],piece['color'],turn,gs)
                if temp != []:
                    total_pos.append(temp)
    if total_pos == []:
        return True
    else:
        return False

# shows if a player can castle or not
def castle(turn,game_state):
    if turn == 'W':
        y_coord = 0
    else:
        y_coord = 7
    clr_castle = c_castle[turn]

    def temp(c,frm,to):
        if clr_castle[c] != 'm':
            for x in range(frm,to):
                if x != 4 and game_state[x][y_coord]['piece']:
                    return False

            chk = check('clr',game_state)
            if chk == turn:
                return False

            total_pos = []
            for x in range(8):
                for y in range(8):
                    piece = gs[x][y]['piece']
                    if piece and piece['color'] != turn:
                        temp = stg1_legal_pos(piece['name'],[x,y],piece['color'],gs)
                        if temp != []:
                            total_pos.append(temp)
            for a in total_pos:
                for z in a:
                    if z[1] == y_coord:
                        for i in range(frm,to):
                            if z[0] == i:
                                return False
            return True
        else:
            return False

    short = temp('s',5,7)
    long = temp('l',1,4)
    return [short,long,y_coord]
