import pygame
from gs import gs,c_castle
from legal_pos import if_checkmate,legal_pos,check


# IMPORTANT_NOTE - I have to do 7 - y because the axis on the ui is not how I want it to be, y axis is flipped in ui

# initialise pygame
pygame.init()


# variables
prom_to = []
prom_frm = []
turn = 'W'
box_size = 100
max_fps = 15
color1 = (118, 150, 86)
color2 = (238, 238, 210)
colors = [color1,color2]
# capital letters represent color and small represent piece
pieces = ["Wp","Wr","Wn","Wb","Wq","Wk","Bp","Br","Bn","Bb","Bq","Bk"]


# create a window
screen = pygame.display.set_mode((8*box_size,8*box_size))


# loading images
icon = pygame.image.load("img/icon.png")
pieces_img = {}
for i in pieces:
    pieces_img[i] = pygame.transform.scale(pygame.image.load("img/"+i+".png"),(box_size,box_size))


# setting icon and caption
pygame.display.set_icon(icon)
pygame.display.set_caption("Chess")


def draw_board():
    # drawing a default 8*8 chess board
    for i in range(8):
        for j in range(8):
            color = colors[((i+j) % 2)]
            pygame.draw.rect(screen,color,(i*box_size,(7-j)*box_size,box_size,box_size))

# drawing pieces
def draw_pieces(gs):
    # draw a new board and then new pieces on the board according to the game state
    draw_board()
    for x in range(8):
        for y in range(8):
            if gs[x][y]["piece"] != "":
                screen.blit(pieces_img[gs[x][y]["piece"]["color"]+gs[x][y]["piece"]["name"]],(x*box_size,(7-y)*box_size))

    chk = check()
    if chk:
        pygame.draw.rect(screen,(255,50,50),(chk[0]*100,(7-chk[1])*100,box_size,box_size),10)

# move pieces
def move_pieces(frm,to):

    x,y = frm
    x1,y1 = to

    if gs[x][y]['piece']['name'] == 'k':
        c_castle[turn]['l'] = 'm'
        c_castle[turn]['s'] = 'm'
    elif gs[x][y]['piece']['name'] == 'r':
        if y == 0 or y == 7:
            if x == 0:
                c_castle[turn]['l'] = 'm'
            elif x == 7:
                c_castle[turn]['s'] = 'm'

    # check if it's the turn of the piece on frm coord
    if turn == gs[x][y]['piece']['color']:
        if gs[x][y]['piece']['name'] == 'k' and frm[0] - to[0] == 2 or frm[0] - to[0] == -2:
            y_coord = frm[1]
            if to[0] == 2:
                move_pieces([0,y_coord],[3,y_coord])
            else:
                move_pieces([7,y_coord],[5,y_coord])
        gs[x1][y1]["piece"] = gs[x][y]["piece"]
        gs[x][y]["piece"] = ""
        draw_pieces(gs)


def pawn_prom(frm,to,color):
    # update these global var to use them ahead in the infinite loop
    global prom_to
    prom_to = to
    global prom_frm
    prom_frm = frm

    # fill the screen white
    screen.fill((255,255,255))

    # draw a green rect in middle
    pygame.draw.rect(screen,color1,(350,200,100,400),0,10)

    # draw pieces on the rect
    screen.blit(pieces_img[color+'q'],(350,200))
    screen.blit(pieces_img[color+'r'],(350,300))
    screen.blit(pieces_img[color+'b'],(350,400))
    screen.blit(pieces_img[color+'n'],(350,500))


def pos_highlight(lgl_pos,frm):
    # hightlight the leagal positions (orange circle where the pieces can go and red circle around an enemy piece)
    for x in range(8):
        for y in range(8):
            for z in lgl_pos:
                if z == [x,y]:
                    # if the location has a piece and of opposite color
                    if gs[x][y]['piece'] != '' and gs[x][y]['piece']['color'] != gs[frm[0]][frm[1]]['piece']['color']:
                        pygame.draw.circle(screen,(255,120,120),(x*box_size+50,(7-y)*box_size+50),50,5)
                    else:
                        pygame.draw.circle(screen,(255, 159, 23),(x*box_size+50,(7-y)*box_size+50),15)


