import board
import json

cb = board.create_board()
with open("default.json") as pos:
    positions = json.loads(pos.read())
value = board.fill_board(cb, positions)

gs = cb

c_castle = {'W':{'l':'','s':''},'B':{'l':'','s':''}}
# w_castle = {'l':'','s':''} value of long and short castle can be 'm' for moved or empty
# when you move the rook with 0 x coord long castle's value will be 'm',
# when you move the rook with 7 x coord short castle's vlaue will be 'm'
# and when you move the king both of the values will be 'm'  