def checkmate(loser):
    if loser == 'W':
        winstmt = 'Black Wins'
    else:
        winstmt = 'White Wins'

    screen.fill(color2)
    font = pygame.font.Font('freesansbold.ttf', 64)
    text = font.render(winstmt, True, color1,color2)
    textRect = text.get_rect()
    textRect.center = (800 // 2, 800 // 2)
    screen.blit(text, textRect)


# the initial call
draw_pieces(gs)


# infinite loop
is_running = True
tracking = False
pawn_prom_menu = False
not_checkmate = True

while is_running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.MOUSEMOTION:
            # getting mouse coordinates and converting into chess coordinates (whenever mouse is moved)
            x,y = pygame.mouse.get_pos()
            x = int(x/box_size)
            y = 7-int(y/box_size)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (True,False,False):

                if not_checkmate:

                    if pawn_prom_menu:

                        x1,y1 = pygame.mouse.get_pos()
                        if x1 > 350 and x1 < 450:
                            # made a func on the go because have to use it 4 times
                            def prom(piece):
                                global turn
                                gs[prom_frm[0]][prom_frm[1]]['piece']['name'] = piece
                                move_pieces(prom_frm,prom_to)
                                if turn == 'W':
                                    turn = 'B'
                                else:
                                    turn = 'W'
                                chk = check()
                                if chk:
                                    print('ran')
                                    if if_checkmate(turn):
                                        checkmate(turn)

                            if y1 > 200 and y1 < 300:
                                prom('q')
                                pawn_prom_menu = False
                            elif y1 > 300 and y1 < 400:
                                prom('r')
                                pawn_prom_menu = False
                            elif y1 > 400 and y1 < 500:
                                prom('b')
                                pawn_prom_menu = False
                            elif y1 > 500 and y1 < 600:
                                prom('n')
                                pawn_prom_menu = False

                    # if tracking is false AND we are clicking on a piece AND it's our turn
                    elif tracking == False and gs[x][y]['piece'] and turn == gs[x][y]['piece']['color']:
                        all_pos = legal_pos(gs[x][y]['piece']['name'],[x,y],gs[x][y]['piece']['color'],turn,gs)
                        if all_pos != []:
                            frm = [x,y]
                            tracking = True
                            pos_highlight(all_pos,frm)


                    elif tracking == True:

                        # checking if we are doing a valid move
                        test = False
                        to = [x,y]
                        for i in all_pos:
                            if i == to:
                                test = True

                        # if it's not a valid move then just end the func
                        if test == False:
                            draw_pieces(gs)
                            tracking = False

                        #  if a white pawn is going to the 7th y coord
                        if gs[frm[0]][frm[1]]['piece']['name'] == 'p' and gs[frm[0]][frm[1]]['piece']['color'] == 'W' and test and y == 7:
                            pawn_prom(frm,to,'W')
                            pawn_prom_menu = True
                            tracking = False


                        #  if a black pawn is going to the 0th y coord
                        elif gs[frm[0]][frm[1]]['piece']['name'] == 'p' and gs[frm[0]][frm[1]]['piece']['color'] == 'B' and test and y == 0:
                            pawn_prom(frm,to,'B')
                            pawn_prom_menu = True
                            tracking = False

                        # if it's none of the above and it's a valid move then just move the piece and switch the turn
                        elif test == True:
                            move_pieces(frm,to)
                            if turn == 'W':
                                turn = 'B'
                            else:
                                turn = 'W'
                            chk = check()
                            if chk:
                                if if_checkmate(turn):
                                    checkmate(turn)

                            tracking = False

    # setting max fps and updating display
    pygame.time.Clock().tick(max_fps)
    pygame.display.flip()